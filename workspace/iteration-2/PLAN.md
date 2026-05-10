# Iteration 2 — resume plan

Saved at the close of the kien-thai restructure session. This file is the
entry point when resuming in a new session.

## State at handoff

The skill has been restructured since iter-1. A fresh generation pass against
the new structure is the next step. **Iter-2 has not been run yet** — the
harness is wired but the eval generations haven't been kicked off.

### Recent commits (newest first)

```
6f3d4eb Integrate scholar-backed rule extensions + use/mention fix
4d8543f Slug pilot, audit-checklist wire-up, Thai-rewritten examples.md
2809b2f Split anti-patterns by rule type + add consistency test
e9b8146 Restructure kien-thai + wire kode-thai loop driver
6592509 Add corpus/ skeleton with research-agent resume protocol
80841d4 Get eval generation working end-to-end
```

### What changed since iter-1

1. **Marketing register family** — split out of Explainer with 4 sub-registers
   (SaaS-SME / B2B-formal / fintech-warm / retail-tech), corpus-derived.
2. **Voice promoted to peer of Register** — gender, brand mood, formality.
3. **Person-arity** as a top-level SKILL.md section (1st brand `เรา` / 2nd
   reader `คุณ` never demographic noun / 3rd product).
4. **Frames 4–7 expanded** — `ต่างหาก` closure, demonstrative bridge, standalone
   `แล้ว`, problem→solution pivot.
5. **Anti-patterns split by rule type**: `ai-tells.md` (mechanical),
   `craft.md` (preferences), `grammar.md` (surface). `audit-checklist.md`
   added as kode-thai entry point.
6. **kode-thai loop driver** wired in `tests/generate/conftest.py` —
   audit/fix subprocess loop until `CLEAN` or `MAX_LOOP=5`. The audit prompt
   now points at `audit-checklist.md` as the structured walk.
7. **Slug pilot** on `grammar.md` — each rule has slug + type/scope/severity
   metadata. Numbers stay stable as alternate IDs.
8. **Scholar citations** integrated into existing rules (Royal Institute,
   Olsson, Takahashi, Prasithrathsint, Singnoi, Treebank, Barang).
9. **Use/mention exemption** in `audit-checklist.md` blocklist — backticked
   occurrences are mention, not use; audit greps un-backticked only.
10. **Consistency test** (`tests/test_skill_consistency.py`) catches orphan
    cross-references. Runs on default `pytest`.
11. **Corpus**: 52 curated entries across 9 categories (8 register categories
    + scholarly). Prose gitignored; index in `corpus/README.md`. Resume
    protocol for further scouring in `corpus/RESUME.md`.

## Iter-2 plan

### What to run

```sh
uv run pytest -m generate
```

Generates 8 outputs under `workspace/iteration-2/`:
- 2 evals × 2 backends (claude, codex) × 2 configs (baseline, with_skill)
- `with_skill` config triggers the kode-thai loop (multi-pass audit/fix until
  CLEAN or MAX_LOOP=5). Pass artifacts saved alongside the final `output.md`.

Cost: claude is logged-in OAuth; codex is logged-in. No API keys needed.
Loop config will be slower than iter-1 since each `with_skill` run is now
multi-turn. Expect 10–20 minutes wall clock.

### What to look for in iter-2

Iter-1 review surfaced these specific patterns (now covered by skill rules).
The dogfood test of iter-2: does the loop catch and fix them?

- **Person-arity** — `เจ้าของร้าน` (demographic noun) substituted for `คุณ` in
  marketing copy. Audit should fire `demographic-noun` per SKILL.md
  Person-arity section. Fix should switch to `คุณ`.
- **Seam connectives** — `ต่างหาก` for contrastive correction, `โดย` for
  result+means, `แล้ว` for sequenced action, problem→solution pivot. Audit
  should fire #38, #40 (ai-tells.md). Fix should add the right particle.
- **Surface grammar** — wrong classifier (`bucket หนึ่งใบ`), missing `จะ`
  modal, function-word confusion (`เมื่อ` vs `เวลา`), verb-level calque
  (`ระเบิด`, `ทิ้ง`). Audit should fire #41–#44 (grammar.md). Fix should
  apply correct grammar.
- **Marketing-SaaS register relaxations** — `!` at hook, light interjection,
  warm CTA. Audit should NOT false-positive on these in SaaS-SME register.
  If it does, the scope notes in #19 / #24 (craft.md) need sharpening.
- **Forbidden phrase blocklist use/mention** — should not false-positive on
  examples.md's pattern-name mentions (handled by the use/mention exemption
  in audit-checklist.md).

### After iter-2 generation lands

1. Compare `workspace/iteration-2/<eval>/<backend>/with_skill/output.md`
   against iter-1 outputs. Note which patterns the loop caught and fixed.
2. Read each pass-N audit to see what the audit pass cited. Calibrate the
   audit prompt sharpness if too noisy or too lenient.
3. Update `workspace/iteration-2/feedback.md` (new file) with the trace per
   CLAUDE.md iteration discipline.
4. Decide rule deltas for iter-3.

### Sanity before generating

```sh
uv run pytest                 # default tests (sanity + consistency)
uv run pytest -m generate     # the actual iter-2 run
```

Default tests should be green before generation kicks off.

## Open items deferred to later iterations

- **Slug migration of remaining files** — only `grammar.md` has the slug
  metadata pilot. `ai-tells.md`, `craft.md` still use bare `### NN.` headings.
  Migrate after iter-2 if the slug format proves useful in audit outputs.
- **Empirical connective-density baselines** — Thai Discourse Treebank
  analysis. Would calibrate the current "≤1 ซึ่ง per 100 words" budgets.
  Separate corpus-analysis task, not blocking iter-2.
- **148-connective inventory mining** — Treebank's full connective list.
  Likely surfaces AI tells the skill doesn't currently name. Separate task.
- **kode-thai loop end-to-end validation** — the loop driver in
  `tests/generate/conftest.py` was wired but never tested before this save.
  Iter-2 *is* the first end-to-end test.
- **Corpus single-author bias** — `tech-writing` (somkiat only) and
  `translation` (Salforest only) need diversification. See `corpus/RESUME.md`.

## Files to read first when resuming

In order:

1. This file (`workspace/iteration-2/PLAN.md`).
2. `CLAUDE.md` — project conventions, especially iteration discipline.
3. `workspace/iteration-1/feedback.md` — full iter-1 trace.
4. `skills/kien-thai/SKILL.md` — current skill structure with frames + person-arity.
5. `skills/kien-thai/references/audit-checklist.md` — the audit pass entry point.
6. `tests/generate/conftest.py` — the loop driver (`_audit_prompt`,
   `_fix_prompt`, `_run_loop`, `MAX_LOOP`, `TIMEOUT_S`).

## Commands cheat-sheet

```sh
# Default tests
uv run pytest

# Generate (the iter-2 run)
uv run pytest -m generate

# Single eval × single backend (faster iteration)
uv run pytest -m generate -k 'tech-doc-short and claude'

# Advisory quant heuristics on latest iteration
uv run pytest -m evaluate
```
