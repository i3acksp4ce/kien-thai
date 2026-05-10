---
name: examples.md analysis
description: Iter 04 — register-scope the worked examples too
slice: skills/kien-thai/references/examples.md
---

# 04 — examples.md (3,865 tokens, 5 examples)

Same architectural lever as register.md. Each example targets one
register; only the active register's example earns its keep on a
given run. Register-scoping the examples stacks cleanly with Cut A
from iter 03.

## Structure

5 examples × ~700–800 tokens each:

| # | Register      | Lines     | ~Tokens |
| - | ------------- | --------- | ------: |
| 1 | Explainer     | 9–27      |     680 |
| 2 | Marketing/SaaS-SME (mislabeled "Explainer" line 18) | 29–57 | 870 |
| 3 | Academic      | 59–91     |     780 |
| 4 | Personal blog | 93–114    |     590 |
| 5 | News          | 116–137   |     740 |
| - | Header + meta | 1–8       |      85 |
| - | (rounding)    |           |     120 |

Total ~3,865. Matches.

Per-example structure: Before (AI-Thai) → Tells (what's wrong) → After
(crafted) → Fixes (what changed). All four pieces earn their keep —
Tells primes the auditor, Fixes primes the fixer.

## Concrete cuts

### Cut A — register-scope examples (stacks with iter 03)
**All passes.** When the bundle is register-scoped (iter 03 Cut A), only
include the matching example. Single-register evals: 1 of 5 examples
ships, ~3,100 tokens dropped.

For the codex tech-doc 5-pass case: 11 × 3,100 = ~34K tokens saved
(stacks on top of iter 03's register cut).

Implementation: walk `examples.md` once at load time, parse each
`## Example N: <title>` heading and tag it with a register frontmatter
or matcher comment, then filter at bundle time.

Cleaner alternative: split into per-register files —
`examples/explainer.md`, `examples/marketing-saas-sme.md`, etc., and
have `kien_thai_bundle()` pick the matching file. Avoids re-parsing.

### Cut B — fix mislabeled register on Example 2
Lines 18 and 39 both say "After (Explainer register)" but Example 2
is for SaaS marketing (SMB owners) — the "After" output uses
demographic noun `เจ้าของร้าน` / first-person plural `เรา` /
`ลองใช้ฟรี 30 วัน` CTA / bullet list — clearly Marketing/SaaS-SME, not
Explainer. The label is wrong (not a token issue but a correctness
issue surfaced during audit).

Cut: 0 tokens, but **fix during the implementation phase** to keep
register-scoping correct (Cut A would route this example to the wrong
bucket).

### Cut C — Thai header note
Lines 6–7 ("ข้อความไทยยาว ๆ ใน blockquote ถือเป็นชิ้นเดียวที่แตะไม่ได้
ความยาวเกิน 90 column ก็ปล่อยให้เกินไป") is markdown-style guidance for
human authors editing the file. LLM doesn't need it.

Cut: ~50 tokens. Move to a top-level comment in the file.

### Cut D — Tells/Fixes notes density
The prose after each example block (e.g., line 24–27 Fixes for
Example 1) averages 50–80 tokens each. Useful for auditor priming,
not redundant. **Keep.**

If aggressive: the Fixes prose for the active example is a clear win;
for examples in *other* registers, even if shipped, this prose is
collateral. Cut A handles that — once examples are scoped, all the
remaining prose serves the active register.

## Cumulative impact (this slice)

| Cut | Tokens/pass | Notes                  |
| :-: | ----------: | ---------------------- |
|  A  |       3,100 | Stacks with iter 03 A  |
|  B  |           0 | Correctness fix        |
|  C  |          50 | Every pass             |
| **Σ** | **~3,150** | **~81% of file when scoped** |

Codex tech-doc 5-pass: ~34K tokens saved (additive to iter 03).

## Combined iter 03 + iter 04 (register scoping)

This is where the architecture starts paying off seriously:

| File                  | Before (always) | After (scoped) | Savings/pass |
| --------------------- | --------------: | -------------: | -----------: |
| register.md           |           8,299 |          2,899 |        5,400 |
| examples.md           |           3,865 |            765 |        3,100 |
| **Combined**          |     **12,164**  |      **3,664** |    **8,500** |

For codex tech-doc 5-pass: 11 × 8,500 = **~93K tokens saved** by
register-scoping these two files alone. ~20% of the worst-case bundle
cost.

## Risks

- **Cut A — example breadth**: an auditor catches patterns by
  comparison. Showing only Explainer examples may make it less alert
  to (say) marketing-shaped tells in an Explainer eval. Mitigation:
  the rules in ai-tells.md / craft.md / grammar.md continue to ship
  in full; only the worked examples get scoped.
- **Cut A — cross-register evals**: same as iter 03; if the eval
  declares secondary register, ship both example sets.

## Decisions deferred

- Per-register file split vs. tag-and-filter — pick during
  implementation. Tag-and-filter avoids restructuring; file split
  is easier to maintain long-term.
- Whether examples.md should hold *additional* examples per register
  (currently 1 each) once scoping makes it cheap. Future work — once
  examples are scoped, growing the inventory has marginal cost,
  potentially improving auditor sharpness.
