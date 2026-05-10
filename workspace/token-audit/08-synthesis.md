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

### Two-tier injection

Pass-0 is **draft mode** — model needs the full skill to write well.
Audit and fix passes are **review mode** — they need the rule index
and the cited rules, not the full draft-time advice.

Today every pass ships the same ~42K-token bundle. Proposal:

| Pass type | Bundle content                                           | ~Tokens (post iter 01–07 cuts) |
| --------- | -------------------------------------------------------- | -----------------------------: |
| pass-0    | Full skill (frames + rules + active register + examples) | ~25–28K |
| audit     | Slim: SKILL frames + rule index + active register        | ~12–14K |
| fix-N     | Tinier: rule index + cited-rule details + active register | ~5–7K |

Citation flow:
- audit prompt asks for `slug · quoted text · suggested fix-direction`
  per issue.
- fix prompt receives the audit list. The harness extracts cited slugs
  and injects only those rule definitions (look up by slug in
  `rules-index.json`).

Mechanism: build a `rules-index.md` (or .json) at bundle time, ~50
tok/rule × ~50 rules ≈ 2.5K tokens. Each rule entry: `slug · file ·
1-line summary · 1 example pair`. Audit gets the index for browsing;
fix gets the index plus full rules expanded for cited slugs only.

Per-pass token cost (codex tech-doc 5-pass, post all cuts):
- pass-0: ~26K
- 5 audits: 5 × 13K = 65K
- 5 fixes: 5 × 6K = 30K
- **Total ~121K** vs current ~470K. **74% reduction.**

### Auditor/author file split

Subset of two-tier. Some rules are author-mode only (style-rules positive
guidance, ทับศัพท์ four-bucket guide, openers/closings); others are
auditor-mode only (forbidden-phrases blocklist, anti-pattern rules).

Crude split:

**Author bundle** (pass-0): SKILL frames + style-rules (positive) +
register active + examples active.

**Auditor bundle** (audit): SKILL frames + ai-tells + grammar + craft
+ forbidden-phrases + register active.

**Fixer bundle** (fix-N): cited rules + register active.

Estimated per-pass:
- pass-0 author bundle: ~22K
- audit bundle: ~18K
- fix bundle: ~5K

Subsumed by two-tier injection above, which is finer-grained. Keep
the split as a **fallback design** if rules-index.json proves brittle.

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
| iter 08 two-tier injection | ~26K avg | ~121K | **74%** |
| iter 07 prompt caching (Anthropic) | n/a (billed) | ~70K | **85%** |

**Total realistic target: ~85% cost reduction on the worst case.**

For the converged-2-pass case (most cells today):
- Today: 4 × 42.6K = ~170K tok
- After iters 01–07 content cuts: 4 × 30K = ~120K tok (~30% off)
- After two-tier (iter 08): pass-0 + audit + fix + audit ≈
  26K + 13K + 6K + 13K ≈ 58K tok (~66% off)
- After Anthropic caching: ~30K tok (~82% off)

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

Stage 4 — two-tier injection (biggest architectural shift):

9. Build `rules-index.md` (or .json) at bundle time. Each rule needs:
   - stable slug (already done in slug migration).
   - file path + line anchor.
   - 1-line summary.
   - canonical bad/good pair (1 each).
   **2 hours.**
10. Refactor `_run_loop()` to:
    - Pass-0: full bundle as today.
    - Audit: drop author-mode sections from bundle.
    - Fix-N: parse audit output for cited slugs, build slim bundle
      with index + cited rules expanded.
    **4 hours.**
11. A/B test with eval data: run iter-3-equivalent with both bundles,
    compare convergence + citation quality. **A full eval run +
    review.**

Stage 4 total: **biggest win, biggest implementation cost.** Defer
until Stages 1–3 are validated.

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
