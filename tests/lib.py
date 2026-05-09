"""Shared eval-harness helpers (paths, loaders, prompt building).

Lives outside conftest.py to avoid the name collision pytest creates when
multiple conftest files coexist along a directory path.
"""

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILL_PATH = ROOT / "skills" / "kien-thai" / "SKILL.md"
EVALS_FILE = ROOT / "evals" / "evals.json"
WORKSPACE = ROOT / "kien-thai-workspace"

# Bare-mode invocations. Skills are injected via prompt prepend, never via
# the backend's own skill-loading machinery — so the only delta between
# `with_skill` and `baseline` is the prompt.
BACKENDS: dict[str, list[str]] = {
    "claude": ["claude", "--bare", "--disable-slash-commands", "-p"],
    "codex": ["codex", "exec"],
}

CONFIGS = ("with_skill", "baseline")


@dataclass(frozen=True)
class Eval:
    id: int
    name: str
    prompt: str


def load_evals() -> list[Eval]:
    data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    return [Eval(**e) for e in data["evals"]]


def latest_iteration() -> Path | None:
    if not WORKSPACE.exists():
        return None
    iters = sorted(
        (p for p in WORKSPACE.iterdir() if p.is_dir() and p.name.startswith("iteration-")),
        key=lambda p: int(p.name.split("-")[1]),
    )
    return iters[-1] if iters else None


def next_iteration_dir() -> Path:
    last = latest_iteration()
    n = (int(last.name.split("-")[1]) + 1) if last else 1
    d = WORKSPACE / f"iteration-{n}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def backend_available(backend: str) -> bool:
    return shutil.which(BACKENDS[backend][0]) is not None


def build_prompt(eval_case: Eval, config: str, skill_text: str) -> str:
    if config == "baseline":
        return eval_case.prompt
    return (
        "ใช้แนวทางการเขียนต่อไปนี้:\n\n"
        "<skill>\n"
        f"{skill_text}\n"
        "</skill>\n\n"
        "งานที่ต้องทำ:\n\n"
        f"{eval_case.prompt}"
    )
