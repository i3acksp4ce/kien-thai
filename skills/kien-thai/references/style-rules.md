# Positive style rules

Counterpart to `anti-patterns.md`. These are rules to apply, not patterns to avoid.

Inline-code Thai examples may exceed the 90-column rule when the example itself is
longer than that — they're treated as atomic, like URLs.

## Sentence shape and rhythm

1. **Mix sentence lengths violently.** A 6-word sentence next to a 35-word one is
   normal Thai prose. Test your draft: if every sentence is ~20 words, break some.

   Good rhythm:
   > เริ่มจากเล็ก ๆ ก่อน. พอ traffic เข้ามาเยอะขึ้น cache layer ที่เคยพอ ก็เริ่มไม่พอ
   > และตอนนั้นเองที่ปัญหา hot key เริ่มโผล่. ปวดหัวมาก.

2. **Connective budget.** In a 100-word paragraph: at most one ซึ่ง, one โดย, one
   ดังนั้น. Drop "however" in roughly half its English occurrences. Test every
   connective: would a Thai reader notice it missing? If no, delete.

3. **Topicalize before commenting.** Thai prefers `topic → comment` over English's
   SVO. When the English would calque a passive ("X is done by Y"), front the patient
   as topic and use active voice.

   - English: `The fact that the human brain grew larger created a problem during childbirth.`
   - Calqued: `ความจริงที่ว่าสมองมนุษย์ใหญ่ขึ้นทำให้เกิดปัญหาในการคลอด`
   - Crafted: `สมองที่ใหญ่ขึ้น คือต้นเหตุของปัญหาในการคลอด`

4. **Break long sentences at conceptual seams.** If your draft has more than ~25 Thai
   words without a break, look for a seam. Skilled translators routinely produce 2–3
   Thai sentences from one English sentence.

5. **Drop pronominal subjects after the topic is established.** Re-state only when
   control changes. A paragraph beginning `เราเรียนรู้จากความผิดพลาด...` can run
   several sentences before *เรา* needs to reappear.

6. **Use ก็ as a pacing particle, not a connective.** `พอ traffic ขึ้น DB ก็เริ่มอืด` —
   feels native. AI tends to drop ก็ entirely or use it wrong.

7. **Use ๆ (mai-yamok) for casual reduplication.** `เรื่อย ๆ`, `ใหม่ ๆ`, `บ่อย ๆ` —
   natural Thai signal.

8. **Use แบบ as a hedger / approximator.** `แบบว่า`, `แบบเร็ว ๆ`, `แบบที่เคยทำ` —
   natural in dev/casual register; rare in AI output.

## Verbs and nouns

9. **Verbs over noun forms when an action is the point.** Prefer `แปลหนังสือ` to
   `ทำการแปลหนังสือ` to `การทำการแปลหนังสือ`. Reserve การ-/ความ- for genuinely
   abstract topics or for headings.

10. **Adjectives directly, not มีความ + adjective.** `โค้ดนี้ซับซ้อน` not
    `โค้ดนี้มีความซับซ้อน`.

11. **Active voice unless the patient is genuinely the topic.** Only use ถูก- when the
    action is genuinely adversative (ถูกวิจารณ์, ถูกแฮก, ถูกปฏิเสธ) or when no agent
    is recoverable.

## Openers and closings

12. **Open with one of:** a fact, a confession, a symptom the reader recognizes, a
    rhetorical question, a concrete number. Never a panorama (`ในยุคปัจจุบัน...`).

13. **Inline parenthetical for definitions, not footnotes.**
    `Kubernetes (หรือเรียกสั้น ๆ ว่า K8s)` — common pattern.

14. **Question-headings when the body answers them**, declarative when the body
    elaborates. Avoid noun-phrase-only headings for explainers.

    - Good: `รวบหนี้…ช่วยให้การเงินดีขึ้นได้อย่างไร?` / `แล้วทำไมถึงต้องเปลี่ยน?` /
      `เคสที่ pricing พัง`

15. **Close without recap.** Real Thai writing ends with: forward-looking line,
    reframed question, quiet handoff (`เท่านี้ก่อน`, `ลองเอาไปเล่นดู`), or just
    stops. Never `โดยสรุปแล้ว...`.

16. **Advisory closings beat imperative CTAs.** Use `ควร` + responsibility framing
    (`กู้เท่าที่จำเป็นและชำระคืนไหว`) over `รีบสมัครเลย!`.

## Concreteness

17. **Numbers and named examples carry the prose.** `p99 ลดจาก 800ms เหลือ ~120ms`,
    `งบ 4 ส่วน: ใช้/ลงทุน/ออม/ฉุกเฉิน`, `50 pods` — anchor abstract claims.

18. **Uneven, specific lists beat symmetric tricolons.** Replace
    `รวดเร็ว ปลอดภัย และมีประสิทธิภาพ` with
    `เร็วขึ้นชัด ๆ จาก 800ms เหลือ ~120ms และ memory ไม่บวมเหมือนเดิม`.

19. **`ยิ่ง X เท่าไหร่ ยิ่ง Y เท่านั้น`** for proportional claims — Thai-native
    intensification, replaces empty `อย่างมาก`.

20. **`นี่คือเหตุผลที่...`** as a clean pivot from problem to concept. Beats
    `ดังนั้นในวันนี้เราจะมาแนะนำ...`.

## Voice and personality

21. **First-person ผม is the default for personal tech writing**; เรา for
    team/collective. Drop both only in pure reference docs and news register.

22. **Conversational asides in parentheses or dashes.** `(เพื่อความง่ายขอใช้เป็น 80M)`,
    `(ใครเคยเจอแบบนี้บ้าง)`. Signals human authorship strongly.

23. **Rhetorical questions to advance arguments.** `แล้วถ้าโหลดเพิ่มอีกสิบเท่าล่ะ?` is
    a normal Thai connective, not a gimmick.

24. **Allow `555` or `5555+` once per long post** in personal blog register. Forbidden
    in news register and most explainer/tech-doc contexts.

25. **Author voice over Thai politeness defaults.** Don't add ครับ/ค่ะ to confident
    essayists when translating. Don't pad with อาจจะ when the source asserts.

## ทับศัพท์ — four-bucket judgment guide

Every foreign term goes into one of four buckets. Pick once per term per document,
commit.

### Bucket 1 — translate to Thai

When a settled Thai equivalent exists and is recognizable.

- *justice* → ความยุติธรรม
- *freedom* → เสรีภาพ
- *cooperation* → ความร่วมมือ
- *capitalism* → ทุนนิยม
- *productivity* → ผลิตภาพ

### Bucket 2 — transliterate (Thai script)

For proper nouns, neologisms with no clean Thai equivalent, or technical terms whose
English form would jar in running prose.

- *algorithm* → อัลกอริทึม
- *blockchain* → บล็อกเชน
- เซิร์ฟเวอร์, ซอฟต์แวร์, ดาต้า, แอป
- Common transliterated brands: เฟซบุ๊ก, กูเกิล (less common in modern body text —
  Latin script wins)

### Bucket 3 — keep in Latin script

For:

- Brand names that are visual identities: Facebook, Google, Apple
- Industry-specific acronyms: GDP, CEO, AI, API, DCA, IPO
- Technical terms developers use in English: deploy, scale, container, payload,
  latency, throughput, query, index, cluster, pipeline
- Famous titles cited as titles: *The Wealth of Nations*
- Terms whose discussion centers on the term itself
  (`คำว่า meritocracy แปลตรงตัวได้ลำบาก`)

### Bucket 4 — coin-and-gloss

For important author concepts that recur.

- First mention: Thai coinage + (English in parentheses + brief gloss).
- Example: `ระเบียบในจินตนาการ (imagined order — ระเบียบที่คนเชื่อร่วมกันว่ามีอยู่จริง)`
- Subsequent mentions: Thai only.

### Heuristics

- Term appears > 5 times and is the author's coinage → Bucket 4.
- Term has a Royal Institute–approved Thai compound → Bucket 1.
- Term is < 3 syllables and visually punchy in Latin (CEO, AI) → Bucket 3.
- Term is a place / person / brand → Bucket 2 on first appearance with Latin in parens;
  Bucket 3 only if the brand is visually distinctive.
- **Never mix buckets for the same term within a document.**

### Code-mix shape

Code-mix at the noun, not the verb. `deploy โค้ด`, `scale ระบบ`, `query ตาราง` — verb
in English, object in Thai is fine. Reverse (`ทำการ deployment ของ code`) reads
bureaucratic.

## Translation craft (English → Thai)

26. **Render English emphatic italics with word-order or particles**, not with
    bold/italic Thai. Thai typography rarely italicizes for emphasis. Use:
    - Final particle: `...แน่นอน`, `...ก็จริง`
    - Foregrounding: putting the emphasized item in topic slot
    - Lexical replacement: `แท้จริง`, `จริง ๆ`, `เสียด้วยซ้ำ`

27. **Localize idioms; preserve metaphors.** "It's raining cats and dogs" →
    `ฝนตกหนักมาก` (meaning, not idiom). But authorial extended metaphors get a
    calque-coined term, kept consistent throughout. For bare-verb calques
    (e.g. "burst" → ระเบิด, "drop" → ทิ้ง, "cap" → ปิดฝา), see anti-pattern #44 —
    Thai often uses a different verb for the same action.

28. **Numeric placement.** English: `in 2019 the law was passed.` In Thai narrative,
    dates often trail: `กฎหมายฉบับนี้ประกาศใช้เมื่อปี 2019`.

29. **Foreign names.** First mention: Thai transliteration + parenthesized original —
    `ไมเคิล แซนเดล (Michael Sandel)`. Subsequent: Thai only. Famous-enough names skip
    the parenthetical (`แฮรารี`).

30. **Don't translate the same technical term twice in the same paragraph.** First
    mention establishes the Thai/transliterated form; later mentions don't gloss again.

31. **Don't add politeness the source doesn't have.** Confident essayists stay
    confident in Thai. No added ครับ/ค่ะ, no hedging อาจจะ inserted into declarative
    sentences.

32. **Headings: shorter than the English, often noun-only.**
    - English: `How Imagined Orders Shape Cooperation`
    - Thai: `ระเบียบในจินตนาการกับความร่วมมือ`
    - Not: `วิธีที่ระเบียบในจินตนาการหล่อหลอมความร่วมมือ`

    Thai chapter titles favor noun-noun juxtaposition with `กับ` / `และ` / colon.

## Structure

33. **Commit to prose paragraphs of 2–4 sentences before bulleting.** Bullets earn
    their place when items are parallel-shaped or the list is 4+.

34. **Numbered sections (1. / 2. / 3.)** are fine and common in bank explainers. Pair
    each with a short heading; don't bullet inside without prose context.

35. **Disclaimers absorbed into voice, not bolted on.** ttb's `กู้เท่าที่จำเป็น` reads
    as ethics, not ad. Krungsri's `ทั้งนี้ ผู้ลงทุนควร...` is one sentence, then the
    piece ends.
