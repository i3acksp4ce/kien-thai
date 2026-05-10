r"""Cross-reference consistency for kien-thai skill files.

Validates the slug system: each rule has a heading of the form
`### \`<slug>\` *(<type> · <scope> · <severity>)*`, slugs are unique across all
skill files, and slug-form cross-references (`` `wrong-classifier` ``,
`` `f4/targhak-closure` ``) resolve. Frame number cross-references
(`Frame N`, `FN`) resolve to a defined frame heading.
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent / "skills" / "kien-thai"
SKILL_FILES = [SKILL_DIR / "SKILL.md"] + sorted(
    p for p in (SKILL_DIR / "references").glob("*.md") if p.is_file()
)

FRAME_REF_RE = re.compile(r"\bFrame\s+(\d+)\b")
F_SHORT_REF_RE = re.compile(r"\bF([1-7])\b")
FRAMES_DEFINED = frozenset(range(1, 8))

# Slug definition: the unified rule heading.
#   ### `<slug>` *(<type> · <scope> · <severity>)*
SLUG_DEFN_RE = re.compile(
    r"^###\s+`([a-z0-9][a-z0-9/_-]*)`\s+\*\([^)]+\)\*\s*$",
    re.MULTILINE,
)

# Slug reference: backticked token of slug shape — kebab-case with at least one
# hyphen, or a frame-sub form (`f<N>/...`).
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


def test_skill_files_exist():
    assert SKILL_FILES, "no skill files discovered"
    for f in SKILL_FILES:
        assert f.exists(), f


def test_no_legacy_numbered_refs():
    """Numbered IDs (#NN) are gone — slugs replaced them. Catches regressions."""
    pattern = re.compile(r"#\d+\b")
    violations: list[str] = []
    for f in SKILL_FILES:
        for line_no, line in enumerate(f.read_text(encoding="utf-8").splitlines(), start=1):
            if pattern.search(line):
                rel = f.relative_to(SKILL_DIR.parent.parent)
                violations.append(f"{rel}:{line_no}: {line.strip()[:120]}")
    assert not violations, "legacy `#NN` refs found:\n  " + "\n  ".join(violations)


def test_frame_cross_refs_resolve():
    defined = FRAMES_DEFINED
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
