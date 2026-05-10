---
name: synthesis
description: Iter 08 — combined optimization roadmap, totals, implementation order
slice: synthesis across iters 00–07
---

# 08 — synthesis: total impact + implementation roadmap

Aggregates iters 00–07. Covers two architectural cuts not yet
detailed (two-tier injection, auditor/author split), then ranks the
whole opportunity stack by leverage.

## Architectural cuts (deferred from earlier iters)

### Two-tier injection (partially landed; fix-pass slimming rejected)

Pass-0 is **draft mode** — full skill, draft-time workflow intact.
Audit passes are **review mode** — workflow sections stripped.
**Fix passes always see the full register-scoped audit bundle.**
Per-pass slimming below the audit bundle was attempted in iter-6
(Stage 4) and rejected — see Stage 4 section.

Currently shipped: pass-0 = `kien_thai_bundle(register, mode='draft')`,
audit + fix = `kien_thai_bundle(register, mode='audit')`.

## Total token reduction stack

Codex tech-doc 5-pass case as the reference (worst case, no caching).

Layer-by-layer reduction:

| Stage | Per-pass | × 11 | Cum reduction |
| ----- | -------: | ---: | ------------: |
| Today | ~42,600 tok | ~470K | baseline |
| iter 01 SKILL.md cuts (~2,820 audit/fix; ~1,350 pass-0) | ~40,000 | ~440K | 6% |
| iter 02 ai-tells.md (~610) | ~39,400 | ~433K | 8% |
| iter 03 register.md (~5,400) | ~34,000 | ~374K | 20% |
| iter 04 examples.md (~3,100) | ~31,000 | ~341K | 27% |
| iter 05 style/craft (~230 net new) | ~30,800 | ~339K | 28% |
| iter 06 grammar/anti-patterns (~777) | ~30,000 | ~330K | 30% |
| iter 07 prompt framing (~150) | ~29,850 | ~328K | 30% |
| iter 07 prompt caching (Anthropic) | n/a (billed) | ~70K | varies |

(Stage 4 two-tier/slim-fix bundle is rejected — see Stage 4 section
below. Previous "~74% / ~85%" headline depended on it.)

For the converged-2-pass case (most cells today):
- Today: 4 × 42.6K = ~170K tok
- After iters 01–07 content cuts: 4 × 30K = ~120K tok (~30% off)
- After Anthropic caching: further reduction varies by hit rate.

## Implementation order (recommended)

Stage 1 — quick wins, low risk:

1. **iter 06 Cut D** — exclude anti-patterns.md from bundle.
   Rename to `_README-rules.md` or special-case the glob. **15 minutes.**
2. **iter 01 Cut A** — split SKILL.md workflow sections to
   `WORKFLOW.md`, inject only on pass-0. **1 hour.**
3. **iter 01 Cut C, D, E** — drop frontmatter description, citation
   provenance, references-list bloat from injection. **1 hour.**
4. **iter 02 Cut A, B** — drop dead audit-checklist refs and default
   metadata. **30 minutes.**
5. **iter 06 Cut A, B, C** — grammar.md trims. **30 minutes.**

Stage 1 total: **~6,000 tokens cut every pass, ~3 hours work.**
Codex tech-doc 5-pass: ~66K saved.

Stage 2 — register scoping (the headline win):

6. **iter 03 + iter 04 Cuts** — refactor `kien_thai_bundle()` to take
   `register` param; build per-register example bundles. Eval
   harness already threads register through; this is plumbing work,
   not API design.
   - Add `register_secondary` to `Eval` for cross-register cases.
   - Update audit/fix prompts to drop now-redundant register-scope
     advisory line (iter 07 Cut B).
   - Rerun the consistency test to confirm cross-references survive.
   **3 hours.**

Stage 2 total: **~8,500 tokens cut every pass, ~3 hours work.**
Codex tech-doc 5-pass: ~93K saved (additive).

Stage 3 — prompt caching (validate first):

7. **iter 07 Cut D** — instrument both backends with usage stats.
   Confirm cache behavior assumptions. **2 hours.**
8. **iter 07 Cut A** — reorder bundle for cross-cell cache hits.
   **30 minutes after measurement.**

Stage 3 total: **~70K saved on full eval run via caching alone.**

Stage 4 — slim fix-pass bundle (REJECTED, do not retry).

Original idea: on fix passes, ship only the cited rules from the
audit (plus SKILL frames + active register), since the fixer "only
needs to address what was flagged."

Tried in iter-6. Codex tech-doc-short — which Stages 1+2 had taken
from MAX_LOOP=5 down to 2-pass convergence — regressed straight
back to MAX_LOOP=5. Failure mode: each fix pass lost sibling-rule
context, so patching the cited issue introduced a fresh violation
that the next audit caught. Classic thrash. Telemetry showed each
pass-N citing a different rule than pass-(N-1).

**Locked principle:** fix passes always run with the full register-
scoped audit bundle. Iteration is tested with the full ruleset
applied. Per-pass slimming on principle, not just on the iter-6
regression — the fixer needs sibling-rule peripheral vision while
restructuring, and there is no slim-bundle design that preserves
that without re-introducing the full bundle.

Stage 4 helpers (`kien_thai_slim_fix_bundle`, `extract_cited_slugs`)
have been deleted. Do not re-introduce.

## What this analysis explicitly de-prioritized

- **Ai-tells.md format reflow** (iter 02 deferred) — ~30% cut on that
  file but risks losing auditor priming. Eval-validate before commit.
- **File merge into single rules.md** (iter 05 Cut F) — saves ~600 tok
  but loses the type/severity routing. Skip unless eval data motivates.
- **Workspace artifact compression** — not in any prompt path.
- **Eval prompt content** (`evals/evals.json`) — already minimal.
- **kode-thai SKILL.md** — separate runtime path (human-invoked,
  not eval); covered briefly in the cost map.

## Validation plan

Before each implementation stage commits, run:
1. `uv run pytest` — sanity + consistency.
2. `uv run pytest -m generate -k 'tech-doc-short and claude'` — single
   cell, fast. Confirm convergence behavior unchanged.
3. Compare meta.json `loop_passes` and `converged` values vs baseline.
4. Spot-check pass-N-audit.md citations — slug coverage stable.

Big-bang regression: rerun the full `pytest -m generate` against
the same eval set after Stage 2 lands and again after Stage 4 lands.
Compare pass counts, audit citation overlap, and final-output
diff-versus-baseline. If convergence patterns shift, that's data
about whether the cuts changed behavior.

## Stop condition for this audit loop

Iters 00–08 cover the bundle in full and architectural levers. Going
further requires:
- Eval data on whether cuts hurt quality (not a token-efficiency
  question).
- Implementation work to validate caching assumptions (instrumentation,
  not analysis).
- Future rule additions (corpus mining, eval feedback) — not this
  task.

**Loop complete.** No further high-value cuts findable from analysis
alone — remaining work is implementation + measurement.
