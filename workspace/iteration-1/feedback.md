# Iteration 1 — feedback and restructure trace

Iteration 1 produced 8 outputs (2 evals × 2 backends × 2 configs) with kien-thai
single-shot prompt-prepend. Human review surfaced patterns that drove a structural
restructure rather than rule-by-rule patches.

## Patterns observed

### marketing-blurb (claude/with_skill)

- 3rd-person address — body uses `เจ้าของร้าน` (demographic noun) where `คุณ` belongs.
- Curt CTA stack — `ลองใช้ฟรี 30 วัน ไม่ต้องผูกบัตร เลิกเมื่อไหร่ก็ได้` reads as
  bullet-list cadence with no closure beat.
- Contrastive correction missing close — `ปัญหาส่วนใหญ่ไม่ได้อยู่ที่ยอดขาย อยู่ที่ต้นทุน`
  needed `ต่างหาก`.
- Result + means/exception missing bridge — `เห็นภาพจริงของร้านตัวเอง ไม่ต้องเปิด Excel`
  needed `โดย` between clauses.
- Sequenced action missing bridge — `ถ่ายรูปบิลจากตลาด ระบบอ่านรายการให้เอง` needed
  `แล้ว` between actions.

### marketing-blurb (codex/with_skill)

- Problem→solution pivot missing — `ของหมดก็เสียยอดขาย ของค้างก็กลายเป็นต้นทุนเงียบ
  ระบบนี้ช่วย...` no pivot between problem-list and solution.
- Same 3rd-person address issue (`เจ้าของร้านเล็ก`).
- Tone perceived as too cold — bank-explainer voice mismatched with
  SaaS-for-SME-restaurant audience.

### tech-doc-short (claude/with_skill)

- Wrong classifiers — `bucket หนึ่งใบ`, `token หนึ่งใบ` (should be `ถัง`, `อัน`).
- Verb-level calque — `ระเบิดได้เต็มความจุ` (calque of "burst").
- Missing `จะ` modal — `เลือกตัวไหนขึ้นอยู่กับว่า` needed `จะเลือกตัวไหน`.
- Function-word confusion — `bucket จะเต็ม` should be `จนเต็ม` (until full).
- Robot-prose subjectless clause — `เพราะรับประกัน output rate` over-dropped subject.

### tech-doc-short (codex/with_skill)

- Missing `จะ` modal — `วิธีนี้คุม average rate ได้`.
- Missing `กับ` after `เหมาะ` — `เหมาะตอนที่อยากให้`.
- Verb-level calque — `ถ้า bucket เต็มก็ทิ้ง` (calque of "drop").
- Function-word formality drift — `ดีเมื่อ` reads stiffly; native is `ดีเวลา` /
  `ดีตอนที่`.
- Phrase calque — `ภายในขอบเขตที่ตั้งไว้`.

## Trace per CLAUDE.md iteration discipline

| Pattern                                | Existing rule                | Status                     | Action                                            |
| -------------------------------------- | ---------------------------- | -------------------------- | ------------------------------------------------- |
| Demographic noun for `คุณ`             | register.md pronoun list     | Existed; fired weakly      | Strengthened in register.md + new Person-arity section in SKILL.md |
| Contrastive correction missing `ต่างหาก` | Frame 4 (closure particles)  | Particle missing from list | Added `ต่างหาก` + example                          |
| Result + means/exception missing `โดย` | None directly                | Real gap                   | New anti-pattern #40 (umbrella for seam connectives) |
| Sequenced action missing `แล้ว`        | Frame 6 (mentions in passing)| Existed; fired weakly      | Frame 6 anchoring example added; #40 sub-case     |
| Problem→solution pivot                 | Frame 7 (rhetorical-question only) | Existed; fired narrowly | Frame 7 broadened (question / demonstrative / `แต่`); special-case anchor added |
| Bank-cold tone in SaaS marketing       | register.md lumps marketing into Explainer | Category error | Marketing split into family of 4 sub-registers     |
| `!` and emotional reassurance bans     | Anti-patterns #19, #24       | Over-broad scope           | Rescoped to bank-explainer registers; softened in SaaS-SME and retail-tech |
| Wrong classifiers                      | None                         | New gap                    | New anti-pattern #41 (classifier guide)            |
| Missing `จะ` modal                     | None                         | New gap                    | New anti-pattern #42                               |
| `จะ`/`จน`, `เมื่อ`/`เวลา`, `กับ` after `เหมาะ` | None              | New gap                    | New anti-pattern #43 (function-word confusion)     |
| Verb-level calque (`ระเบิด`/`ทิ้ง`)     | style-rules #27 (idiom only) | Adjacent; not specific     | New anti-pattern #44; #27 cross-references it      |
| Subjectless robot-prose                | Frame 5 (zero anaphora — too aggressive) | Existed without limit | Frame 5 caveat added; demonstrative-bridge example |
| Marketing voice/gender                 | register.md mentions in passing | Buried as pronoun detail | Voice promoted to peer concept; gender ASK required for Personal-blog |
| Definition-first SEO opening           | None                         | Corpus-derived gap         | New anti-pattern #45                               |

## Structural restructure (delivered this iteration)

1. **Marketing register family** — split out of Explainer with 4 sub-registers
   (SaaS-SME / B2B-formal / fintech-warm / retail-tech), each tied to corpus
   exemplars.
2. **Voice promoted to peer of Register** — gender, brand mood, formality level
   are now top-level voice attributes, not pronoun sub-bullets.
3. **Person-arity as a top-level SKILL.md section** — 1st (brand) / 2nd (reader =
   `คุณ`, never demographic noun) / 3rd (product). Most critical for Marketing.
4. **Frame 4** — `ต่างหาก` added to closure inventory; contrastive-correction example.
5. **Frame 5** — demonstrative-as-bridge strategy added (3rd cohesion mechanism);
   zero-anaphora caveat documenting where it fails.
6. **Frame 6** — standalone `แล้ว` as sequence bridge example.
7. **Frame 7** — broadened from rhetorical-question-only to question / demonstrative /
   simple `แต่`; problem→solution pivot anchoring example.
8. **SKILL.md workflow** — register family + voice + person-arity as identification
   steps; gender ASK required for Personal blog.
9. **Anti-patterns #19, #24** — rescoped to bank-explainer family registers.
10. **Anti-pattern #40** — umbrella for seam-connective family (4 sub-cases:
    contrastive / means-exception / sequenced / problem→solution pivot).
11. **Anti-patterns #41–#44** — new "Surface grammar" section: classifiers,
    missing `จะ` modal, function-word confusion, verb-level calque.
12. **Anti-pattern #45** — definition-first SEO opening.
13. **Style-rule #27** — cross-references new #44 for bare-verb calques.

## Corpus expansion

40 curated entries committed to `corpus/curated/` across 8 categories
(`bank-longform`, `marketing/{saas-sme,b2b-formal,fintech-warm,retail-tech}`,
`tech-writing`, `newspaper-feature`, `translation`). All meet 5+ minimum.

`corpus/curated/` and `corpus/raw/` are gitignored — prose may contain third-party
copyrighted material. Only the index (`corpus/README.md`) and resume protocol
(`corpus/RESUME.md`) are tracked.

Single-author bias flagged in `tech-writing` (somkiat only) and `translation`
(Salforest only); future expansion needed if corpus is re-scoured.

## Deferred / open questions

- **Marketing for retail emotional copy / FMCG-style** — still excluded per
  CLAUDE.md scope; if needed for future evals, locked source decision needs
  another expansion pass.
- **Eval-skill consistency check** — process gap surfaced this iteration: eval
  prompts and skill rules drifted independently. Future eval additions should
  verify the skill's registers/voices cover the target audience before generating.
- **Iteration 2 should run with kode-thai loop** — the loop driver is wired in
  `tests/generate/conftest.py` but never end-to-end tested. Iteration 2 will
  exercise it and validate the restructured skill against it.
