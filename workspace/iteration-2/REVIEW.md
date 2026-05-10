# Iteration 2 — review entry point

Read this first when resuming. PLAN.md is historical (written before iter-2
prep landed); audit-gaps.md is the trace of the prep work. This file is
about reviewing iter-2 *outputs*.

## State at handoff

Iter-2 generation kicked off at the end of the prep session. Check status:

```sh
rtk ls workspace/iteration-2/
```

Expected layout once the run completes:

```
workspace/iteration-2/
├── PLAN.md                       # historical
├── audit-gaps.md                 # prep-work trace
├── REVIEW.md                     # this file
├── tech-doc-short/
│   ├── claude/{baseline,with_skill}/
│   └── codex/{baseline,with_skill}/
└── marketing-blurb/
    ├── claude/{baseline,with_skill}/
    └── codex/{baseline,with_skill}/
```

Each `with_skill/` dir holds the loop trace: `pass-0.md` (initial draft),
`pass-N-audit.md` + `pass-N.md` per fix iteration, `output.md` (final),
`meta.json` (convergence + timing).

If `output.md` is missing or `meta.json` shows `converged: false`, the loop
hit MAX_LOOP=5 without reaching CLEAN. That's data, not failure — note it.

## What changed since iter-1 (load-bearing for review)

This is the *intended design* under test in iter-2. If iter-2 outputs look
worse than iter-1, the design needs revisiting; if better, the design is
working.

1. **Audit-checklist removed.** Audit pass is now read-and-judge, not
   walk-the-checkboxes. Auditor cites violations with slug-first, `#NN`
   fallback, plus quoted offending text. Forbidden-phrase blocklist
   (`forbidden-phrases.md`) runs as a pre-check.
2. **Slug migration completed.** Frame umbrellas (`f1`–`f7`), Frame
   sub-patterns (`f4/targhak-closure`, `f6/ko-resumptive`, etc.),
   ai-tells (~29 rules), craft (~10 rules), grammar (#46/#47 added) all
   carry slugs + `type · scope · severity` metadata. Sub-pattern slugs
   exist precisely so audit citations land at the right granularity for
   Frame violations.
3. **Register tag threaded through harness.** Eval entries carry
   `register` (`explainer`, `marketing-saas-sme`); audit + fix prompts
   inline it so register-scoped craft rules (#19, #24, #25, #41)
   judge against the right scope.

Pre-iter-2 commit: see `git log` for "Pre-iter-2 prep: kill audit-checklist,
slug migration, register threading".

## Review protocol

Follow CLAUDE.md "Iteration discipline" — trace before adding rules. Don't
react to one bad output by inventing a new rule.

### Step 1 — convergence sanity

For each `with_skill/meta.json`:
- Did the loop converge (`converged: true`)? At what `loop_passes`?
- If converged in 1 pass: was the initial draft already clean, or did
  the auditor fail to flag anything?
- If hit MAX_LOOP: what did the last audit cite? Are the cited rules
  genuinely violated, or is the auditor stuck flagging false positives?

### Step 2 — citation quality

Read `pass-N-audit.md` files. The new audit prompt asks for:
- Slug-first citations (e.g., `f4/targhak-closure`, `wrong-classifier`).
- `#NN` only as fallback for unmigrated rules (post-migration: should be
  rare to none).
- Quoted offending text inline.
- Specific particle / connective / pattern named, not just umbrella rule.

Calibrate:
- Citations too generic ("Frame 4 violation") → audit prompt may need
  tightening; sub-pattern slugs are supposed to handle this.
- Citations referencing slugs that don't exist → consistency-test gap or
  prompt-induced hallucination.
- `#NN` heavily preferred over slugs → migration didn't take in the
  prompt; investigate.

### Step 3 — fix quality

Compare `pass-(N-1).md` → `pass-N.md` — does each fix actually address the
cited issue, or is it cosmetic / drift / regression?

### Step 4 — register-scoped behavior

Cross-check craft-rule firing against register:
- `marketing-blurb` is `marketing-saas-sme` → single `!` at hook OK (#19),
  warm reassurance softened-not-banned (#24), no ครับ/ค่ะ in body (#25).
- `tech-doc-short` is `explainer` → no particles, no `!`, problem-first.

If the auditor false-positives across registers, `register.md` scope
notes need sharpening or the prompt isn't conveying register clearly.

### Step 5 — patterns to specifically look for (from PLAN.md, still valid)

- **Person-arity**: `เจ้าของร้าน` → `คุณ` substitution caught and fixed?
- **Seam connectives**: ต่างหาก / โดย / แล้ว / problem→solution pivot
  — cited at sub-pattern granularity, not umbrella?
- **Surface grammar**: classifier (#41), จะ modal (#42), function words
  (#43), verb calque (#44), capability-modal (#46), time-period (#47).
- **Forbidden-phrase use/mention**: blocklist should NOT false-positive
  on backticked occurrences.

### Step 6 — write `feedback.md`

Drop a `workspace/iteration-2/feedback.md`. For each issue traced:

1. Quote the offending output.
2. Map to existing rule (slug + file + line) — was it covered?
3. If covered but didn't fire: why? Audit prompt issue, rule wording
   issue, or rule conflict?
4. If not covered: is this a genuine gap, or a one-off? Check
   `corpus/curated/` for evidence before proposing a new rule.

Don't pile on new rules without trace.

## Decisions gated on iter-2

- **Slug system kept or retired.** If audit citations consistently use
  slugs and they're sharper than `#NN` would have been, the migration
  paid for itself. If the auditor barely uses them or names them
  arbitrarily, reconsider — slug pilot was committed on intuition, not
  evidence.
- **Sub-pattern slug coverage.** Did `f4/targhak-closure`, `f6/ko-resumptive`,
  `f5/demo-bridge` actually surface in audit output? If yes, expand the
  inventory. If never cited, the umbrella Frame slugs alone may suffice.
- **MAX_LOOP=5.** Convergence usually within 2-3 passes? Loosen. Hits the
  cap regularly? Either the prompt is broken or the rules are inconsistent.
- **iter-3 rule deltas** based on traced gaps. Per iteration discipline,
  every new rule needs corpus or scholarly backing — `corpus/curated/`
  is the source of record.

## Files to read first when resuming

In order:

1. This file (`workspace/iteration-2/REVIEW.md`).
2. `git log -1` — confirm prep-work commit landed.
3. `workspace/iteration-2/audit-gaps.md` — full trace of the prep work
   in case any review question reaches back to "why did we do that".
4. One sample `with_skill/output.md` per eval × backend — orient on
   what the loop produced.
5. The corresponding `meta.json` — convergence behavior.
6. The corresponding `pass-1-audit.md` — audit-citation quality.
7. `skills/kien-thai/SKILL.md` — Frame definitions + sub-pattern slugs
   are the rule of record for citations.
8. `tests/generate/conftest.py:_audit_prompt` and `_fix_prompt` — the
   prompts iter-2 actually used.

## Commands cheat-sheet

```sh
rtk uv run pytest                         # sanity + consistency (default)
rtk ls workspace/iteration-2/             # find generated outputs
rtk cat workspace/iteration-2/<eval>/<backend>/with_skill/meta.json
rtk uv run pytest -m generate -k '<eval> and <backend>'   # re-run one cell
```

## Open items deferred from this session

- **Cosmetic stale references** (audit-gaps.md's "Cosmetic / low-priority"
  section): `SKILL.md:52` "Covers anti-patterns #6, #12" wording, `kode-thai
  /SKILL.md:57` generic "kien-thai's rules". Pick up only if a sweep
  happens to land near them.
- **Corpus diversification** — `tech-writing` (somkiat only), `translation`
  (Salforest only). See `corpus/RESUME.md`.
- **Empirical connective baselines** — Thai Discourse Treebank analysis,
  148-connective inventory mining. Separate corpus-analysis tasks.
