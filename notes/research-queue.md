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

---

## Hedge-stack pattern beyond `น่าจะ X อยู่ด้วยซ้ำ`

**Question.** Does the broader multi-particle hedge-stack pattern in
marketing-register body copy generalize beyond the one stack shape now
captured in `over-hedging`?

**Hypothesis.** AI defaults to hedge-stacking in marketing register
because the training data conflates "warmth" with "softening." Native
marketing copy asserts (`กลายเป็นขาดทุน`) and reserves hedging for
disclaimer-adjacent lines, not body-pain-point claims.

**Status so far.** The `น่าจะ X อยู่ด้วยซ้ำ` instance from iter-7
marketing-blurb L4 landed in `ai-tells.md#over-hedging` as the marketing
example. The general "does multi-particle stacking in pain-point copy
generalize?" question is still unanswered.

**Scope to investigate.** Look at iteration-1 through iteration-7
marketing outputs for other instances of multi-particle hedge stacks
(`อาจจะ … คงจะ … น่าจะ …`, `อาจ … อยู่ … บ้าง …`, etc.) in body copy
making a pain-point claim. If the pattern is recurring with different
stack shapes, promote `over-hedging` to a register-aware rule (or split
into a marketing-specific entry in `register.md`).

**Landing place.** Extend `ai-tells.md#over-hedging` with more attested
stack shapes, or new `register.md` marketing entry specifically about
pain-point assertion vs hedging.

---

## Personification verbs on inanimate / system subjects

**Question.** Is `ทน` the only personification verb AI mis-applies to
non-human subjects, or part of a broader class? Candidate verbs:
`ทรมาน`, `เหน็ดเหนื่อย`, `อดทน`, `เครียด`, `สบาย`, `กล้า`, `รู้`.

**Hypothesis.** AI applies a wider set of human-only or animate-only
verbs to systems/abstractions because English freely personifies
("the system *suffers* under load," "the server *gets tired*"). Thai
constrains animacy more tightly.

**Provenance so far.** One instance — iteration-7 tech-doc-short
(claude/with_skill): `downstream ทนรับ burst ได้แค่ไหน`. Chakrit's
rewrite: `downstream รองรับ burst`.

**Scope to investigate.** Look at tech-doc and explainer outputs from
iterations 1–7 for verbs marked as requiring animate subjects but
applied to system-state subjects. Cross-check against a list of Thai
animacy-restricted verbs.

**Landing place.** `grammar.md` new entry "animacy-restricted verbs," or
folded into `ai-tells.md` as a calque-pattern entry. If only a handful
of verbs are involved, an explicit list works; if it's open-ended, a
heuristic rule may be needed.

---

## Closer-binding scope reading discipline

**Question.** Where does the "read closure-binding scope before judging
pair-compatibility" discipline belong? It's a review-process rule, not a
prose-content rule.

**Hypothesis.** Belongs in `skills/kien-thai/SKILL.md` review workflow
(applies to both generation-time self-review and audit-pass) rather than
`skills/kode-thai/SKILL.md` (audit-loop only). Generation-time
self-review benefits equally from getting binding scope right before
calling a pair incompatible.

**Provenance so far.** One instance — iteration-7 marketing-blurb L11
variant E reading: Claude misparsed `เมื่อไหร่ + เสมอ` as a direct pair
when `ทันที` had already closed `เมื่อไหร่` and `เสมอ` belonged to a
separate `จะ…เสมอ` frame.

**Scope to investigate.** See whether other audit-pass misreads in
iter-7 outputs (across the un-reviewed remaining 10) involve similar
binding-scope errors. If yes, the discipline lands in the audit-loop
side; if also at generation time, it lands in the kien-thai workflow.

**Landing place.** TBD between `skills/kien-thai/SKILL.md` workflow
section, `skills/kode-thai/SKILL.md` audit pass, or a new checklist
file under `skills/`. Pick after seeing more instances.
