"""Plumbing checks. Cheap, default-on, no API calls."""

from __future__ import annotations

import json

from lib import EVALS_FILE, SKILL_PATH, Eval, build_prompt, parse_backend_output


def test_evals_json_loads():
    data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    assert data["skill_name"] == "kien-thai"
    assert isinstance(data["evals"], list) and data["evals"], "no evals defined"
    for e in data["evals"]:
        assert {"id", "name", "prompt", "register"} <= e.keys()


def test_skill_file_present():
    assert SKILL_PATH.exists(), f"missing {SKILL_PATH}"
    text = SKILL_PATH.read_text(encoding="utf-8")
    assert text.startswith("---"), "SKILL.md missing frontmatter"
    assert len(text) > 100, "SKILL.md suspiciously empty"


def test_skill_injection_differs_from_baseline(skill_text: str):
    sample = Eval(id=0, name="dummy", prompt="ทดสอบ", register="explainer")
    base = build_prompt(sample, "baseline", skill_text)
    injected = build_prompt(sample, "with_skill", skill_text)
    assert base != injected, "with_skill prompt identical to baseline"
    assert sample.prompt in injected, "task prompt missing from injected version"
    assert "skill" in injected.lower(), "skill content not actually injected"


def test_parse_claude_output():
    blob = json.dumps({
        "type": "result", "result": "Hello world.",
        "usage": {"input_tokens": 10, "cache_read_input_tokens": 1000,
                  "cache_creation_input_tokens": 0, "output_tokens": 4},
    })
    text, usage = parse_backend_output("claude", blob)
    assert text == "Hello world."
    assert usage["cache_read_input_tokens"] == 1000


def test_parse_codex_output():
    lines = [
        '{"type":"thread.started","thread_id":"x"}',
        '{"type":"turn.started"}',
        '{"type":"item.completed","item":{"id":"i0","type":"agent_message","text":"Hi."}}',
        '{"type":"turn.completed","usage":{"input_tokens":2000,"cached_input_tokens":1500,"output_tokens":3}}',
    ]
    text, usage = parse_backend_output("codex", "\n".join(lines))
    assert text == "Hi."
    assert usage["cached_input_tokens"] == 1500
