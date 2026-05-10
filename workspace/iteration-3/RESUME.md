---
name: iter-3 resume
description: Entry point for resuming iter-2/3 review. Outputs landed in iter-3, not iter-2.
---

# Iter-3 — resume entry point

Read this first. `workspace/iteration-2/REVIEW.md` is still the review
protocol; only the directory name changed.

## What happened this session

- Iter-2 generation was kicked off in background (`uv run pytest -m generate`).
  Completed in 18:18 wall clock, 8 passed.
- **Outputs landed in `workspace/iteration-3/`**, not iter-2 — the harness
  auto-numbers to the next empty iteration dir. iter-2 prep work
  (`PLAN.md`, `REVIEW.md`, `audit-gaps.md`) stayed in iteration-2/.
- No code edits this session. Tree clean except untracked `.claude/`.

## Convergence summary

| Cell                    | Passes | Converged                  |
| ----------------------- | -----: | :------------------------- |
| marketing-blurb/claude  |      2 | ✓                          |
| marketing-blurb/codex   |      2 | ✓                          |
| tech-doc-short/claude   |      1 | ✓ (initial draft clean)    |
| tech-doc-short/codex    |      5 | ✗ hit MAX_LOOP             |

Headline: **codex tech-doc-short never reached CLEAN over 5 rounds**. Either
auditor stuck on false positives, or the rule set is internally inconsistent
for that register. Highest-priority cell to read.

Secondary curiosity: claude tech-doc-short converged on pass-0 — auditor
either correctly found a clean draft, or failed to flag anything. Read the
single audit to disambiguate.

## Next session — review protocol

Follow `workspace/iteration-2/REVIEW.md` steps 1–6 against
`workspace/iteration-3/`. Order of attack:

1. **codex tech-doc-short loop trace** — read all 5 `pass-N-audit.md` and
   diff `pass-(N-1).md` → `pass-N.md`. Likely deserves an isolated agent
   (5 audits + 5 fixes + 5 audit-prompts is heavy). Question to answer:
   are citations sharp + genuine violations, or is the auditor flagging
   the same false-positive across passes?
2. **claude tech-doc-short pass-1-audit.md** — verify the auditor actually
   inspected, didn't shortcut to CLEAN.
3. **marketing-blurb both backends** — clean 2-pass convergence; spot-check
   citation quality + register-scoped fixes (no demographic noun, single
   `!` allowed, no ครับ/ค่ะ in body).
4. Write `workspace/iteration-3/feedback.md` per CLAUDE.md iteration
   discipline — trace each finding to existing rule before proposing
   deltas.

## Parallel track (kicked off this session)

User started a **self-analysis loop on repo token efficiency**. That work
runs alongside / before review. Do not let it edit the skill content
without review converging first — token-efficiency edits to
`skills/kien-thai/references/*.md` could change what the next iter
generates against. Coordinate ordering before merging.
