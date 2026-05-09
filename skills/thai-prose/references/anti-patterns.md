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

## Closings  *(Style)*

### 18. โดยสรุป + recap

Real Thai writing rarely closes with "in summary."

- **Bad**: `โดยสรุปแล้ว Kubernetes เป็นเครื่องมือที่มีประโยชน์อย่างยิ่งในการ...`
- **Good (war-story)**: `เท่านี้ก่อนนะครับ ใครเคยเจอเคสแปลก ๆ มาคุยกันได้`
- **Good (explainer)**: `เพื่อให้คุณมีชีวิตทางการเงินที่ดีขึ้น`
- **Good (synthesis)**: reframe the original question — don't summarize.

### 19. Imperative product CTAs

- **Bad**: `รีบสมัครเลย!` / `อย่ารอช้า!`
- **Good (advisory)**: `กู้เท่าที่จำเป็นและชำระคืนไหว` / `ผู้ลงทุนควรทำความเข้าใจก่อนตัดสินใจ`

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

### 24. Generic emotional reassurance

- **Bad**: `ไม่ต้องกังวล เป็นเรื่องที่เข้าใจได้`
- **Good**: specifics — what the reader concretely should do next.

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
