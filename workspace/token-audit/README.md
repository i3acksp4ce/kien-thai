---
name: token-audit index
description: Index for the token-efficiency audit; entry point for review or implementation
---

# Token-efficiency audit — index

Self-paced analysis loop on bundle + harness token cost. Goal:
identify concrete optimizations to make kien-thai/kode-thai much more
token-efficient at runtime and at development time.

**Scope**: analysis only. No skill content edited. Implementation
ordered separately in `08-synthesis.md`.

## Files

| #  | File                          | Slice                              |
| -: | ----------------------------- | ---------------------------------- |
| 00 | [00-cost-map.md](./00-cost-map.md) | Repo-wide token survey + plan |
| 01 | [01-skill-md.md](./01-skill-md.md) | SKILL.md (~30% cut)           |
| 02 | [02-ai-tells.md](./02-ai-tells.md) | ai-tells.md (~8% cut)         |
| 03 | [03-register.md](./03-register.md) | register.md → register-scoped (~67%) |
| 04 | [04-examples.md](./04-examples.md) | examples.md → register-scoped (~81%) |
| 05 | [05-style-and-craft.md](./05-style-and-craft.md) | style + craft + numbering bug |
| 06 | [06-grammar-forbidden-anti.md](./06-grammar-forbidden-anti.md) | small files + anti-patterns dead-weight |
| 07 | [07-prompts-and-caching.md](./07-prompts-and-caching.md) | prompt template + cache strategy |
| 08 | [08-synthesis.md](./08-synthesis.md) | totals + implementation roadmap |

## Headline numbers

Codex tech-doc 5-pass case (worst observed in iter-3 eval run):

- Today: ~470K input tokens.
- After Stage 1 (quick wins): ~404K. **14% off.**
- After Stage 2 (register scoping): ~311K. **34% off.**
- After Stage 3 (prompt caching): ~241K (estimated). **49% off.**
- After Stage 4 (two-tier injection): ~70K (estimated). **85% off.**

## Cleanest single cuts (no risk)

1. **Exclude anti-patterns.md from bundle** (iter 06 Cut D). 537 tok
   per pass, pure stub redirector. ~15 min implementation.
2. **Drop frontmatter description from injection** (iter 01 Cut D).
   370 tok per pass, runtime-irrelevant skill discovery info.
3. **Move citation provenance out of prompt path** (iter 01 Cut C).
   200 tok per pass, scholarly cites useful only to humans.

These three together: ~1,100 tok/pass, ~12K saved on a 5-pass codex
failure case, with **zero behavior risk**. Implement first.

## Headline architectural change

**Register-scoping the bundle** (iters 03 + 04). Eval cases already
declare register; the harness already inlines it. `kien_thai_bundle()`
should take a register param and emit only the active register's
content from register.md and examples.md. ~8,500 tok cut every pass,
~93K saved on the 5-pass case.

Implementation: ~3 hours, 15 LOC of plumbing in tests/lib.py +
tests/generate/conftest.py. Single biggest leverage point identified.

## Bugs surfaced (not token-related but worth fixing during sweep)

- **Dead audit-checklist.md refs** in SKILL.md:352–353 and
  ai-tells.md:12 — file was deleted in iter-2 prep.
- **Numbering collision** between style-rules.md and craft.md (#17–
  #21 mean different things). Slug-first citations paper over it
  but `#NN` fallback is ambiguous. Recommend dropping `#NN` since
  slug coverage is complete.
- **Mislabeled register** on examples.md Example 2 — labeled
  Explainer but conventions are clearly Marketing/SaaS-SME.

## When this audit was run

Pre-implementation; the iter-3 eval review (per
`workspace/iteration-3/RESUME.md`) has not happened yet. **Do not
implement these cuts until iter-3 review establishes a baseline** —
implementing token cuts on top of unreviewed eval data risks
conflating token-efficiency wins with rule-content shifts.

## What was NOT analyzed

- **Eval quality vs token cost trade-offs** — needs eval data, not
  analysis.
- **kode-thai SKILL.md** as a standalone human-invoked skill (only
  the eval-harness path through it).
- **pythainlp word_tokenize** runtime cost (not a token-cost issue).
- **Workspace artifacts** (prompt files, audit traces) — disk only.
