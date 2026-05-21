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

---

## Browser tooling for Thai source vetting ✅ unblocked 2026-05-13

**Status.** Claude-in-Chrome MCP wired up. Used for the 2026-05-13 vetting
pass — see [`source-vetting-2026-05-13.md`](source-vetting-2026-05-13.md).
Worked well for GotoKnow, readthecloud.co, storyloggroup.com, Pantip.
Minimore continues to return empty body even via Chrome (same JS-render
block as WebFetch); use Wayback / paste-in for those.

**Outstanding constraint.** Some sites still don't yield prose:

- Minimore — SPA renders empty in the MCP context. Use Archive.org or
  user paste-in.
- Subscription-gated content (if ever needed) would require logged-in
  profile; current setup is clean profile, read-only.

The original block-condition on the broadened Register 3 Models list is
resolved — `references/register.md` is now evidence-backed.

Below is the original entry for archive.

---

**Need.** Autonomous source-research for Thai prose models is blocked because
WebFetch hits 403 / empty-render across the primary candidate sites (GotoKnow,
readthecloud.co, minimore.com, fungjaizine.com). Without rendered prose,
grammar-discipline tier verdicts can't be made — see
[`research-queue.md`](research-queue.md) → "Vet non-tech personal-blog source
candidates."

**Decided.** Wire up a Chrome / browser MCP so Claude can navigate JS-rendered
pages, get past bot blocks, and extract verbatim Thai prose. Chakrit (2026-05-13)
confirmed this is the unblock path.

**Open design choices.**

- Which MCP: Chrome DevTools MCP, browser-MCP, or playwright-mcp.
- Auth/profile: should the browser run with a clean profile or chakrit's
  logged-in profile (relevant if we ever want subscription-gated content).
- Scope: vetting reads only, no form-submission / write actions.

**Block.** Do not ship the broadened Register 3 Models list (currently
provisional in `references/register.md`) as evidence-backed until this lands
and the vetting pass completes.

---

## Framing experiments for Thai-native generation

**Need.** Bundle ordering and exemplar proximity matter for shifting
Claude's output distribution toward Thai-native prose. Literature
(multilingual ICL, English-accent paper, persona effect, multilingual
CoT) confirms prompt-level techniques have measurable — though
"marginal or inconsistent" — effects. The biggest under-used lever in
the current harness: `examples.md` sits mid-bundle alphabetically, so
the most concentrated native-Thai prose in the bundle is *not* adjacent
to the task prompt where attention recency would amplify it.

**Scope.** Add new harness configs alongside `with_skill` and `baseline`
in `tests/lib.py:CONFIGS`. Three ranked experiments per the framing
investigation:

1. `with_skill_reordered` — `examples.md` last in bundle. 5-line change
   in `kien_thai_bundle()`. Zero new content.
2. `with_skill_primed` — adds curated native-prose exemplars from
   `corpus/native-exemplars/<register>.md` after `examples.md`. Needs a
   small curated corpus (2–3 short pieces per register) before this can
   run.
3. `with_skill_persona` — register-keyed Thai-language persona prepend
   naming a specific publication/voice. Tested against #1+#2.

**Findings so far.** Literature lens, recommended ordering, and the
"don't force Thai-language CoT for mid-resource languages" caveat
captured in
[`notes/framing-investigation-2026-05-21.md`](framing-investigation-2026-05-21.md).

**Open design choices.**

- Whether the three variants A/B independently or stack into a single
  `with_skill_primed` super-variant.
- Where curated exemplars live (`corpus/native-exemplars/` vs
  `references/exemplars.md`).
- How to measure improvement — `test_quant.py` advisory heuristics +
  human review (the existing convention), or add LLM-judge later.

**Block.** None. Independent of in-flight skill work.

---

## Eval harness: xdist splits iteration directory across workers

**Need.** `tests/generate/conftest.py` exposes `iteration_dir` as a
session-scoped pytest fixture that calls `next_iteration_dir()`. Under
`pytest-xdist -n N`, each worker has its own session, so each worker mints
a fresh iteration directory. A single `pytest -m generate -n 4` run produces
N iteration dirs containing partial slices of the matrix instead of one
complete iteration.

**Repro.** Iteration-7 generation (2026-05-11): one `pytest -m generate -n 4`
run produced 12 outputs split 6/6 across `iteration-7/` and `iteration-8/`.
Manual consolidation required before review.

**Fix candidates.**

- Resolve the iteration dir in the xdist controller pre-fork and broadcast
  via env var or `--iteration-dir` CLI flag.
- Use `tmp_path_factory`-style shared-state mechanism that xdist plugins
  already support.
- Drop session scope; have one designated rank-0 worker write a manifest
  the others read.

**Block.** Do not run `-m generate -n >1` until fixed, or expect to
manually merge iteration directories afterward.
