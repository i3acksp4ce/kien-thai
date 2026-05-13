"""Generate artifacts using `codex exec`.

Run: `EVAL_BACKENDS=claude,codex uv run pytest -m generate tests/generate/test_codex.py`
Opt-in via `EVAL_BACKENDS`; skipped by default. Also skipped if `codex` is not on PATH.
"""

from __future__ import annotations

import pytest

from lib import Eval, enabled_backends

pytestmark = pytest.mark.generate


def test_codex(run_eval, eval_case: Eval, config: str):
    if "codex" not in enabled_backends():
        pytest.skip("codex not in EVAL_BACKENDS (opt-in)")
    run_eval("codex", eval_case, config)
