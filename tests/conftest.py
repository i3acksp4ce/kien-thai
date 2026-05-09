"""Top-level fixtures only. Shared helpers live in `lib.py` to avoid
the conftest name collision when nested conftest files exist.
"""

from __future__ import annotations

import pytest

from lib import SKILL_PATH


@pytest.fixture(scope="session")
def skill_text() -> str:
    return SKILL_PATH.read_text(encoding="utf-8")
