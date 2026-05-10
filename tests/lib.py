"""Shared eval-harness helpers (paths, loaders, prompt building).

Lives outside conftest.py to avoid the name collision pytest creates when
multiple conftest files coexist along a directory path.
"""

from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

from pythainlp.tokenize import word_tokenize

ROOT = Path(__file__).parent.parent
KIEN_THAI_DIR = ROOT / "skills" / "kien-thai"
SKILL_PATH = KIEN_THAI_DIR / "SKILL.md"
EVALS_FILE = ROOT / "evals" / "evals.json"
WORKSPACE = ROOT / "workspace"

# Bare-mode invocations. Skills are injected via prompt prepend, never via
# the backend's own skill-loading machinery — so the only delta between
# `with_skill` and `baseline` is the prompt.
BACKENDS: dict[str, list[str]] = {
    "claude": ["claude", "--disable-slash-commands", "-p"],
    "codex": ["codex", "exec"],
}

CONFIGS = ("with_skill", "baseline")


@dataclass(frozen=True)
class Eval:
    id: int
    name: str
    prompt: str


def load_evals() -> list[Eval]:
    data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    return [Eval(**e) for e in data["evals"]]


def latest_iteration() -> Path | None:
    if not WORKSPACE.exists():
        return None
    iters = sorted(
        (p for p in WORKSPACE.iterdir() if p.is_dir() and p.name.startswith("iteration-")),
        key=lambda p: int(p.name.split("-")[1]),
    )
    return iters[-1] if iters else None


def next_iteration_dir() -> Path:
    last = latest_iteration()
    n = (int(last.name.split("-")[1]) + 1) if last else 1
    d = WORKSPACE / f"iteration-{n}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def backend_available(backend: str) -> bool:
    return shutil.which(BACKENDS[backend][0]) is not None


_FENCE_RE = re.compile(r"^(\s*)(```|~~~)")
_HEADER_RE = re.compile(r"^(#{1,6}\s+)")
_LIST_RE = re.compile(r"^(\s*(?:[-*+]|\d+\.)\s+)")
_BLOCKQUOTE_RE = re.compile(r"^(\s*>+\s*)")


def _wrap_paragraph(text: str, width: int, prefix: str = "", cont: str = "") -> list[str]:
    tokens = word_tokenize(text, keep_whitespace=True)
    if not tokens:
        return [prefix + text]
    lines: list[str] = []
    cur = prefix
    cur_prefix = prefix
    for tok in tokens:
        candidate = cur + tok
        if len(candidate.rstrip()) > width and cur.rstrip() != cur_prefix.rstrip():
            lines.append(cur.rstrip())
            cur = cont + tok.lstrip()
            cur_prefix = cont
        else:
            cur = candidate
    if cur.strip():
        lines.append(cur.rstrip())
    return lines


def wrap_markdown(text: str, width: int = 90) -> str:
    """Wrap markdown for terminal readability. Thai-aware via pythainlp.

    Preserves fenced code blocks. Wraps paragraphs, headers, list items, and
    blockquotes while keeping their leading markers and continuation indent.
    """
    out: list[str] = []
    in_fence = False
    fence_marker: str | None = None
    for line in text.split("\n"):
        m = _FENCE_RE.match(line)
        if m:
            if in_fence and m.group(2) == fence_marker:
                in_fence = False
                fence_marker = None
            elif not in_fence:
                in_fence = True
                fence_marker = m.group(2)
            out.append(line)
            continue
        if in_fence or not line.strip():
            out.append(line)
            continue
        if (h := _HEADER_RE.match(line)):
            p = h.group(1)
            out.extend(_wrap_paragraph(line[len(p):], width, prefix=p, cont=" " * len(p)))
        elif (li := _LIST_RE.match(line)):
            p = li.group(1)
            out.extend(_wrap_paragraph(line[len(p):], width, prefix=p, cont=" " * len(p)))
        elif (bq := _BLOCKQUOTE_RE.match(line)):
            p = bq.group(1)
            out.extend(_wrap_paragraph(line[len(p):], width, prefix=p, cont=p))
        else:
            out.extend(_wrap_paragraph(line, width))
    return "\n".join(out)


def kien_thai_bundle() -> str:
    """SKILL.md + every references/*.md, framed for prompt injection.

    kode-thai's protocol requires loading kien-thai in full (skill + all four
    references) — most misses surface against the granular anti-patterns, not
    the seven frames alone.
    """
    parts = [SKILL_PATH.read_text(encoding="utf-8")]
    for ref in sorted((KIEN_THAI_DIR / "references").glob("*.md")):
        parts.append(f"\n\n## reference: {ref.name}\n\n{ref.read_text(encoding='utf-8')}")
    return "".join(parts)


def build_prompt(eval_case: Eval, config: str, skill_text: str) -> str:
    if config == "baseline":
        return eval_case.prompt
    return (
        "ใช้แนวทางการเขียนต่อไปนี้:\n\n"
        "<skill>\n"
        f"{skill_text}\n"
        "</skill>\n\n"
        "งานที่ต้องทำ:\n\n"
        f"{eval_case.prompt}"
    )
