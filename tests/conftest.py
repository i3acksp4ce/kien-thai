"""Top-level fixtures only. Shared helpers live in `lib.py` to avoid
the conftest name collision when nested conftest files exist.
"""

from __future__ import annotations

import pytest

from lib import kien_thai_bundle


@pytest.fixture(scope="session")
def skill_text() -> str:
    return kien_thai_bundle()
