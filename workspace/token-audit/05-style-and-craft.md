---
name: style-rules + craft
description: Iter 05 — confirms iter 01 Cut F, surfaces a numbering collision
slice: skills/kien-thai/references/style-rules.md + craft.md
---

# 05 — style-rules.md + craft.md (5,493 + 2,722 tok)

Two files, both rule lists. style-rules is "positive style rules" /
draft-time advice; craft is "voice / taste preferences" / soft rules.

Confirms iter 01 Cut F: SKILL.md "Stylistic conventions" lines
240–265 duplicate ~6 rules already in style-rules.md.

Also surfaces a **numbering collision** between the two files (#17
through #21 mean different things in each — slug system mostly papers
over this for the auditor, but human-facing it's a footgun).

## style-rules.md structure

| Section                    | Rules        | ~Tokens |
| -------------------------- | -----------  | ------: |
| Header + intro             | --           |     50  |
| Sentence shape and rhythm  | 1–8          |   1,300 |
| Verbs and nouns            | 9–11         |     400 |
| Openers and closings       | 12–16        |     650 |
| Concreteness               | 17–20        |     500 |
| Voice and personality      | 21–25        |     680 |
| ทับศัพท์ four-bucket guide  | --           |   1,200 |
| Translation craft          | 26–32        |   1,000 |
| Structure                  | 33–35        |     400 |

## craft.md structure

| Section                | Rules            | ~Tokens |
| ---------------------- | ---------------- | ------: |
| Header + intro         | --               |     180 |
| Headlines and openers  | 17, 45           |     400 |
| Closings               | 18, 19           |     580 |
| Intensifiers and lists | 20, 21, 24       |     680 |
| Sentence-level shape   | 33, 34, 35       |     250 |

## Concrete cuts

### Cut A — SKILL.md "Stylistic conventions" dedup (iter 01 Cut F)
**All passes.** SKILL.md:240–265 = 6 numbered conventions:

1. Verbs over noun forms ↔ style-rules #9 (verbatim concept)
2. Particles match register ↔ style-rules #25 (overlapping)
3. Open with reader's situation ↔ style-rules #12
4. Concrete numbers ↔ style-rules #17
5. Vary sentence length ↔ style-rules #1 + craft #33
6. Mai-yamok ๆ ↔ style-rules #7

Replace SKILL.md:240–265 with a one-line pointer:
```
## Stylistic conventions (apply on top of the frames)

Positive style rules in `references/style-rules.md` § Sentence shape /
Verbs and nouns / Voice and personality. Soft taste-preferences in
`references/craft.md`.
```

Cut: ~520 tokens off SKILL.md every pass. Codex tech-doc 5-pass:
~5,720 tokens.

### Cut B — Treebank citation in style-rules #2
**All passes.** Lines 21–26 spend ~120 tokens explaining that the
100-word connective budget is "observation-calibrated" and pointing at
the Thai Discourse Treebank for re-calibration. Useful project-context;
useless to the auditor applying the rule today.

Move to `corpus/curated/scholarly/thai-discourse-treebank.md` (or a
`PROVENANCE.md` at skill root) alongside the iter 01 Cut C
provenance moves.

Cut: ~120 tokens every pass.

### Cut C — Marcel Barang prose in #31
**All passes.** Lines 204–211 are 80 tokens of "Per Marcel Barang on
Thai literary translation: no added editorial commentary, no cultural
framing..." — motivational prose around the actual rule. Keep the
rule, trim the cite.

Replacement (~30 tokens):
```
31. **Don't add anything the source doesn't have.** No added ครับ/ค่ะ
on confident essayists. No hedging อาจจะ where the source asserts.
If the source omits a transition, omit it. Fidelity to voice, not
tour-guiding.
```

Cut: ~50 tokens every pass.

### Cut D — fix numbering collision
**Correctness, not tokens.** Both files use #17–#21 with different
content:

| #  | style-rules.md                    | craft.md                       |
| -: | --------------------------------- | ------------------------------ |
| 17 | Numbers and named examples        | Cliché headlines               |
| 18 | Uneven, specific lists            | โดยสรุป + recap                 |
| 19 | ยิ่ง X เท่าไหร่ ยิ่ง Y                  | Imperative product CTAs (`!`)  |
| 20 | นี่คือเหตุผลที่...                   | Empty intensifiers             |
| 21 | First-person ผม                    | Symmetric tricolons            |

Slug system papers over this for auditor citations (post-iter-2
migration uses slugs as primary), but `#NN` fallback is ambiguous.

Two options:
1. **Renumber craft.md** rules to a non-overlapping range (e.g.,
   100–149 for craft).
2. **Drop `#NN` fallback entirely** since slug migration is complete.
   Eliminates the ambiguity.

Recommend (2) — slugs are the rule of record; numbering should be
purely human-readable. Audit prompt already prefers slugs.

Token impact: 0. Quality impact: better citation precision.

### Cut E — craft.md scope-soft note dedup
**All passes.** Each scope-conditional craft rule (#19, #24) declares
its scope twice — once in metadata line, once in body prose:

```
`cta-bang` · craft · scoped · soft

- Bad: ...
- Good: ...

**Scope**: full strictness in Explainer, Marketing/B2B-formal, ...
**Softened in Marketing/SaaS-SME** — single `!` at hook is fine ...
```

The metadata line says `scoped`; the **Scope** block then enumerates
the conditional. Compress — drop the `scoped` keyword (uninformative)
and let the **Scope** block carry the detail.

Cut: ~30 tokens × 2 rules = 60 tokens every pass.

### Cut F (deferred) — merge ai-tells / craft / grammar into one rules.md
**Not recommended for this pass.** Compresses 4 file-level frontmatter
intros (~600 tok), but loses the type/severity routing the auditor
prompt currently relies on. If a future eval shows the auditor
benefits from rule-list flatness, revisit.

## Cumulative impact (this slice)

| Cut | Tokens/pass | Notes                  |
| :-: | ----------: | ---------------------- |
|  A  |         520 | Every pass (SKILL.md)  |
|  B  |         120 | Every pass             |
|  C  |          50 | Every pass             |
|  D  |           0 | Correctness only       |
|  E  |          60 | Every pass             |
| **Σ** |     **750** |                        |

Codex tech-doc 5-pass: ~8,250 tokens saved. Modest single-slice; A is
the bulk and is already counted under iter 01 deferred — net **new**
contribution from iter 05 is ~230 tok/pass after deduplication.

## Risks

- **Cut A**: SKILL.md is read first; the auditor may use the convention
  list to anchor before getting to references. Mitigation: the pointer
  preserves the headings and points to specific style-rules sections.
- **Cut D (renumber/drop #NN)**: requires sweep across all rule files
  and the audit prompt template to ensure no #NN-only references
  remain. Low effort, high signal — do it.

## Decisions deferred

- Whether craft.md's "scoped" keyword in metadata is worth preserving
  for tooling (e.g., a future linter that warns when a scoped rule
  fires outside its register). Cut E drops it; if tooling lands later,
  re-introduce.
- File-merge experiment (Cut F) — only if eval data motivates.
