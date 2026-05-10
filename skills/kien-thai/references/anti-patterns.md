# Anti-patterns: AI tells in Thai prose

Each entry: rule, why, **bad** (synthetic AI-Thai), **good** (natural Thai). Synthesized
from observed patterns in real Thai tech writing, bank long-form blogs, young-newspaper
features, and skilled non-fiction translation.

Each rule cross-references the **discourse frame** it violates (see `SKILL.md`):

- **F1** — Topic-comment over SVO
- **F2** — Condition / time / frame goes first
- **F3** — Sentence boundaries via space and paragraph, not period
- **F4** — Closure via sentence-final particles
- **F5** — Cohesion via zero anaphora and demonstratives
- **F6** — Pacing via ก็
- **F7** — Pivots via rhetorical question

Some rules are stylistic conventions outside the frames (register, padding, etc.).
Those are labelled **Style**.

Inline-code Thai examples may exceed the 90-column rule when the example itself is
longer than that — they're treated as atomic, like URLs.

## Connectives and transitions  *(F6, F7)*

### 1. ซึ่ง-stacking

AI uses ซึ่ง to glue every dependent clause. Native writers use a period or restructure.

- **Bad**: `Kubernetes เป็นระบบจัดการคอนเทนเนอร์ ซึ่งพัฒนาโดย Google ซึ่งเปิดเป็นโอเพนซอร์ส ซึ่งได้รับความนิยมอย่างแพร่หลาย`
- **Good**: `Kubernetes เป็นระบบจัดการคอนเทนเนอร์ของ Google ปัจจุบันเป็นโอเพนซอร์สและมีคนใช้เยอะมาก`

Budget: at most **one ซึ่ง per sentence**, and prefer ที่ when the antecedent is
concrete.

### 2. ทั้งนี้ + อีกทั้ง + นอกจากนี้ stacked

AI piles them; humans pick one or skip.

- **Bad**: `ทั้งนี้ระบบยังรองรับการขยายตัว อีกทั้งยังมีความปลอดภัยสูง นอกจากนี้ยังใช้งานง่าย`
- **Good**: `ระบบขยายได้ ปลอดภัยพอใช้ และตั้งค่าไม่ยาก`

`ทั้งนี้` in real bank writing appears almost exclusively near the disclaimer/CTA. Not
as a paragraph opener.

### 3. Mechanical "อย่างไรก็ตาม" at every contrast

Humans use แต่, แต่ว่า, ทว่า sparingly, or just a new sentence.

- **Bad**: `อย่างไรก็ตาม การใช้งานในระดับ production มีข้อจำกัดบางประการ`
- **Good**: `แต่พอเอาขึ้น production จริง ก็มีอะไรให้ปวดหัวอีก`

Heuristic: drop "however" in roughly half its English occurrences.

### 4. โดย-clause sprawl

`โดยที่... โดยการ... โดยมี...` chains.

- **Bad**: `ระบบทำงานโดยที่มีการจัดเก็บข้อมูลโดยใช้ database โดยมีการ query ผ่าน API`
- **Good**: `ระบบเก็บข้อมูลใน database และเปิด query ผ่าน API`

Cap at one โดย per paragraph. Prefer ด้วย, ผ่าน, จาก, with, or just no connective.

### 5. ในขณะที่ for English contrast

`ในขณะที่` is mainly temporal in Thai. For contrast, use แต่, ส่วน, กลับ.

- **Bad**: `ในขณะที่ A เชื่อ X, B เชื่อ Y`
- **Good**: `A เชื่อ X แต่ B เชื่อ Y` / `A เชื่อ X ส่วน B กลับเชื่อ Y`

## Passive and agency  *(F1)*

### 6. ถูก- passive on actions with no real agent

Thai ถูก- carries adversative reading. Native writers use it for genuinely unfortunate
events (ถูกวิจารณ์, ถูกปฏิเสธ, ถูกแฮก) and re-cast everything else to active.

- **Bad**: `ข้อมูลจะถูกส่งไปยังเซิร์ฟเวอร์โดยไคลเอนต์ และจะถูกประมวลผลโดยระบบ`
- **Good**: `ไคลเอนต์ส่งข้อมูลไปที่เซิร์ฟเวอร์ แล้วระบบประมวลผลต่อ`

- **Bad**: `หนังสือเล่มนี้ถูกเขียนโดยแฮรารี`
- **Good**: `หนังสือเล่มนี้แฮรารีเป็นคนเขียน` / `แฮรารีเขียนหนังสือเล่มนี้`

### 7. "ถูกพิจารณาว่าเป็น" / "ได้รับการพิจารณาว่าเป็น"

Calque of "is considered (to be)."

- **Good**: `ถือกันว่าเป็น...` / `นับว่าเป็น...` / `คนมองว่าเป็น...`

## Nominalization and padding  *(Style)*

### 8. ทำการ + verb

Pure padding.

- **Bad**: `ทำการติดตั้ง / ทำการรัน / ทำการตรวจสอบ / ทำการศึกษาเรื่องนี้`
- **Good**: `ติดตั้ง / รัน / เช็ค / ศึกษาเรื่องนี้`

### 9. การ- nominalization of every verb

- **Bad**: `การทำการทดสอบและการทำการ deploy ของระบบ`
- **Good**: `เทสและ deploy ระบบ` / `ตอน deploy กับตอนเทส`

Reserve การ- for genuinely abstract topics (การปฏิวัติ, การเรียนรู้) and for headings.

### 10. มีความ + adjective

- **Bad**: `โค้ดนี้มีความซับซ้อนและมีความยากในการ maintain`
- **Good**: `โค้ดนี้ซับซ้อนและดูแลยาก`

- **Bad**: `ภาษามีความสำคัญต่อการอยู่รอดของเผ่าพันธุ์`
- **Good**: `ภาษาสำคัญต่อการอยู่รอดของเผ่าพันธุ์`

Reserve มีความ for genuine emphasis.

Counter-exception: see #38 — `เป็นความ + V` (predicate-noun, e.g. `เป็นความตั้งใจ`)
is required grammar, not padding. Don't strip it to a bare verb.

### 11. การที่...นั้น... subject framing

Calque of "the fact that X is..."

- **Bad**: `การที่ระบบสามารถรองรับผู้ใช้จำนวนมากนั้น เป็นเรื่องที่สำคัญ`
- **Good**: `ระบบต้องรับโหลดได้เยอะ เรื่องนี้สำคัญ`

### 12. การที่...ทำให้... causal chain

Calque of "the fact that X causes Y."

- **Bad**: `การที่สมองของมนุษย์มีขนาดใหญ่ขึ้นทำให้การคลอดยากขึ้น`
- **Good**: `ขนาดสมองที่ใหญ่ขึ้นบังคับให้มนุษย์ต้องคลอดก่อนกำหนด`

Topicalize the noun, pick a vivid verb, drop การที่.

### 13. ในเรื่องของ X / ในส่วนของ X as topic markers

Calques of "regarding / as for." Often unnecessary.

- **Bad**: `ในเรื่องของเศรษฐกิจ ประเทศไทยกำลัง...`
- **Good**: `เศรษฐกิจไทยกำลัง...` / `ส่วนเศรษฐกิจ ประเทศไทย...`

### 14. X ของ Y ของ Z chains

- **Bad**: `การพัฒนาของระบบเศรษฐกิจของประเทศไทย`
- **Good**: `การพัฒนาเศรษฐกิจไทย`

Thai compounds by juxtaposition, not by ของ.

### 39. `ที่มี + adjective` padding when noun-noun compound exists

AI calques English `[noun] that has [quality]` patterns into `[noun]ที่มี[คุณ]`.
Thai usually compounds noun-noun directly without `ที่มี` scaffolding.

- **Bad**: `งานเขียนทั่วไปที่มีคุณภาพ` (calque of "general writing that has quality")
- **Good**: `งานเขียนคุณภาพทั่วไป` (noun-noun: "quality writing, generally")

- **Bad**: `บทความที่มีความน่าสนใจ`
- **Good**: `บทความน่าสนใจ`

This compounds with anti-pattern #10 (มีความ + adj). When you see `ที่มี + ความ + adj`,
both layers are usually padding — strip both.

## Openers  *(Style)*

### 15. "ในยุคปัจจุบัน / ในโลกที่..." panorama

Banned. Real writers open with a fact, a confession, a symptom, a question.

- **Bad**: `ในยุคปัจจุบันที่เทคโนโลยีพัฒนาอย่างก้าวกระโดด การพัฒนาซอฟต์แวร์จึงมีความสำคัญ...`
- **Good (war-story)**: `สวัสดีครับ วันนี้จะเล่าเรื่องตอน traffic พุ่งจน DB ล่มให้ฟัง`
- **Good (news)**: `Red Hat ประกาศถอด Xorg ออกจาก RHEL 10`
- **Good (explainer)**: `มีเงินใช้แค่เดือนชนเดือน ไม่เคยเหลือเก็บ — เคยรู้สึกแบบนี้ไหม`
- **Good (question hook)**: `เคยสงสัยไหมว่าทำไม API ที่ดูเร็วบนเครื่องตัวเอง พอขึ้น production ถึงช้า`

### 16. "เป็นที่ทราบกันดีว่า / เป็นที่รู้กันว่า"

Real writers don't assert consensus they have to declare. They show the symptom.

### 17. Cliché headlines

- **Bad**: `ทุกสิ่งที่คุณต้องรู้เกี่ยวกับ X`
- **Good**: question pair (`X คืออะไร / Y ได้จริงไหม`) / specific pain frame /
  numbered angle (`5 เรื่องที่...`)

### 45. Definition-first SEO opening

`X คือ ...` as the first sentence is the SEO-blog default — homogenizes openings
across SaaS, fintech, and accounting tutorials. Replace with reader-symptom or
question-hook unless the term genuinely needs defining for the audience.

- **Bad**: `ภาษีหัก ณ ที่จ่าย คือ ภาษีที่ผู้จ่ายเงินต้องหักไว้...`
- **Good (symptom)**: `เคยจ่ายค่าจ้างแล้วโดนถามจากบัญชีว่าหัก ณ ที่จ่ายแล้วยัง?`
- **Good (question)**: `ถ้าคุณเคยจ่ายเงินค่าบริการให้บริษัทอื่น อาจต้องหักภาษีไว้ — แล้วเท่าไหร่?`

Reserve `X คือ ...` for reference docs and explainers where the definition really is
the goal, not for marketing or conversion-oriented copy.

## Closings  *(Style)*

### 18. โดยสรุป + recap

Real Thai writing rarely closes with "in summary."

- **Bad**: `โดยสรุปแล้ว Kubernetes เป็นเครื่องมือที่มีประโยชน์อย่างยิ่งในการ...`
- **Good (war-story)**: `เท่านี้ก่อนนะครับ ใครเคยเจอเคสแปลก ๆ มาคุยกันได้`
- **Good (explainer)**: `เพื่อให้คุณมีชีวิตทางการเงินที่ดีขึ้น`
- **Good (synthesis)**: reframe the original question — don't summarize.

### 19. Imperative product CTAs (Explainer / Marketing-B2B-formal / Marketing-fintech-warm)

- **Bad**: `รีบสมัครเลย!` / `อย่ารอช้า!`
- **Good (advisory)**: `กู้เท่าที่จำเป็นและชำระคืนไหว` / `ผู้ลงทุนควรทำความเข้าใจก่อนตัดสินใจ`

**Scope**: full strictness in Explainer, Marketing/B2B-formal, Marketing/fintech-warm,
News, Academic. **Softened in Marketing/SaaS-SME and Marketing/retail-tech** — a single
`!` at hook or CTA is fine, but the rest of the close should still stay advisory rather
than imperative-with-bang.

## Padding and intensifiers  *(Style)*

### 20. Empty intensifiers

- **Bad**: `อย่างมหาศาล / อย่างน่าทึ่ง / อย่างไม่น่าเชื่อ / อย่างมีประสิทธิภาพ / อย่างมาก`
- **Good**: substitute a number, a named example, or a Thai-native intensification
  (`ยิ่ง X เท่าไหร่ ยิ่ง Y เท่านั้น`).

### 21. Symmetric tricolons

`รวดเร็ว ปลอดภัย และมีประสิทธิภาพ` — AI's signature.

- **Good**: uneven, specific lists.
  `เร็วขึ้นชัด ๆ จาก 800ms เหลือ ~120ms และ memory ไม่บวมเหมือนเดิม`

### 22. "ไม่ว่าจะเป็น A B หรือ C" overuse

Used sparingly in real copy; AI defaults to it for any list.

### 23. Over-hedging

`อาจจะมีความเป็นไปได้ที่จะ...` / `อาจจะ...ก็เป็นไปได้ว่า...อาจ`

- **Good**: `น่าจะ` once, or just assert. ttb hedges with a singular `อาจ`, not stacked.

### 24. Generic emotional reassurance (Explainer / Marketing-B2B-formal / Marketing-fintech-warm)

- **Bad**: `ไม่ต้องกังวล เป็นเรื่องที่เข้าใจได้`
- **Good**: specifics — what the reader concretely should do next.

**Scope**: full strictness in Explainer, Marketing/B2B-formal, Marketing/fintech-warm,
News, Academic. **Softened in Marketing/SaaS-SME** — a brief reassurance at hook or
pivot is acceptable when paired with a concrete next-step
(`ไม่ต้องกลัวเริ่มไม่ทัน — ลองฟรี 30 วันได้เลย`).

## Pronouns and politeness  *(F5, register)*

### 25. ครับ/ค่ะ on every sentence

Wrong register for body copy of explainers, tech docs, marketing. Real bank explainers
(SCB, ttb, Krungsri body) use **zero** ครับ/ค่ะ. Particles appear in: quoted speakers,
personal blog openings/sign-offs, social/chat copy.

- **Bad (explainer)**: `การออมเงินสำคัญมากครับ คุณควรเริ่มเก็บตั้งแต่วันนี้ครับ`
- **Good (explainer)**: `การออมเงินสำคัญ ยิ่งเริ่มเร็วเท่าไหร่ยิ่งดี`

### 26. ท่าน as default pronoun

Reads as legal/old-bank copy. Default is **คุณ** (instructional/direct) or **เรา**
(concept-teaching).

### 27. Avoiding ผม/เรา to sound "objective"

In personal blog / dev war-story register, dropping first-person reads as translated
press release.

- **Bad**: `จึงทำการศึกษาและทดลองใช้งาน`
- **Good**: `ผมเลยลองเล่นดู` / `เราเลยเอามาลองที่ทีมก่อน`

### 28. Explicit pronominal subjects in every sentence

English needs *we / you / it*; Thai drops them once topic is set.

- **Bad**: `เราต้องเข้าใจว่าเราอยู่ในโลกที่เราสร้างขึ้นมาเอง`
- **Good**: `ต้องเข้าใจว่าโลกที่เราอยู่ คือโลกที่สร้างขึ้นเอง`

### 29. Dummy "มัน" for English "it"

- **Bad**: `มันเป็นที่ชัดเจนว่า...`
- **Good**: `เห็นได้ชัดว่า...` / `ชัดเจนว่า...`

### 30. สำหรับ for broad English "for"

- **Bad**: `สำหรับฉันแล้ว ฉันคิดว่า...`
- **Good**: `ฉันคิดว่า...` / `ในความเห็นของฉัน...`

## Punctuation  *(F3, Style)*

### 31. Comma-glued apposition

Thai uses spaces for apposition, not commas.

- **Bad**: `แฮรารี, นักประวัติศาสตร์ชาวอิสราเอล, แย้งว่า...`
- **Good**: `แฮรารี นักประวัติศาสตร์ชาวอิสราเอล แย้งว่า...` (spaces only)

### 32. English em-dashes / semicolons

Thai prose rarely uses `—` or `;`. Real writers use comma, parens, paragraph break,
or just whitespace. Periods are an option but not the default — see #37.

- **Bad**: `แนวคิดนี้ — ซึ่งเริ่มต้นในศตวรรษที่ 18 — ได้เปลี่ยนโลก`
- **Good**: `แนวคิดนี้ (ซึ่งเริ่มต้นในศตวรรษที่ 18) ได้เปลี่ยนโลก` or split into two
  sentences.

### 37. Full-stop overuse  *(F3)*

English requires a period after every sentence. Modern Thai web writing
(blog, marketing, explainer, news) uses periods sparingly. Sentence boundaries are
carried by spaces and paragraph breaks. AI inserts periods because the English
training data conventions carry over. Result: prose with the rhythm of a typewriter.

- **Bad (period spam)**: `ระบบทำงานเร็วขึ้น. ใช้ memory น้อยลง. ทีมพอใจมาก.`
- **Good**: `ระบบทำงานเร็วขึ้น ใช้ memory น้อยลง ทีมพอใจมาก`

Heuristic: drop mid-paragraph periods. Reserve periods for end-of-paragraph snap or
genuinely terminal statements where finality is intended (`เท่านี้ก่อน.`).

## Closure  *(F4)*

### 38. Missing closure particle on additive frames

Thai uses sentence-final particles (`ด้วย`, `แล้ว`, `ไป`, `อยู่`, `เลย`, `ก็แล้วกัน`,
`อยู่ดี`) to wrap clauses. English has no equivalent, so AI omits them and Thai
sentences feel dangling. Especially watch frames that *imply* "also Y": `ไม่ได้...อย่างเดียว`,
`ไม่ใช่แค่...`, `ไม่เพียงแต่...` almost always need `ด้วย` or similar to finish the
implicit additive clause.

- **Bad (dangling)**: `repo นี้ไม่ได้มากับกฎอย่างเดียว มี eval harness ผูกกับ claude และ codex`
- **Good (closed)**: `repo นี้ไม่ได้มากับกฎอย่างเดียว มี eval harness ผูกกับ claude และ codex ด้วย`

Beyond the additive frame, watch for clipped statements after a topic — they often
want `ก็` opening (Frame 6) plus a particle close.

- **Bad (clipped)**: `ในรายการนี้ ไม่มีคอลัมนิสต์ดังคนไหน เป็นความตั้งใจ`
- **Good**: `ในรายการนี้ ไม่มีคอลัมนิสต์ดังคนไหน ก็เป็นความตั้งใจ`

Related pitfall — **don't strip `เป็นความ` to a bare verb.** Thai verbs can't serve
as subject complements alone; `ตั้งใจ` without `เป็นความ-` or an explicit subject
(`เราตั้งใจ`) flips to imperative ("intend!") or "intent on doing X." This is the
inverse of rule #10: `มีความ + adj` is bureaucratic padding, but `เป็นความ + V` for
"X is [verb-as-noun]" is required grammar, not padding.

- **Bad (bare verb)**: `ที่ไม่มีคอลัมนิสต์ดัง ตั้งใจ`
- **Good (nominalized)**: `ที่ไม่มีคอลัมนิสต์ดัง เป็นความตั้งใจ`
- **Good (explicit subject)**: `ที่ไม่มีคอลัมนิสต์ดัง เราตั้งใจ`

### 40. Missing seam connectives (F4, F6, F7)

Umbrella for a family of AI tells: omitting Thai's between-clause beats because the
English source has none. Different particles per seam type, but the underlying
pattern is one.

- **Contrastive correction** (`ไม่ได้ X อยู่ที่/เป็น/คือ Y`) → close with `ต่างหาก`
  (Frame 4). #38 above covers the additive variant.

  - **Bad**: `ปัญหาส่วนใหญ่ไม่ได้อยู่ที่ยอดขาย อยู่ที่ต้นทุน`
  - **Good**: `ปัญหาส่วนใหญ่ไม่ได้อยู่ที่ยอดขาย อยู่ที่ต้นทุนต่างหาก`

- **Result + means/exception** (`X. ไม่ต้อง Y`) → bridge with `โดย` / `ด้วย` / `ก็`.
  Cap one `โดย` per paragraph (#4) — that single use is fine.

  - **Bad**: `เห็นภาพจริงของร้านตัวเอง ไม่ต้องเปิด Excel`
  - **Good**: `เห็นภาพจริงของร้านตัวเอง โดยไม่ต้องเปิด Excel`

- **Sequenced action** (`X. Y.`) → bridge with `แล้ว` (or `แล้ว ก็`, see Frame 6).

  - **Bad**: `ถ่ายรูปบิลจากตลาด ระบบอ่านรายการให้เอง`
  - **Good**: `ถ่ายรูปบิลแล้วระบบจะอ่านรายการให้เอง`

- **Problem-list to solution** → pivot via question, demonstrative bridge, or
  contrastive `แต่`. See Frame 7 special case.

Bullet-list cadence (`X. Y. Z. ระบบนี้ช่วย...`) is the AI signature when this rule
fires weakly across a paragraph.

## Sentence-level shape  *(Style)*  *(Style)*

### 33. Monotone sentence length

AI homogenizes around ~20 words. Real Thai prose mixes 6-word and 35-word sentences in
the same paragraph.

### 34. Heading-Heading-bullet-bullet with no prose

Real long-form has 2–4 sentence prose paragraphs between headings. AI skips straight to
bullets.

### 35. Bullet-dump every list of 2

Commit to prose for 2–3 items; switch to bullets only at 4+ or when items are
parallel-shaped.

### 36. "หนึ่งใน + ที่ + superlative" stacking

Calque of "one of the most ___ X."

- **Bad**: `เขาเป็นหนึ่งในนักเศรษฐศาสตร์ที่มีอิทธิพลมากที่สุดในศตวรรษที่ 20`
- **Good**: `เขาคือนักเศรษฐศาสตร์ผู้ทรงอิทธิพลที่สุดคนหนึ่งของศตวรรษที่ 20`

## Surface grammar  *(Style)*

Sentence-level Thai grammar issues that AI gets wrong because the English source has
no equivalent surface marker. Distinct from the discourse frames — these operate at
the word/phrase level.

### 41. Wrong classifier (ลักษณนาม)

Thai requires a classifier when counting or specifying a noun. AI defaults to `ใบ`
for "thing" or drops the classifier entirely. Each noun has an established
classifier; using the wrong one reads as foreign-fluent.

- **Bad**: `bucket หนึ่งใบ` / `request กิน token หนึ่งใบ` / `server หนึ่งตัว`
- **Good**: `bucket หนึ่งถัง` / `request กิน token หนึ่งอัน` / `server หนึ่งเครื่อง`

Common technical-noun classifiers:

- `เครื่อง` — server, computer, machine, device
- `ตัว` — variable, function, instance, character, parameter
- `อัน` — generic small/abstract object (token, item, record)
- `ถัง` — bucket, tank, container
- `ชิ้น` — piece, item (concrete physical thing)
- `รายการ` — list item, transaction, entry
- `บรรทัด` — line (of text/code)
- `หน้า` — page

If unsure, omit the count (`เก็บ token เพิ่ม`) over picking a wrong classifier.

### 42. Missing `จะ` modal/future marker

English present tense covers future, modal, and habitual readings. Thai uses `จะ` to
mark future or hypothetical/modal clauses. AI omits it when the English source has
no explicit future marker, producing clauses that read as bare description rather
than the intended modal.

- **Bad**: `เลือกตัวไหนขึ้นอยู่กับว่า downstream ทนต่อ burst ได้แค่ไหน`
- **Good**: `จะเลือกตัวไหนขึ้นอยู่กับว่า downstream ทนต่อ burst ได้แค่ไหน`

- **Bad**: `วิธีนี้คุม average rate ได้`
- **Good**: `วิธีนี้จะคุม average rate ได้`

- **Bad**: `พอเริ่มยิงทีก็ระเบิดได้เต็มความจุ`
- **Good**: `พอจะเริ่มยิงทีก็ยิงได้เต็มความจุ` / `ตอนที่เริ่มยิงก็ยิงได้เต็มความจุ`

### 43. Function-word confusion (จะ / จน / ก็ / กับ / เมื่อ)

Short connectives carry distinct meanings; AI substitutes them based on shape rather
than function.

- **`จะ` (future/modal) vs `จน` (until / extent)**

  - **Bad**: `client ไม่ได้ยิง bucket จะเต็ม`
  - **Good**: `client ไม่ได้ยิง bucket จนเต็ม`

- **`เมื่อ` (formal "when") vs `เวลา` / `ตอนที่` (natural casual "when")** —
  `เมื่อ` reads stiffly in conversational/explainer/marketing registers.

  - **Bad (stiff)**: `token bucket ดีเมื่อ traffic burst`
  - **Good (natural)**: `token bucket ดีเวลามี burst` / `token bucket ดีตอนที่ traffic burst`

- **Missing `กับ` after `เหมาะ`** — `เหมาะ` requires an object marker.

  - **Bad**: `เหมาะตอนที่อยากให้...`
  - **Good**: `เหมาะกับตอนที่อยากให้...` / `เหมาะกับงานที่...`

Heuristic: when a short connective feels off, check whether AI picked the
register-formal cousin (`เมื่อ`) where the natural-register cousin (`เวลา` /
`ตอนที่`) fits better.

### 44. Verb-level calque

Translating English verbs literally without checking whether Thai uses the same verb
for the same action. Distinct from idiom calque (style-rules #27) — this is at the
bare verb.

- **Bad**: `ระเบิดได้เต็มความจุ` (calque of "burst")
- **Good**: `ยิงได้เต็มความจุ`

- **Bad**: `ถ้า bucket เต็มก็ทิ้ง` (calque of "drop"; also `ก็` is calque of English
  "then" in conditional-consequence — Thai prefers `จะ` for hypothetical-modal)
- **Good**: `ถ้า bucket เต็ม request จะโดน reject` / `ถ้า bucket เต็มจะถูกปฏิเสธ`

- **Bad**: `ภายในขอบเขตที่ตั้งไว้` (calque of "within the bounds")
- **Good**: `ภายในลิมิตที่ตั้งไว้` / `ไม่เกินที่ตั้งไว้`

Heuristic: when a Thai verb feels metaphorical-but-flat, search for the English verb
it's translating. If the English verb is idiomatic-physical (burst / drop / cap /
throttle), the Thai equivalent is usually a different verb, not the literal physical
one.

## Forbidden phrase blocklist (for self-edit search)

Search for these and rewrite when found:

- `ในยุคปัจจุบัน`
- `ในโลกปัจจุบัน` / `ในโลกที่`
- `เป็นที่ทราบกันดีว่า` / `เป็นที่รู้กันว่า`
- `ปฏิเสธไม่ได้ว่า`
- `เป็นสิ่งสำคัญที่ต้องตระหนัก`
- `ทำการ` (almost always padding)
- `มีความสำคัญ` (usually just `สำคัญ`)
- `การที่...นั้น`
- `ในเรื่องของ` / `ในส่วนของ`
- `อย่างมีประสิทธิภาพ` / `อย่างมาก` / `อย่างมหาศาล`
- `โดยสรุปแล้ว` / `กล่าวโดยสรุป`
- `รีบ...เลย!` (imperative product CTAs)
- `นั่นเอง!` (fake-friendly closer)
