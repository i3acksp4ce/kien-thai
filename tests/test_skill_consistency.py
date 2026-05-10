"""Cross-reference consistency for kien-thai skill files.

Catches the failure mode where deleting an anti-pattern (#11) silently orphans
a cross-ref in SKILL.md or another reference. Run as part of default pytest.

Also validates the slug system: each rule has a `` `slug` · type · scope ·
severity `` line under its heading, slugs are unique across all skill files,
and slug-form cross-references (`` `wrong-classifier` ``,
`` `f4/targhak-closure` ``) resolve.
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

# Slug definition: a backticked kebab-case (or f<N>/sub) token followed by
# ` · <type> · <scope> · <severity>`. Lives on its own line in body text.
SLUG_DEFN_RE = re.compile(
    r"^`([a-z0-9][a-z0-9/_-]*)`\s+·\s+\S+\s+·\s+\S+\s+·\s+\S+\s*$",
    re.MULTILINE,
)

# Slug reference: backticked token of slug shape. Conservative — kebab-case
# with at least one hyphen or a frame-sub form (`f<N>/...`). Avoids matching
# every backticked Thai word or single English token.
SLUG_REF_RE = re.compile(
    r"`(f[1-7](?:/[a-z][a-z0-9-]*)?|[a-z][a-z0-9]*(?:-[a-z0-9]+)+)`"
)

# Frame umbrella slugs (f1..f7) are defined implicitly by the frame headings
# plus the on-line `f<N>` slug under each frame heading.
FRAME_UMBRELLA_SLUGS = {f"f{n}" for n in range(1, 8)}

# Frame sub-pattern slugs (`f<N>/<descriptor>`) are introduced inline in SKILL.md
# rather than via a metadata definition line. Collect them as definitions when
# they first appear in SKILL.md.
FRAME_SUB_RE = re.compile(r"`(f[1-7]/[a-z][a-z0-9-]*)`")

# Tokens that look like slugs but are project / directory names. Treat as defined.
KNOWN_NON_RULE_TOKENS = {"kien-thai", "kode-thai"}


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


def _collect_slug_definitions() -> dict[str, list[Path]]:
    """Return slug -> list of files where it's defined."""
    slugs: dict[str, list[Path]] = {}
    for f in SKILL_FILES:
        text = f.read_text(encoding="utf-8")
        for m in SLUG_DEFN_RE.finditer(text):
            slugs.setdefault(m.group(1), []).append(f)
    # Frame sub-pattern slugs are inline-defined in SKILL.md.
    skill_md = SKILL_DIR / "SKILL.md"
    if skill_md.exists():
        text = skill_md.read_text(encoding="utf-8")
        for m in FRAME_SUB_RE.finditer(text):
            slugs.setdefault(m.group(1), [skill_md])
    return slugs


def test_slug_uniqueness():
    slugs = _collect_slug_definitions()
    dups = {s: paths for s, paths in slugs.items() if len(paths) > 1}
    assert not dups, "duplicate slugs:\n  " + "\n  ".join(
        f"{s}: {[str(p.relative_to(SKILL_DIR.parent.parent)) for p in paths]}"
        for s, paths in dups.items()
    )


def test_slug_cross_refs_resolve():
    defined = set(_collect_slug_definitions()) | FRAME_UMBRELLA_SLUGS | KNOWN_NON_RULE_TOKENS
    missing: list[str] = []
    for f in SKILL_FILES:
        text = f.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            # Skip the slug's own definition line.
            if SLUG_DEFN_RE.match(line):
                continue
            for m in SLUG_REF_RE.finditer(line):
                slug = m.group(1)
                if slug in defined:
                    continue
                # Skip false positives: file paths, env-style tokens. None expected
                # in current corpus, but keep the test forgiving.
                if "/" in slug and not slug.startswith(("f1/", "f2/", "f3/",
                                                        "f4/", "f5/", "f6/",
                                                        "f7/")):
                    continue
                rel = f.relative_to(SKILL_DIR.parent.parent)
                missing.append(f"{rel}:{line_no}: `{slug}` (line: {line.strip()[:120]})")
    assert not missing, "orphan slug cross-refs:\n  " + "\n  ".join(missing)
