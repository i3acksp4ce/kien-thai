"""Cross-reference consistency for kien-thai skill files.

Catches the failure mode where deleting an anti-pattern (#11) silently orphans
a cross-ref in SKILL.md or another reference. Run as part of default pytest.
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent / "skills" / "kien-thai"
SKILL_FILES = [SKILL_DIR / "SKILL.md"] + sorted(
    p for p in (SKILL_DIR / "references").glob("*.md") if p.is_file()
)

NUM_DEFN_RE = re.compile(r"^###\s+(\d+)\.\s", re.MULTILINE)
FRAME_DEFN_RE = re.compile(r"^###\s+Frame\s+(\d+)\s", re.MULTILINE)
NUM_REF_RE = re.compile(r"#(\d+)\b")
FRAME_REF_RE = re.compile(r"\bFrame\s+(\d+)\b")
F_SHORT_REF_RE = re.compile(r"\bF([1-7])\b")


def _collect_definitions() -> tuple[set[int], set[int]]:
    nums: set[int] = set()
    frames: set[int] = set()
    for f in SKILL_FILES:
        text = f.read_text(encoding="utf-8")
        nums.update(int(n) for n in NUM_DEFN_RE.findall(text))
        frames.update(int(n) for n in FRAME_DEFN_RE.findall(text))
    return nums, frames


def test_skill_files_exist():
    assert SKILL_FILES, "no skill files discovered"
    for f in SKILL_FILES:
        assert f.exists(), f


def test_anti_pattern_cross_refs_resolve():
    defined, _ = _collect_definitions()
    missing: list[str] = []
    for f in SKILL_FILES:
        text = f.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            # Skip the rule's own definition heading.
            if NUM_DEFN_RE.match(line):
                continue
            for m in NUM_REF_RE.finditer(line):
                n = int(m.group(1))
                if n not in defined:
                    rel = f.relative_to(SKILL_DIR.parent.parent)
                    missing.append(f"{rel}:{line_no}: #{n} (line: {line.strip()[:120]})")
    assert not missing, "orphan anti-pattern cross-refs:\n  " + "\n  ".join(missing)


def test_frame_cross_refs_resolve():
    _, defined = _collect_definitions()
    missing: list[str] = []
    for f in SKILL_FILES:
        text = f.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for m in FRAME_REF_RE.finditer(line):
                n = int(m.group(1))
                if n not in defined:
                    rel = f.relative_to(SKILL_DIR.parent.parent)
                    missing.append(f"{rel}:{line_no}: Frame {n}")
            for m in F_SHORT_REF_RE.finditer(line):
                n = int(m.group(1))
                if n not in defined:
                    rel = f.relative_to(SKILL_DIR.parent.parent)
                    missing.append(f"{rel}:{line_no}: F{n}")
    assert not missing, "orphan frame cross-refs:\n  " + "\n  ".join(missing)
