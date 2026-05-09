"""Generate artifacts using `codex exec`.

Run: `uv run pytest -m generate tests/generate/test_codex.py`
Skipped automatically if `codex` is not on PATH.
"""

from __future__ import annotations

import pytest

from lib import Eval

pytestmark = pytest.mark.generate


def test_codex(run_eval, eval_case: Eval, config: str):
    run_eval("codex", eval_case, config)
