"""Plumbing checks. Cheap, default-on, no API calls."""

from __future__ import annotations

import json

from lib import EVALS_FILE, SKILL_PATH, Eval, build_prompt


def test_evals_json_loads():
    data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    assert data["skill_name"] == "kien-thai"
    assert isinstance(data["evals"], list) and data["evals"], "no evals defined"
    for e in data["evals"]:
        assert {"id", "name", "prompt"} <= e.keys()


def test_skill_file_present():
    assert SKILL_PATH.exists(), f"missing {SKILL_PATH}"
    text = SKILL_PATH.read_text(encoding="utf-8")
    assert text.startswith("---"), "SKILL.md missing frontmatter"
    assert len(text) > 100, "SKILL.md suspiciously empty"


def test_skill_injection_differs_from_baseline(skill_text: str):
    sample = Eval(id=0, name="dummy", prompt="ทดสอบ")
    base = build_prompt(sample, "baseline", skill_text)
    injected = build_prompt(sample, "with_skill", skill_text)
    assert base != injected, "with_skill prompt identical to baseline"
    assert sample.prompt in injected, "task prompt missing from injected version"
    assert "skill" in injected.lower(), "skill content not actually injected"
