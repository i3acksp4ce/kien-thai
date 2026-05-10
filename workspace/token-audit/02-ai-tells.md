---
name: ai-tells.md analysis
description: Iter 02 — rule-density audit of ai-tells.md
slice: skills/kien-thai/references/ai-tells.md
---

# 02 — ai-tells.md (7,928 tokens, 29 rules)

Already tighter than SKILL.md. Most cuts here are mechanical (dead refs,
redundant metadata) rather than structural. ~10% baseline reduction; up
to ~30% if we accept a format reflow that requires eval validation.

## Structure today

```
# AI tells in Thai prose (mechanical)
<intro paragraph, 3 lines>
<companion files: 3 entries, includes DEAD audit-checklist.md>
<frame cross-reference: F1–F7 list, duplicates SKILL.md>
<note about register-mechanical rules>
<note about 90-col exemption for inline Thai>

## <Group heading 1> *(F-tags)*
### N. <Rule name>
`slug` · mechanical · all-registers · hard
<explanation prose>
- **Bad**: ...
- **Good**: ...
<optional notes>

(repeat × 29 rules across ~7 groups)
```

29 rules numbered (gaps: #11, #17–21, #24, #33–35 missing — old slots)
across groups: connectives, passive/agency, nominalization,
panorama openers, padding, pronouns/politeness, punctuation, closure.

## Concrete cuts

### Cut A — drop dead audit-checklist ref + duplicated frame list
Lines 7–22 contain:
- 3 companion-file entries (one is dead `audit-checklist.md`).
- 7-line frame summary identical to SKILL.md:33–36 + Frames 1–7 headings.
- Notes about register-mechanical rules and 90-col Thai exemption.

The frame list duplicates SKILL.md, which is *always* injected before
this file. The auditor doesn't need both. Companion-files block is
agent-routing info; auditor already has the bundle.

Replace with one line:
```
Mechanical Thai-correctness rules. Cross-references to Frames F1–F7
in SKILL.md. Register-conditional rules tagged `· register`.
```

Cut: ~180 tokens (every pass).

### Cut B — drop default metadata flags
Every rule has `· mechanical · all-registers · hard`. By being in
ai-tells.md, all are mechanical (the file's name). Most are
all-registers. Almost all are hard.

Convention: print only **non-default** values. Default values:
- type: `mechanical` (always — drop entirely)
- scope: `all-registers` (drop; only print when scope is `register`)
- severity: `hard` (drop; only print `soft` when soft)

Per-rule line drops from `\`slug\` · mechanical · all-registers · hard`
to just `\`slug\``.

Approx 29 rules × ~10 tokens saved = **~290 tokens** cut every pass.

The two `· register` tagged rules (#25 ครับ/ค่ะ, #27 first-person)
keep their scope tag.

### Cut C — trim Prasithrathsint inline note in #6
Lines 96–104 spend 80 tokens on the โดน/ถูก register split with cite.
The auditor doesn't need the cite to apply the rule; the corpus has
the full version.

Replace 8 lines with 2:
```
- โดน: strongly adversative, colloquial (โดนแฮก, โดนปฏิเสธ).
- ถูก: neutral-mild adversative, formal (ถูกประเมิน, ถูกตรวจสอบ).
```

Cut: ~60 tokens.

### Cut D — merge near-duplicate examples
Several rules have 2 example pairs making the same point. Where the
second pair adds no new pattern, drop it. Audit candidates:

- #6 lines 109–110 — "หนังสือเล่มนี้ถูกเขียน" — distinct from
  data-flow example, **keep**.
- #10 lines 147–148 — second `มีความ` pair on `ภาษาสำคัญ`. First pair
  on `โค้ดซับซ้อน` makes the rule clear. **Drop second pair.** ~40 tok.
- #15 lines 209–212 — 4 "Good" examples for panorama-opener. The
  variety (war-story / news / explainer / question hook) maps to
  registers. **Keep all four** — register-discriminating.
- #28 lines 270–274 — explanation paragraph longer than the rule
  warrants. Compress 4 lines to 1: "Drop pronouns when topic carries;
  fire only on translation-shape repetition." ~40 tok.

Total ~80 tokens saved.

### Cut E — section header tags `*(F6, F7)*` redundancy
Group headings like `## Connectives and transitions  *(F6, F7)*`
duplicate the F-tag info present per-rule. Plus the frame list
already lives in SKILL.md.

These are cheap (~5 tokens each × ~7 groups = ~35 tokens) and aid
human navigation. **Marginal — keep.** Token impact too small to
justify human-readability cost.

## Cumulative impact (this slice)

| Cut | Tokens/pass | Net effect            |
| :-: | ----------: | --------------------- |
|  A  |         180 | every pass            |
|  B  |         290 | every pass            |
|  C  |          60 | every pass            |
|  D  |          80 | every pass            |
|  E  |       skip  | low value             |
| **Σ** | **~610** | **every pass**        |

ai-tells.md drops from 7,928 → ~7,320 tokens (~8%). Codex tech-doc
5-pass case: 11 × 610 = ~6,700 tokens.

## Format-reflow experiment (deferred — requires eval)

Beyond the conservative cuts, a more aggressive reformat could land
~30% on this file. Each rule's explanation prose ("AI uses ซึ่ง to
glue every dependent clause. Native writers use a period or
restructure.") repeats what the Bad/Good pair already shows.

Compressed format:
```
### 1 · ซึ่ง-stacking `chueung-stacking` · F6
Bad:  Kubernetes เป็นระบบจัดการคอนเทนเนอร์ ซึ่ง...ซึ่ง...ซึ่ง...
Good: Kubernetes เป็นระบบจัดการคอนเทนเนอร์ของ Google เป็นโอเพนซอร์สและมีคนใช้เยอะมาก
Cap: ≤1 ซึ่ง/sentence. Prefer ที่ for concrete antecedents.
```

Estimated cut: ~2,500 tokens (~30% of file). **Risk: auditor may stop
firing the rule when the explanation that primes it is gone.** This is
a behavioral question, not a token question. Validate by running one
eval cell with the reflowed file and comparing audit citations.

Mark as **iter-N follow-up post-eval**, not part of conservative wave.

## Risks

- Cut B (drop default metadata): the consistency test
  (`tests/test_skill_consistency.py`) may parse those tags. Verify
  the parser before dropping. Likely tolerant; if not, update parser.
- Cut C (Prasithrathsint trim): provenance lives in
  `corpus/curated/scholarly/prasithrathsint.md` per SKILL.md
  citation paragraph. Doesn't lose information.

## Decisions deferred

- Format reflow (above) — needs A/B eval.
- Whether to renumber the rules (gaps look untidy) — pure cosmetic,
  zero token effect, skip during efficiency pass.
