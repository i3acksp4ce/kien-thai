---
name: SKILL.md analysis
description: Iter 01 — line-level breakdown of SKILL.md, dead refs, and audit/fix-pass cuts
slice: skills/kien-thai/SKILL.md
---

# 01 — SKILL.md (10,228 tokens)

Largest single file in the bundle. Found dead references and identified
~3K tokens of content that doesn't earn its keep on audit/fix passes.

## Dead references

- **`audit-checklist.md`** is referenced from `SKILL.md:352-353` and
  `references/ai-tells.md:12`, but the file was deleted in iter-2 prep
  (commit `df7d906`, REVIEW.md confirms). Pure dead weight that pollutes
  audit citations (LLM may cite a slug from a file that doesn't exist).
- Cut: ~30 tokens. Quality benefit > token benefit.

## Section breakdown (line ranges, est. tokens)

| Section                              | Lines     | ~Tokens | Audit/fix value |
| ------------------------------------ | --------- | ------: | --------------- |
| Frontmatter `description` (line 3)   | 1         |     370 | none — discovery-only |
| Why this skill exists                | 8–22      |     320 | low — motivation |
| Deeper problem: discourse frames     | 24–36     |     280 | low — motivation |
| Frames 1–7 (definitions + examples)  | 38–216    |   4,500 | **high — core reference** |
| Person-arity                         | 218–238   |     500 | high           |
| Stylistic conventions 1–6            | 240–265   |     520 | medium — overlaps style-rules.md |
| Workflow: writing                    | 267–309   |     900 | low on audit/fix |
| Workflow: editing                    | 311–315   |      90 | low on audit/fix |
| Workflow: translation                | 317–335   |     480 | low on audit/fix |
| References list                      | 337–353   |     320 | low — agent already has files |
| Citation provenance                  | 356–360   |     200 | none in prompt — human-doc only |
| Important: when in doubt             | 362–366   |      60 | low |

Total: ~10,228 (consistent with `wc -m` × 0.55).

## Concrete cuts

### Cut A — split out a `WORKFLOW.md`, inject only on pass-0
**Affects audit + fix passes only.** Lines 267–335 ("When asked to write
/ edit / translate") are author-mode instructions: pick register, draft
frame-first, self-edit, translation checklist. Auditor and fixer don't
need them — auditor reads existing prose against rules; fixer applies
specific issues.

- Move to `skills/kien-thai/WORKFLOW.md` (or keep inline + introduce
  a `BUNDLE_WORKFLOW=False` flag in `lib.kien_thai_bundle()`).
- **Pass-0 bundle**: includes WORKFLOW.
- **Audit + fix bundles**: omit WORKFLOW.
- Cut: ~1,470 tokens off every audit/fix pass.

For codex tech-doc 5-pass: 10 audit+fix invocations × 1,470 = **~14.7K
tokens saved per failure case** from this cut alone.

### Cut B — compress motivation into one paragraph
**All passes.** Lines 8–36 ("Why this skill exists" + "deeper problem")
total ~600 tokens. Both restate the same point: AI-Thai is mechanical,
calque-shaped, over-formal — fix via discourse frames, not surface
patches.

Compress to ~100 tokens (5 lines):

```
AI-generated Thai imports English's discourse mechanics whole-cloth and
adds polite/connective padding by default. Surface-level rules treat
symptoms; the seven frames below are the structure. Granular rules in
references/*.md become applications of the frames — most auto-resolve
once the frames are right.
```

Cut: ~500 tokens off **every pass** (pass-0, audit, fix). For codex
tech-doc 5-pass: 11 × 500 = 5,500 tokens saved.

### Cut C — citation provenance out of prompt
**All passes.** Lines 356–360 list scholarly sources. Useful for human
readers and for justifying rules in PRs; useless during draft/audit/fix.
LLM doesn't need to know that ก็ comes from Takahashi 2023 to apply it
correctly — the rule is what matters.

- Move to `skills/kien-thai/PROVENANCE.md` (human-readable index).
- Cut: ~200 tokens off every pass. 11 × 200 = 2,200 tokens for the bad case.

### Cut D — frontmatter description out of injection
**All passes.** Frontmatter `description:` is for skill auto-load
discovery — at runtime, the harness already decided to inject the
skill, so the description is redundant context. Currently
`kien_thai_bundle()` reads SKILL.md verbatim, frontmatter included.

- In `tests/lib.py:kien_thai_bundle()`, strip the YAML frontmatter
  before bundling.
- Cut: ~370 tokens off every pass. 11 × 370 = 4,070 tokens.

### Cut E — references list pruned to one line
**All passes.** Lines 337–353 enumerate every references/*.md with a
sentence each. The auditor/fixer is going to see all those files'
contents anyway because they're concatenated into the bundle. The
"read on demand" framing is a leftover from when references were
loaded lazily — now they're injected unconditionally.

- Replace 320 tokens of file-by-file blurb with one line:
  "References (full text below): ai-tells, grammar, craft, style-rules,
   register, examples, forbidden-phrases, anti-patterns."
- Net cut: ~280 tokens × 11 = 3,080 tokens for the bad case.

### Cut F — stylistic conventions deduplication (verify in iter 05)
**All passes.** Lines 240–265 list 6 numbered conventions:
verb-over-noun, particles-by-register, openers, concrete numbers, length
variance, mai-yamok. style-rules.md (5,493 tokens) almost certainly
expands the same six. Expected duplication: full ~520 tokens
recoverable from SKILL.md side. **Defer to iter 05** which audits style-
rules.md directly.

## Cumulative impact (this slice only)

Cuts A–E (excluding F pending iter 05):

| Cut | Tokens/pass | Passes affected      | Best case  | Worst (codex 5) |
| :-: | ----------: | -------------------- | ---------: | --------------: |
|  A  |       1,470 | audit + fix only     |     2,940* |          14,700 |
|  B  |         500 | every pass           |      1,000 |           5,500 |
|  C  |         200 | every pass           |        400 |           2,200 |
|  D  |         370 | every pass           |        740 |           4,070 |
|  E  |         280 | every pass           |        560 |           3,080 |
| **Σ** | **2,820 / 1,350** |              | **~5,640** |     **~29,550** |

\* converged-1-pass case (no audit needed) skips Cut A.

SKILL.md drops from 10,228 → ~7,400 tokens on audit/fix passes,
~8,870 on pass-0. **~30% reduction on the worst-case file alone.**

## Risks

- **Cut B (motivation compression)**: motivation prose may help the
  draft-mode model anchor. Test by running a single pass-0 with the
  compressed version and compare; if quality drops, restore.
- **Cut A (workflow split)**: if the auditor occasionally needs
  workflow context to judge ("is this opening line in spec?"), it
  loses access. Low risk — the 7 Frames + register.md already cover
  what the auditor judges against.
- **Cut F (style-rules dedup)**: blocked on iter 05.

## Decisions deferred

- Whether to keep frontmatter `description:` short *and* informative
  (~100 tokens) for human-facing skill catalogs, vs. strip entirely
  during injection. Stripping is the right move; description lives
  on disk for tooling.
- Whether to retire the dead `audit-checklist.md` references during
  this audit phase or wait for the implementation phase. Recommend:
  fix during audit since it's a 2-line cleanup with quality benefit.
