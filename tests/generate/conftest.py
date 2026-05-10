"""Generation-stage fixtures: baseline single-shot, with_skill = kode-thai loop."""

from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path

import pytest

from lib import (
    BACKENDS,
    CONFIGS,
    Eval,
    backend_available,
    build_prompt,
    load_evals,
    next_iteration_dir,
    wrap_markdown,
)

MAX_LOOP = 5
TIMEOUT_S = 300


@pytest.fixture(scope="session")
def iteration_dir() -> Path:
    return next_iteration_dir()


def pytest_generate_tests(metafunc):
    if "eval_case" in metafunc.fixturenames:
        evals = load_evals()
        metafunc.parametrize("eval_case", evals, ids=[e.name for e in evals])
    if "config" in metafunc.fixturenames:
        metafunc.parametrize("config", CONFIGS)


def _invoke(backend: str, prompt: str) -> tuple[str, int, float]:
    cmd = [*BACKENDS[backend], prompt]
    t0 = time.monotonic()
    proc = subprocess.run(
        cmd, capture_output=True, text=True, timeout=TIMEOUT_S, env={**os.environ}
    )
    return proc.stdout, proc.returncode, time.monotonic() - t0


def _run_once(backend: str, prompt: str, out_dir: Path, label: str) -> tuple[str, float]:
    (out_dir / f"{label}-prompt.txt").write_text(prompt, encoding="utf-8")
    stdout, rc, dur = _invoke(backend, prompt)
    assert rc == 0, f"{backend} {label} exited {rc}: {stdout[:500]}"
    assert stdout.strip(), f"{backend} {label} empty output"
    return stdout, dur


def _audit_prompt(prose: str, bundle: str) -> str:
    return (
        "ใช้แนวทางการเขียนต่อไปนี้:\n\n"
        "<skill>\n" + bundle + "\n</skill>\n\n"
        "งาน: ใช้ `audit-checklist.md` ใน skill เป็น entry point — เดินตามส่วน "
        "Mechanical ทีละข้อก่อน แล้วค่อยทำ Craft (filter ตาม register ของ prose). "
        "สำหรับทุก violation ระบุ rule slug (เช่น `wrong-classifier`, "
        "`missing-cha-modal`) หรือ #NN พร้อมยกข้อความที่ผิด. "
        "ถ้าผ่านทุกข้อ ให้ตอบบรรทัดเดียวว่า `CLEAN` ห้าม output prose\n\n"
        "<prose>\n" + prose + "\n</prose>"
    )


def _fix_prompt(prose: str, audit: str, bundle: str) -> str:
    return (
        "ใช้แนวทางการเขียนต่อไปนี้:\n\n"
        "<skill>\n" + bundle + "\n</skill>\n\n"
        "issue ที่ต้องแก้:\n\n" + audit + "\n\n"
        "prose ปัจจุบัน:\n\n<prose>\n" + prose + "\n</prose>\n\n"
        "งาน: แก้ prose ตาม issue ข้างบน output เฉพาะ prose ที่แก้แล้ว "
        "ห้ามใส่คำอธิบาย ห้ามใส่หัวเรื่อง"
    )


def _is_clean(audit: str) -> bool:
    txt = audit.strip()
    if not txt:
        return False
    return txt.splitlines()[0].strip().upper().startswith("CLEAN")


def _run_baseline(backend: str, eval_case: Eval, out_dir: Path, skill_text: str) -> dict:
    prompt = build_prompt(eval_case, "baseline", skill_text)
    stdout, dur = _run_once(backend, prompt, out_dir, "input")
    (out_dir / "output.md").write_text(wrap_markdown(stdout), encoding="utf-8")
    return {"duration_s": round(dur, 2)}


def _run_loop(backend: str, eval_case: Eval, out_dir: Path, bundle: str) -> dict:
    initial_prompt = build_prompt(eval_case, "with_skill", bundle)
    prose, dur0 = _run_once(backend, initial_prompt, out_dir, "pass-0")
    (out_dir / "pass-0.md").write_text(wrap_markdown(prose), encoding="utf-8")
    passes: list[dict] = [{"pass": 0, "kind": "initial", "duration_s": round(dur0, 2)}]

    converged = False
    last_pass = 0
    for i in range(1, MAX_LOOP + 1):
        audit, audit_dur = _run_once(backend, _audit_prompt(prose, bundle), out_dir, f"pass-{i}-audit")
        (out_dir / f"pass-{i}-audit.md").write_text(audit.strip() + "\n", encoding="utf-8")
        clean = _is_clean(audit)
        passes.append({"pass": i, "kind": "audit", "duration_s": round(audit_dur, 2), "clean": clean})
        last_pass = i
        if clean:
            converged = True
            break
        prose, fix_dur = _run_once(backend, _fix_prompt(prose, audit, bundle), out_dir, f"pass-{i}-fix")
        (out_dir / f"pass-{i}.md").write_text(wrap_markdown(prose), encoding="utf-8")
        passes.append({"pass": i, "kind": "fix", "duration_s": round(fix_dur, 2)})

    (out_dir / "output.md").write_text(wrap_markdown(prose), encoding="utf-8")
    return {"loop_passes": last_pass, "converged": converged, "passes": passes}


@pytest.fixture
def run_eval(iteration_dir: Path, skill_text: str):
    def _run(backend: str, eval_case: Eval, config: str) -> Path:
        if not backend_available(backend):
            pytest.skip(f"{backend} not on PATH")
        out_dir = iteration_dir / eval_case.name / backend / config
        out_dir.mkdir(parents=True, exist_ok=True)
        if config == "baseline":
            extra = _run_baseline(backend, eval_case, out_dir, skill_text)
        else:
            extra = _run_loop(backend, eval_case, out_dir, skill_text)
        (out_dir / "meta.json").write_text(
            json.dumps(
                {
                    "backend": backend,
                    "config": config,
                    "eval_id": eval_case.id,
                    "eval_name": eval_case.name,
                    **extra,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        return out_dir / "output.md"

    return _run
