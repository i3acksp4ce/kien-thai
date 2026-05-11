# Session checkpoint — 2026-05-11 — iteration-7 generation + review

Iteration-7 was generated (12 outputs, 3 evals × 2 backends × 2 configs)
and partially reviewed via the 1-by-1 protocol. Apply phase already
executed — all batch items completed. **Nothing committed yet**; resume
session decides commit chunking.

## How to resume

1. `git status` should show 7 modified + 4 untracked. Review the diffs.
2. Decide commit chunking — natural groups described in "Commit chunks"
   below.
3. Continue review on the remaining 10 iteration-7 outputs (un-reviewed
   in this session — see "Not done" below).

## What was done this session

**Generation.**

- `uv run pytest -m generate -n 4` produced 12 outputs, split across
  `iteration-7/` and `iteration-8/` due to xdist + session-scoped
  `iteration_dir` fixture (one logical iteration, two physical dirs).
- Manually consolidated all 12 outputs into `iteration-7/`. iter-8
  removed.
- Bug logged to `notes/work-queue.md`.

**Review (partial).**

Two outputs reviewed: `marketing-blurb/claude/with_skill` (lines 3, 4–5,
11) and `tech-doc-short/claude/with_skill` (`ทน` on `downstream`,
`มองกลับด้าน` → `มองกลับกัน`). Remaining 10 outputs un-reviewed.

**Skill content additions** (all checked in to working tree, not yet
committed):

- `skills/kien-thai/references/grammar.md` — new rules
  `quant-subject-cog-verb`, `tirai-frame-closure`, `frame-scoped-ko`
  (covers constitutive-vs-causal `ก็`).
- `skills/kien-thai/references/ai-tells.md` — new rule
  `whenever-calque` (English "whenever" → `ทีไร` vs
  `ไม่ว่าจะ…เมื่อไหร่`).
- `skills/kien-thai/references/register.md` — added "Deixis continuity"
  block under person-deixis section.
- `skills/kien-thai/references/examples.md` — added Examples 6, 7, 8
  (marketing-saas-sme register, before/after lifts from L3, L4–5, L11).

**Notes additions.**

- `notes/judgements/2026-05-11-cognitive-vs-affective-verbs.md`
- `notes/judgements/2026-05-11-frame-rules-have-idiomatic-edges.md`
- `notes/judgements/2026-05-11-person-deixis-discourse-over-syntax.md`
- `notes/work-queue.md` — xdist iteration-dir bug entry
- `notes/research-queue.md` — three deferred rule candidates with
  provenance, hypothesis, scope-to-investigate, landing target

**Per-iteration trace.**

- `workspace/iteration-7/feedback.md` — patterns observed,
  rule-candidate trace, judgements logged, followups.

**CLAUDE.md correction.**

- Added "Workspace outputs are evidence, not artifacts" block under
  Iteration discipline. Documents that eval subdirs are gitignored
  evidence, feedback.md is tracked, and the deliverable lives in
  `skills/kien-thai/references/*.md` + `notes/judgements/` +
  `workspace/iteration-N/feedback.md`. (Replaces a misplaced judgement
  file deleted during the session — context defect, not a prose-call
  override.)

**1-by-1 protocol** — refined and added to CLAUDE.md so future sessions
don't re-violate. Working shape: log agreed edits to a task batch, keep
discussing; actual work starts only after all discussion is done.

## Commit chunks (suggestion)

Natural separations for review:

1. **Skill content** — grammar.md + ai-tells.md + register.md +
   examples.md. Bundle as "iter-7: new rules from marketing-blurb +
   tech-doc review." References each other (`tirai-frame-closure` ↔
   `whenever-calque` cross-link).
2. **Judgements** — three judgement files. Bundle as "iter-7: three
   judgements logged."
3. **Notes infra** — work-queue.md (harness bug) + research-queue.md
   (three deferred candidates). Separate or fold into commit (1).
4. **CLAUDE.md + workspace/iteration-7** — CLAUDE.md "workspace
   evidence" block + feedback.md + skill 1-by-1 protocol. Bundle as
   "iter-7: feedback trace + CLAUDE.md clarifications."

Or fewer, bigger commits — chakrit's call.

## Not done

- **Review remaining 10 iter-7 outputs**: codex/with_skill on all 3
  evals, all 6 baselines, news-feature-bts both backends. May surface
  additional rule candidates and corroborating instances for the three
  deferred research-queue items.
- **Skill content rules deferred** (single-example provenance):
  hedge-stack collapse in marketing register; personification verbs on
  inanimate subjects; closer-binding scope reading discipline. All
  logged to `notes/research-queue.md` with provenance.
- **xdist iteration-dir harness bug**: not fixed. Logged to
  `notes/work-queue.md`. Do not run `-m generate -n >1` until fixed
  (or expect manual merge of split iteration directories).

## Open questions

None blocking. The three research-queue items each have a clear
"scope-to-investigate" path forward (look at remaining iter-7 outputs
and earlier iterations for corroborating instances).
