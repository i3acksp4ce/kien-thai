# Work queue

Decided work items awaiting design/build. Distinct from `research-queue.md`
(speculative items needing evidence) and `judgements/` (retrospective entries
about calls already made). Items here are committed scope — the question is
*how*, not *whether*.

---

## Thai-aware markdown wrap tooling

**Need.** Enforce the CLAUDE.md hard-wrap-90 rule on Thai-heavy markdown.
Naïve codepoint-based wrapping overshoots ~10–15% on Thai prose because Thai
combining marks (vowel signs, tone marks) are zero-width but count as
codepoints. Thai also has no word spaces, so line-break candidates need
dictionary-based segmentation rather than splitting on whitespace.

**Scope.** Uniform across every `.md` the repo produces or maintains —
`SKILL.md`, `references/*.md`, `notes/*.md`, `CONTRIBUTING.md`, eval feedback
files. Includes both authoring help and CI enforcement.

**Findings so far.**

- `pythainlp` is already in deps and provides `word_tokenize` for
  segmentation.
- `wcwidth` handles display-width counting for the codepoint-vs-display
  problem.
- ICU4C is the heavier alternative; full Unicode-segmentation, but a much
  bigger dependency.

**Open design choices.**

- Stack: Python + pythainlp + wcwidth, vs ICU, vs something else.
- Integration point: standalone CLI, pre-commit hook, generator post-
  processor, or all three.

**Block.** Do not hand-fix Thai-prose wrap regressions until this exists —
the manual fixes won't survive the next eval generation pass.

---

## Thai dictionary lookup capability

**Need.** When uncertain about Thai spelling or word usage, both Claude and
contributors should be able to verify against an authoritative Thai source
rather than rely on memory or web search. Today there is no project-local
way to confirm `กฎ` vs `กฏ`, `นัย` vs `นัยยะ`, etc.

**Scope.**

- Source: Royal Institute Dictionary published forms? pythainlp-bundled
  dictionary? other?
- Storage: gitignored or checked in (depends on size and license).
- Access: CLI tool, Python helper for tests, or raw file lookup.

**Open.** Licensing — RID dictionaries may not be redistributable, in which
case this becomes a per-developer download with a setup script rather than
a checked-in resource.

**Block.** Do not make confident orthography claims in skill or contributor
docs until this exists. Today every spelling call is from-memory and
unverifiable.
