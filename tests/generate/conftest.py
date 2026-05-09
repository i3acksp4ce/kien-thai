"""Generation-stage fixtures.

Each test_<backend>.py runs every eval × every config against one backend.
Outputs land in workspace/iteration-N/<eval>/<backend>/<config>/.
"""

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


@pytest.fixture(scope="session")
def iteration_dir() -> Path:
    return next_iteration_dir()


def pytest_generate_tests(metafunc):
    if "eval_case" in metafunc.fixturenames:
        evals = load_evals()
        metafunc.parametrize("eval_case", evals, ids=[e.name for e in evals])
    if "config" in metafunc.fixturenames:
        metafunc.parametrize("config", CONFIGS)


def _invoke(backend: str, prompt: str, timeout: int = 180) -> tuple[str, int, float]:
    cmd = [*BACKENDS[backend], prompt]
    t0 = time.monotonic()
    proc = subprocess.run(
        cmd, capture_output=True, text=True, timeout=timeout, env={**os.environ}
    )
    return proc.stdout, proc.returncode, time.monotonic() - t0


@pytest.fixture
def run_eval(iteration_dir: Path, skill_text: str):
    """Returns a callable: (backend, eval_case, config) -> output path."""

    def _run(backend: str, eval_case: Eval, config: str) -> Path:
        if not backend_available(backend):
            pytest.skip(f"{backend} not on PATH")

        out_dir = iteration_dir / eval_case.name / backend / config
        out_dir.mkdir(parents=True, exist_ok=True)

        prompt = build_prompt(eval_case, config, skill_text)
        (out_dir / "prompt.txt").write_text(prompt, encoding="utf-8")

        stdout, rc, duration = _invoke(backend, prompt)
        (out_dir / "output.md").write_text(wrap_markdown(stdout), encoding="utf-8")
        (out_dir / "meta.json").write_text(
            json.dumps(
                {
                    "backend": backend,
                    "config": config,
                    "eval_id": eval_case.id,
                    "eval_name": eval_case.name,
                    "returncode": rc,
                    "duration_s": round(duration, 2),
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        assert rc == 0, f"{backend} exited {rc}: {stdout[:500]}"
        assert stdout.strip(), f"{backend} produced empty output"
        return out_dir / "output.md"

    return _run
