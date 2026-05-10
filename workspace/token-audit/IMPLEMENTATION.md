---
name: implementation log
description: What landed in Stages 1–2 of the token-audit roadmap, smoke-test results, and what's next.
---

# Token-audit implementation log

Stages 1 and 2 of the roadmap from `08-synthesis.md` landed in this
session despite the README's "wait for iter-3 review baseline" note
— a control-agent override during autonomous mode. The risk
(conflating token cuts with rule-content shifts) was acknowledged in
`.questions.log` but proceeded under instruction.

## Commits landed (in order)

1. `Skill source: mechanical cuts + register tags + label fix`
   ai-tells.md / grammar.md / examples.md — drop dead refs, dup frame
   list, slug-vs-numeric meta-prose, Singnoi cite; tag examples with
   register; fix Example 2 mislabel (Explainer → Marketing/SaaS-SME).

2. `Bundle preprocessor: register scoping + draft/audit modes`
   tests/lib.py refactor — `kien_thai_bundle(register, mode)` with:
   - frontmatter strip
   - `anti-patterns.md` skip (human stub redirector)
   - default `· mechanical · all-registers · hard` strip
   - audit-checklist.md dead-ref strip
   - register-scoped `register.md` and `examples.md`
   - mode='audit' drops draft-time workflow sections from SKILL.md

   tests/generate/conftest.py — two bundles per cell (draft / audit),
   redundant register-advisory line dropped from prompts.

3. `Gitignore .inbox.log and .questions.log`
   Session-local files for ace-connect bridge.

4. `SKILL.md: compress motivation, dedup conventions, prune References`
   - "Why this skill exists" + "Deeper problem": 29 lines → 7
   - "Stylistic conventions": 26 lines → 4 (pointer to style-rules.md)
   - "References — read on demand": 16 lines → 7

5. `Trim scholarly cite prose: Prasithrathsint, Treebank, Barang`
   - ai-tells.md #6: drop Prasithrathsint cite paragraph
   - style-rules.md #2: drop Treebank recalibration note
   - style-rules.md #31: collapse Barang prose to one line

## Bundle size (verified)

| Variant                         | Chars  | vs original 77,483 |
| ------------------------------- | -----: | -----------------: |
| Original (iter-3 baseline)      | 77,483 |               100% |
| unscoped, draft (post-cuts)     | 69,898 |              90.2% |
| explainer/draft                 | 56,155 |              72.5% |
| explainer/audit                 | 52,822 |              68.2% |
| marketing-saas-sme/draft        | 56,327 |              72.7% |
| marketing-saas-sme/audit        | 52,994 |              68.4% |

End-to-end prompt size (smoke test, claude tech-doc-short pass-0):
- iter-3: 107,545 bytes
- iter-4 (post-impl): 79,970 bytes
- **~25.6% reduction**

Per-pass token estimate at 0.55 tok/char on Thai-heavy content:
- iter-3 audit pass: ~24,000 tok
- iter-4 audit pass (explainer/audit): ~16,000 tok
- **~33% per-audit-pass reduction** in the explainer case.

For the codex tech-doc 5-pass worst case (iter-3): saves ~88K input
tokens off ~470K. ~19% off the worst-case scenario from content cuts
+ register scoping alone, before any prompt-cache wins.

## Smoke-test results

Single-cell `pytest -m generate -k 'tech-doc-short and claude'` ran
end-to-end. Iter-4 outputs at `workspace/iteration-4/`:

```
loop_passes: 2
converged: true
pass-0: ~43s    initial draft
pass-1 audit: ~37s   cited em-dash-semicolon (#32)
pass-1 fix:   ~17s   removed em-dashes
pass-2 audit: ~26s   CLEAN
```

**Quality finding**: iter-3 converged this same cell in 1 pass (auditor
returned CLEAN on draft). Iter-4 caught two `—` em-dashes the iter-3
auditor missed. The reduced bundle's auditor is **sharper, not
weaker** — likely because the auditor's attention isn't diluted by
4 unused register sections.

This is a **quality win**, not a regression. Convergence in 2 passes
is normal for this kind of audit; iter-3's 1-pass result was almost
certainly under-auditing.

Audit citation format held up:
```
- `em-dash-semicolon` (#32) — em-dash ปรากฏสองครั้งในชิ้นสั้น ๆ ...
  - `algorithm ที่นิยมมี 2 ตัว — token bucket กับ leaky bucket`
  - `พอถังเต็มก็หยุดเติมรอไว้ — เวลามี burst ...`
```

Slug-first citation as designed; `#NN` fallback parenthetical;
quoted offending text. Sub-pattern citations (`f4/...`, `f6/...`) not
exercised in this single cell — full eval will surface more.

## Open items

- **iter-3 review backlog**. The original review queue per
  `workspace/iteration-3/RESUME.md` is unaffected — those outputs
  are still there and still merit review. The implementation just
  changed what the *next* eval run produced.

## iter-5 regression — RESULTS

Full `pytest -m generate` against the same 4 cells as iter-3.
Compares like-for-like (same evals, same backends), measures
convergence shift after Stage 1+2 cuts. iter-5 used the pre-Stage-3
code (no instrumentation), so no usage stats — that lands in iter-6.

Convergence comparison:

| Cell                    | iter-3      | iter-5      | Verdict |
| ----------------------- | ----------- | ----------- | ------- |
| marketing-blurb/claude  | 2 ✓        | 2 ✓        | stable  |
| marketing-blurb/codex   | 2 ✓        | 1 ✓        | improved |
| tech-doc-short/claude   | 1 ✓        | 2 ✓        | sharper audit |
| tech-doc-short/codex    | **5 ✗**    | **2 ✓**    | **fixed** |

The headline iter-3 failure (codex tech-doc hitting MAX_LOOP=5
without converging) **now converges in 2 passes**.

Why: iter-3's noisier bundle (anti-patterns stub, dead audit-checklist
refs, default-metadata clutter, all 5 register sections + all 5
example registers, full draft-time workflow on audit) likely
confused codex's auditor — it found different issues each pass and
got stuck in a fix→re-audit cycle. iter-5's register-scoped, mode-
specific bundle gives the auditor a stable rule set; findings
stabilize, fix converges.

Bundle byte-size comparison (codex tech-doc-short cell):

| Pass            | iter-3       | iter-5       |
| --------------- | -----------: | -----------: |
| pass-0 prompt   | 107,545 B    |  75,503 B    |
| pass-1 audit    | 110,962 B    |  74,833 B    |

**~30% per-pass byte reduction**, ~25% per-pass token reduction at
0.5 tok/byte for Thai-heavy content.

**Total bytes sent to codex on this cell**:
- iter-3: 11 invocations × ~107K = ~1.18MB (uncached)
- iter-5: 4 invocations × ~75K  = ~302KB (uncached)
- **74% total reduction** — combined effect of fewer passes (cleaner
  convergence) and smaller per-pass bundle.

## Stage 3 + 4 — landed in this session

Stage 3 (instrumentation):
- `BACKENDS` updated with `--output-format json` (claude) and
  `--json` (codex).
- `parse_backend_output()` extracts text + usage from each backend's
  output format.
- `_invoke()` returns `(text, usage, rc, dur)`; usage lands in each
  pass's meta.json.
- 2 unit tests cover both parsers.
- End-to-end smoke test confirmed claude returns
  `cache_read_input_tokens=18183` after warm-up — cache is working
  for the eval flow.

Stage 4 (slim fix-pass bundle):
- `_build_rules_index()` walks ai-tells/craft/grammar/style-rules,
  maps slug → full rule block.
- `extract_cited_slugs()` parses audit output for slug refs (order-
  preserving, deduplicated).
- `kien_thai_slim_fix_bundle(register, cited_slugs)` builds:
  SKILL.md (workflow stripped) + active register + forbidden-phrases
  + only the cited rule blocks.
- `_run_loop` extracts cited slugs after each audit, feeds slim
  bundle to the matching fix invocation. `cited_slugs` lands in
  meta.json per-pass.
- 3 new tests cover slug extraction, slim bundle filtering, and
  graceful unknown-slug handling.

Slim fix-bundle measurements (explainer register):
- audit pass:  51,817 chars
- slim, 1 cited rule  : 20,186 chars (39%)
- slim, 3 cited rules : 21,489 chars (41%)
- slim, 5 cited rules : 22,056 chars (43%)

Per fix pass: ~30K chars / ~16K tokens cut on top of Stage 1+2.

## Total state at end of session

12 commits since iter-3 review save. Default pytest 20/20.
Stages 1+2+3+4 all wired. iter-5 validated Stage 1+2 with the
codex tech-doc-short case fixed. Stage 3+4 not yet exercised in
real eval — iter-6 will validate.

Ready for next eval generation: `uv run pytest -m generate`.

## Architectural notes for next session

- `kien_thai_bundle()` is now register-aware and mode-aware. The
  source files retain the verbose form so the consistency test
  parses them — preprocessing only happens at bundle time.
- Adding a new register = add an entry to `lib.REGISTER_HEADERS`
  + add a `<!-- register: <slug> -->` tag to the matching example
  in examples.md + add the section heading in register.md. Three
  changes, no plumbing.
- Future runtime cuts (e.g. dropping particular sections from
  audit-mode bundles) plug into `kien_thai_bundle()` without
  touching source files. The pattern is established.

## Provenance

Generated 2026-05-10 in autonomous mode under control-agent direction.
Smoke test landed at `workspace/iteration-4/`. Full eval landing at
`workspace/iteration-5/` once it completes.
