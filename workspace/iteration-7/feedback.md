# Iteration 7 — feedback and rule-candidate trace

Iteration 7 produced 12 outputs (3 evals × 2 backends × 2 configs) under
the same skill bundle as iteration-6 — no skill edits between iter-6 and
iter-7. The intent was to capture `news-feature-bts` (new register) for
the first time and a fresh comparison set on the other two evals.

Harness note: `pytest -m generate -n 4` split the 12 outputs across
`iteration-7/` and `iteration-8/` (6 each) because `iteration_dir` is a
session-scoped fixture and xdist gives each worker its own session.
Manually consolidated post-run. Bug logged in `notes/work-queue.md`.

Review status: only `tech-doc-short/claude/with_skill` and
`marketing-blurb/claude/with_skill` reviewed in this session. The other
ten outputs (codex backends, baselines, news-feature-bts both backends)
remain unreviewed and are candidates for a follow-up pass.

## Patterns observed

### tech-doc-short (claude/with_skill)

- **Personification verb on system subject** — `downstream ทนรับ burst
  ได้แค่ไหน`. `ทน` (endure) requires an animate subject; `downstream` is
  not human. Native fix: `downstream รองรับ burst ได้แค่ไหน`. `ทน` reads
  organic on humans, wrong on systems.
- **Idiom mis-selection** — `Leaky bucket มองกลับด้าน` ("the other way
  around"). Native preference: `มองกลับกัน` (more idiomatic Thai for
  "viewed inversely / mirrored"). Borderline — may be lexical preference
  rather than rule.

### marketing-blurb (claude/with_skill)

- **Cognitive-vs-affective verb collocation** — `ตัวเลขไม่ตรงกับที่
  รู้สึก`. Quantitative subject + affective verb = wrong register. Fix:
  `ตัวเลขไม่เคยตรงกับที่คาดสักที` (cognitive verb + per-instance closure
  for `ทีไร` frame). Two errors stacked: verb choice + missing frame
  closure.
- **`ทีไร` frame closure missing** — bare `แต่พอ … ทีไร X` endings do
  not parse as complete. Frame requires per-instance closure on the
  right clause: `ทุกที` (positive, safest), `ไม่เคย…สักที` / `…เลย`
  (negative). `ทุกครั้ง` is a soft drift toward `เสมอ`-class.
- **Person-deixis discontinuity** — `แต่ไม่มีใครรู้` introduced
  third-party `ใคร` into an implicit-2nd-person passage (lines 1–6 run
  zero-deixis; `คุณ` only appears at L7). Native fix: `โดยไม่รู้ตัว`
  keeps the implicit-2nd-person frame intact.
- **Hedge-stack collapse needed** — `น่าจะขาดทุนอยู่ด้วยซ้ำ`
  (modal + progressive + emphatic stack) reads timid. Marketing register
  wants assertion: `กลายเป็นขาดทุน`. AI default in marketing is to pile
  hedges; native voice asserts.
- **Loose afterthought tail → modifier** — same line, `แต่ไม่มีใครรู้`
  promoted to `โดยไม่รู้ตัว`. Surface restructure; the underlying rule is
  person-deixis continuity (above).
- **`มา` insertion for intentional come-and-do** — `นั่งคิด` →
  `มานั่งคิด`. The `มา` adds a temporal/intentional shading absent in
  the bare form. May be a recurring marketing-register polish move or a
  one-off — needs more examples.
- **Constitutive-vs-causal `ก็` mis-placement** — `ราคาวัตถุดิบขยับ
  เมื่อไหร่ ต้นทุนต่อจาน**ก็**ขยับตาม`. `ก็` marks consequence in causal
  pairs (rain→wet). Fails here because cost↔ingredient-prices is a
  *constitutive* relationship — cost *is* ingredient prices summed, not
  *caused by* them. Native rewrite drops `ก็`:
  `ต้นทุนต่อจานขยับตามทันที`, with `ทันที` closing the `เมื่อไหร่`
  frame. The third clause `คุณจะเห็นกำไรที่แท้จริงของเมนูเสมอ` is a
  separate future-promise frame with its own `จะ…เสมอ` binding.
- **Marketing-promise structure** — `กำไรที่แท้จริง…เสมอ` carries the
  actual value-prop (truth-guarantee), not the speed (`ทันที`). Adjective
  intensification + universal-aspect is the natural shape for the
  promise. AI tends to lead with the feature; native marketing leads
  with the universal guarantee.

## Rule candidates surfaced

Tracking each candidate's provenance, formulation, landing target, and
confidence. Some need corpus evidence before encoding.

| Candidate                                                | Provenance                          | Landing                              | Confidence       |
| -------------------------------------------------------- | ----------------------------------- | ------------------------------------ | ---------------- |
| R-a: quantitative subjects take cognitive verbs (`คาด`/`คิด`/`หวัง`), not affective (`รู้สึก`); `ตรง` not `ซ้ำ` for match | marketing-blurb L3 + dashboard ex.  | `grammar.md` collocations slot       | High — clean trace |
| R-b spine: `ทีไร` requires per-instance closure on right clause; safest closures `ทุกที`, `ไม่เคย…สักที / เลย` | marketing-blurb L3 + extended thread | `grammar.md` paired-constructions    | High             |
| R-b idiomatic edges: `เสมอ` + `ทีไร` partially attested; bounded-to-trigger hypothesis captures *some* cases | extended thread, four test rows     | `examples.md` tagged collection      | Low — idiomatic  |
| R-b linker: `ก็` redundant with `ทีไร`; `ก็จะ` required with `ไม่ว่าจะ…เมื่อไหร่` (frame-scoped) | extended thread                     | `grammar.md` paired-constructions    | High             |
| `ทีไร` ≠ `(ไม่ว่าจะ)…เมื่อไหร่`: distinct frames, English "whenever" trap | extended thread                     | `ai-tells.md` calque-trap entry      | High             |
| Person-deixis continuity: once deixis (incl. zero/implicit) is established, holds across the passage | marketing-blurb L4–5                | `register.md` person-deixis section  | High             |
| Hedge-stack collapse in marketing register: `น่าจะ X อยู่ด้วยซ้ำ` → `กลายเป็น X` | marketing-blurb L4                  | `register.md` marketing-saas-sme     | Medium — one example |
| Constitutive-vs-causal `ก็` placement: causal pairs only; constitutive pairs use bare or `จะ` | marketing-blurb L11                 | `grammar.md` linker rules            | Medium — one example |
| Personification verbs on system subjects: `ทน` requires animate subject | tech-doc-short                      | `grammar.md` or `ai-tells.md`        | Medium — one example, may generalize |
| Marketing promise structure: adjective intensification + universal aspect carries the value-prop | marketing-blurb L11                 | `register.md` marketing-saas-sme     | Low — needs more examples |
| Closer-binding scope discipline (process note, not prose rule) | extended thread, variant E read     | `SKILL.md` review workflow or `kode-thai/SKILL.md` | Process |

## Trace per CLAUDE.md iteration discipline

For each pattern, check existing rules before adding new ones.

| Pattern                                | Existing rule                          | Status                               | Action                                                          |
| -------------------------------------- | -------------------------------------- | ------------------------------------ | --------------------------------------------------------------- |
| Wrong verb-object collocation (ตัวเลข + รู้สึก) | None directly                         | New gap                              | Propose `grammar.md` collocations slot covering quantitative-subject + verb constraints |
| `ทีไร` frame requires closure          | None directly                          | New gap                              | Propose `grammar.md` paired-constructions section; structural rule only |
| `ทีไร` + `เสมอ` edge cases             | None                                   | Idiomatic — resist universal rule    | Propose `examples.md` tagged collection of attested pairings    |
| `ก็` frame-scoped (`ทีไร` vs `ไม่ว่าจะ…เมื่อไหร่`) | None                              | New gap                              | Propose `grammar.md` linker rule with both frames               |
| English "whenever" calque (`ทีไร` vs `เมื่อไหร่`) | `ai-tells.md` covers some calques    | Adjacent; not specific               | Propose `ai-tells.md` entry for this specific mapping           |
| Person-deixis discontinuity            | `SKILL.md` + `register.md` cover which deixis, not continuity | Continuity gap | Propose addition to `register.md` person-deixis section         |
| Hedge-stack in marketing               | `register.md` marketing covers tone, not hedge collapse | Not directly covered | Defer until 2+ examples (one-instance evidence)              |
| Constitutive `ก็` mis-placement        | None                                   | New gap                              | Defer until 2+ examples                                         |
| Personification verbs on systems       | None                                   | New gap                              | Defer until 2+ examples                                         |
| Marketing promise structure (adj-intensification + universal aspect) | None                | New gap                              | Defer until 2+ examples                                         |

## Judgements logged

Three judgements from this session, in `notes/judgements/`:

- [`2026-05-11-cognitive-vs-affective-verbs.md`](../../notes/judgements/2026-05-11-cognitive-vs-affective-verbs.md)
- [`2026-05-11-frame-rules-have-idiomatic-edges.md`](../../notes/judgements/2026-05-11-frame-rules-have-idiomatic-edges.md)
- [`2026-05-11-person-deixis-discourse-over-syntax.md`](../../notes/judgements/2026-05-11-person-deixis-discourse-over-syntax.md)

A fourth call (Claude treating workspace outputs as editable artifacts) was
diagnosed as a context defect rather than a prose-judgement override —
the fix is in project `CLAUDE.md` (Iteration discipline → "Workspace
outputs are evidence, not artifacts"), not a retrospective judgement.

## Followups

- Review the remaining 10 outputs (codex backends, baselines, news-feature-bts
  both backends) — un-reviewed in iter-7 session.
- Resolve the xdist iteration-dir split before the next `-n N` generation
  run (see `notes/work-queue.md`).

## Done

- Rule candidates marked "Action: Propose" — landed in `grammar.md`
  (`quant-subject-cog-verb`, `tirai-frame-closure`, `frame-scoped-ko`),
  `ai-tells.md` (`whenever-calque`), `register.md` (deixis-continuity
  block).
- L3, L4–5, L11 before/after pairs lifted into `references/examples.md`
  as Examples 6–8 (register-tagged marketing-saas-sme).
