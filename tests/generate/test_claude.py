"""Generate artifacts using `claude --bare --disable-slash-commands -p`.

Run: `uv run pytest -m generate tests/generate/test_claude.py`
Skipped automatically if `claude` is not on PATH.
"""

from __future__ import annotations

import pytest

from lib import Eval

pytestmark = pytest.mark.generate


def test_claude(run_eval, eval_case: Eval, config: str):
    run_eval("claude", eval_case, config)
