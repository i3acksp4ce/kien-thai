# Research queue

Speculative items needing evidence before they can graduate into a rule. Items
here are *questions*, not verdicts. Each entry should name the question, the
hypothesis (if any), the scope of work that would settle it, and where the
finding would land.

---

## ๆ-spacing as register-scoped style

**Question.** Is the spacing convention around ๆ (e.g. `แย่ ๆ` vs `แย่ๆ`)
register-dependent in real Thai writing, or is one form correct everywhere?

**Hypothesis (chakrit's speculation, NOT verdict).** Formal / contributor-doc /
official-leaning prose tracks Royal-Institute spacing (`คำ ๆ`); marketing and
casual prose drop the space (`คำๆ`).

**Scope to investigate.** Tech blog, bank long-form, newspaper รุ่นใหม่,
dev-casual blog, government, academic, marketing copy. Look at how each
register actually handles ๆ; check whether any register is internally
consistent.

**Landing place.** New or amended rule in `references/style-rules.md`, or a
register-scoped slot in `references/register.md`. Not a hard `ai-tells.md`
rule unless the formal-strict form turns out to be universal.

---

## Comma-listing as register/formality feature; formality as a missing axis

**Question (a).** Does Thai-prose comma-listing (e.g. `A, B, หรือ C`) track
register, formality, both, or neither? Is it always wrong, always fine, or
context-dependent?

**Question (b).** Is "formality" a missing or replacement axis to the current
5-register taxonomy in `references/register.md`? Right now register is one
flat axis; formality may cut across it (a `personal-blog` post can be casual
or formal independently of the register family).

**Method.** Survey the curated corpus in `corpus/curated/` across families.
Tabulate comma-listing density by family. Tabulate formality cues
independently and check whether they co-vary or are orthogonal to register.

**Landing place.** New dimension in `references/register.md` (feature-by-
register matrix), or a separate formality axis layered on top of the
existing register taxonomy.
