---
name: register.md analysis
description: Iter 03 — register-scoped injection is the headline win
slice: skills/kien-thai/references/register.md
---

# 03 — register.md (8,299 tokens)

This file holds the **biggest single cut in the bundle**: register-scoped
injection. Eval cases already carry a `register` field; the harness
already inlines it in audit/fix prompts. But `kien_thai_bundle()` still
ships all 5 registers + 4 marketing sub-registers in every pass.

## Structure

| Section                     | Lines    | ~Tokens | Per-pass need |
| --------------------------- | -------- | ------: | ------------- |
| Header + intro              | 1–10     |     100 | always        |
| Quick register decision     | 12–26    |     230 | pass-0 only   |
| Voice attributes            | 28–41    |     200 | pass-0 only   |
| Person-arity                | 43–64    |     320 | **DUPLICATE of SKILL.md:218–238** |
| Register 1: Explainer       | 66–108   |     680 | only if active |
| Register 2: Marketing fam.  | 110–186  |   1,840 | only if active |
| Register 3: Personal blog   | 188–235  |     900 | only if active |
| Register 4: News/reference  | 237–260  |     400 | only if active |
| Register 5: Academic        | 262–298  |     680 | only if active |
| Cross-register: when shift  | 300–313  |     280 | always        |
| Coherence within passage    | 315–334  |     400 | always        |
| Default if unclear          | 336–340  |      50 | always        |

Total reconciled: ~6,080 register-body + ~1,580 always-needed +
~640 person-arity-dup ≈ 8,300. Matches.

## Concrete cuts

### Cut A — register-scoped injection (the big one)
**All passes.** Eval cases declare register (`evals.json` validated by
`load_evals()`). The audit + fix prompts inline `register` for scoping
craft rules. Pass-0 also receives the register via the same path.

Rebuild `kien_thai_bundle()` to take `register: str` and emit:
- header + intro
- registry index (one-line summary per register, ~30 tok × 9 = ~270 tok)
- the **single active register block** (or multiple if cross-register
  shift declared in eval metadata)
- cross-register shift section + coherence + default

For default case (1 register): bundle drops register-body 6,080 → ~700 tok.

**Per-pass cut: ~5,400 tokens** (every pass). 11 × 5,400 = **~59K
tokens saved on codex tech-doc 5-pass**. Best case (2-pass converge):
4 × 5,400 = 21.6K saved.

Cross-register cases are rare in evals (most are single-register).
Add an optional `register_secondary` field if a piece needs it.

### Cut B — drop person-arity duplication
**All passes.** Lines 43–64 are a verbatim restating of SKILL.md
Person-arity (lines 218–238). Two paths to the same content add zero
information.

- Replace register.md:43–64 with a 2-line pointer:
  `Person-arity (1st brand เรา / 2nd reader คุณ — never demographic
   noun / 3rd product) is defined in SKILL.md and applies in full here.
   Marketing sub-registers below override only the brand-side default.`

Cut: ~180 tokens every pass.

### Cut C — registry index format
A registry index (Cut A's prerequisite) replacing the quick-decision
table needs to be tighter. Current table is 230 tokens for 12 rows;
condensed index can be ~30 tok × 9 = 270 tokens but doubles as the
quick-decision lookup. Net: ~40 token *increase* — accept it as the
price of Cut A.

Actually more compact:
```
Registers: explainer · marketing/{saas-sme,b2b-formal,fintech-warm,retail-tech} ·
personal-blog · news · academic. Pick by output type — see scoping table below.
```
~50 tokens, plus the active block. Keep the table only for the pass-0
draft prompt where register selection happens. Audit/fix passes have
register pre-selected — table is dead weight.

### Cut D — "Models" pointers move to corpus
Each register section ends with `**Models**: <list of source publications>`.
Useful for human-curating new corpus entries; useless for an LLM
auditor that doesn't fetch them. ~25 tok × 5 registers = ~125 tok.

- Move to `corpus/curated/<register>/README.md` (already the corpus
  index pattern).
- Cut: ~125 tokens (every pass, multiplied by however many registers
  are still in the bundle post-Cut-A — typically 1, so net ~25 tokens).

Marginal once Cut A applies; defer until corpus reorganization.

### Cut E — Marketing common-rules dedup
Lines 115–126 ("Common to all Marketing sub-registers") list 5 bullets.
Some content (anti-pattern #19, #24 references) is mentioned again
inside each sub-register. Centralize once.

Cut: ~80 tokens. Applies whenever any marketing sub-register is active.

## Cumulative impact (this slice)

| Cut | Tokens/pass | Notes                  |
| :-: | ----------: | ---------------------- |
|  A  |       5,400 | Every pass, default case |
|  B  |         180 | Every pass             |
|  C  |       (-40) | Cost of Cut A's index  |
|  D  |          25 | Every pass post-A      |
|  E  |          80 | When marketing active  |
| **Σ** | **~5,565 / 5,485** | **66–67% of file** |

For codex tech-doc 5-pass case: ~61K tokens saved. **By far the
largest single-slice win identified so far.**

This single cut, if implemented, justifies the whole loop's existence.

## Risks

- **Cut A — auditor scope awareness**: when the auditor only sees one
  register's rules, can it flag "this isn't the right register for the
  brief"? Yes — the registry index + the eval-supplied register tag
  give it enough context. The audit prompt asks the auditor to apply
  the rules of the *given* register, not to second-guess the choice.
- **Cut A — cross-register shift evals**: some pieces legitimately
  shift register mid-piece (bank explainer with quoted expert,
  marketing with testimonial). The bundle must support 2 registers
  for those cases. Add `eval.register_secondary` and concat both
  blocks. Worst-case bundle size = 2 register blocks ≈ 2.5K tok,
  still ~3K under current.
- **Cut A — implementation complexity**: `kien_thai_bundle()`
  currently no-arg; needs a `register` param threaded through both
  pass-0 (`build_prompt`) and the audit/fix invocations
  (`_audit_prompt`, `_fix_prompt`). Modest refactor in `tests/lib.py`
  + `tests/generate/conftest.py`. Maybe 15 LOC.
- **Cut B — Person-arity in marketing sub-registers**: each sub-register
  block (Marketing/SaaS-SME, /B2B-formal, etc.) has its own
  person-arity wrinkles. Those stay in the sub-register block; only
  the generic 1st/2nd/3rd definitions move out. Verify by re-read.

## Decisions deferred

- Whether to also scope `examples.md` to register (iter 04 will
  examine — likely similar win).
- Whether `craft.md` rules should be split by register (iter 05).
- Cross-register shift API design — `register_secondary` field, or
  a more general `extra_registers: list[str]`?
