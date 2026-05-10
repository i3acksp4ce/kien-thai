# Contributing

ขอบคุณที่อยากช่วยปรับปรุง skill นี้ เอกสารนี้สรุปขั้นตอนเสนอแก้ไข — ไม่ว่าจะเจอกฎ
ที่ผิด เจอ AI tell ที่ skill จับไม่ได้ หรืออยากเพิ่มกฎใหม่

## 0. อ่านก่อน

ก่อนเปิด issue หรือ PR ขอให้อ่านสามไฟล์นี้ก่อน:

1. [`skills/kien-thai/SKILL.md`](skills/kien-thai/SKILL.md) — กรอบการเรียบเรียง
   7 ข้อ + person-arity + workflow
2. [`skills/kien-thai/references/register.md`](skills/kien-thai/references/register.md)
   — register 5 family
3. ไฟล์ใน `references/` ที่ตรงกับประเภทกฎ — `ai-tells.md` (mechanical),
   `grammar.md` (surface), `craft.md` (taste), `style-rules.md` (positive)

ส่วนใหญ่ feedback แบบ "กฎข้อนี้ผิด" จริง ๆ แล้วเป็น register-mismatch ไม่ใช่ตัว
กฎพัง — เช็คก่อนว่า register ถูกแล้วหรือยัง

## 1. วินัยการเพิ่มกฎ — trace before you write

ทุกกฎใน skill นี้กลั่นจากงานเขียนจริง (tech blog, bank long-form, newspaper รุ่น
ใหม่, งานแปลฝีมือดี) มี *why* รองรับทุกข้อ — failure mode ที่ป้องกัน หรือ pattern
มนุษย์ที่อยากให้ทำตาม

**กฎที่ไม่มีที่มาจะเน่า** อย่าโตเร็วกว่าหลักฐาน

เวลาเจอ output แย่ ความรู้สึกแรกคืออยากเพิ่มกฎใหม่หรือเข้มงวดกฎเดิม **อดทนไว้**
ทำตาม trace ก่อน:

1. **หา offending pattern** ใน output ที่เป็นปัญหา
2. **map กลับไปยังกฎที่ควรจับได้** — กฎไหน? ไฟล์ไหน? ถ้าไม่เจอ นั่นคือช่องโหว่
   จริง
3. **ถ้ากฎมีอยู่แล้วแต่ไม่ทำงาน** — เพราะอะไร? wording อ่อน? ตัวอย่างไม่ชัด?
   ขัดกับกฎอื่น? register ไม่ตรง? **แก้กฎเดิมที่ wording / ความเด่น / anchoring
   example อย่าซ้อนกฎใหม่ที่พูดเรื่องเดียวกัน**
4. **ถ้าไม่มีกฎครอบคลุมจริง ๆ** ก่อนเพิ่ม เช็คงานค้นคว้าก่อน — pattern นี้มี
   หลักฐานในงานจริงไหม? ถ้ามี ก็ผิวให้เป็นกฎ ถ้าไม่มี กฎใหม่ก็เป็นแค่ข้อสันนิษฐาน
   — flag เป็น provisional แล้ว cite counter-example หรือแหล่งให้ชัด
5. **บันทึก trace** ใน issue / PR description เพื่อให้ที่มาของกฎอยู่กับการแก้

CLAUDE.md ส่วน "Iteration discipline" มีรายละเอียดเดียวกันสำหรับ developer
internal

## 2. ขั้นตอนเสนอแก้ไข

ใช้ template ตามนี้ใน issue / PR:

### a. ระบุ register

prose ตัวอย่างเป็น register ไหน?

- `explainer` — bank/tech long-form
- `marketing-saas-sme` / `marketing-b2b-formal` / `marketing-fintech-warm` /
  `marketing-retail-tech` — Marketing 4 sub-register
- `personal-blog` — dev blog / war-story
- `news` — ข่าว / reference doc
- `academic` — วิชาการยาว

ถ้า register ไม่ตรงกับที่ skill จับ บอกเลยว่าตรงไหน

### b. ระบุชั้นของกฎ

issue เป็นเรื่อง:

- **discourse-level** — โครงสร้างประโยค การจัดอนุประโยค การเปลี่ยน topic
  → frame F1–F7 ใน SKILL.md
- **mechanical** — ตัวเชื่อมเฝือ คำแปลตรงตัว passive ใช้ผิด
  → `ai-tells.md`
- **surface grammar** — ลักษณนาม modal classifier function-word
  → `grammar.md`
- **taste / voice** — headline ซ้ำซาก closing แบบ recap empty intensifier
  → `craft.md`
- **positive guidance** — สิ่งที่อยากให้ทำตอน draft ไม่ใช่กฎ audit
  → `style-rules.md`

ไม่แน่ใจก็เดาก่อน reviewer จะช่วยปรับ

### c. trace

- กฎไหน *น่าจะ* จับ pattern นี้ได้? cite slug
- ทำไมไม่ทำงาน? (wording อ่อน / ตัวอย่างเก่า / ขัด register / ตัวกฎไม่มีจริง)
- เสนอแก้ — rewrite กฎเดิม หรือ เพิ่ม slug ใหม่

### d. ที่มา (กรณีเสนอกฎใหม่)

cite ตัวอย่างจริงอย่างน้อยหนึ่งแหล่ง:

- blog dev ไทย / bank explainer / newspaper รุ่นใหม่ / งานแปล non-fiction —
  พร้อม URL หรือ excerpt
- หรือ counter-example ชัด ๆ ที่แสดงว่ากฎเดิมพลาด

กฎที่ไม่มี citation จะเข้าเป็น *provisional* — มี marker ใน file รอ eval หลาย
รอบยืนยัน

## 3. รูปแบบ slug + metadata

ทุกกฎมี heading รูปนี้:

```markdown
### `<slug>` *(<type> · <scope> · <severity>)*

<body — คำอธิบาย + Bad/Good example>
```

- **slug** — kebab-case อ่านได้ ใช้ romanization ของคำหลัก ถ้าเป็นคำ Thai
  (`chueung-stacking`, `mi-khwam-padding`) หรือชื่อ pattern ตรง ๆ ถ้าไม่มี Thai
  หลัก (`em-dash-semicolon`, `wrong-classifier`)
- **type** — `mechanical` / `grammar` / `craft` / `style` / `frame`
- **scope** — `all-registers` / `scoped` / `<register-key>` (เช่น `marketing`,
  `register`)
- **severity** — `hard` (กฎ correctness) / `soft` (taste) / `structural` (frame)

frame slug ใช้ form `f<N>` (`f1`...`f7`) sub-pattern ใต้ frame ใช้
`f<N>/<descriptor>` (เช่น `f4/targhak-closure`)

cross-reference ระหว่าง rule ใช้ slug ใน backtick ในเนื้อความ — เช่น "ดู
`mid-paragraph-period` สำหรับ period spam" ไม่ใช้เลขลำดับ (legacy IDs ตายไปแล้ว)

## 4. รูปแบบ PR

- **title** สั้น ระบุประเภท + slug ที่กระทบ — เช่น `craft: rewrite cliche-headline
  to cover SEO listicle pattern` หรือ `ai-tells: add new slug for X`
- **body** ครอบคลุม:
  - register และไฟล์ที่กระทบ
  - offending example (snippet จริง)
  - trace ตามข้อ 2 ข้างบน
  - diff ของ rule wording (ถ้าแก้กฎเดิม) หรือ slug + metadata + body ใหม่
    (ถ้าเพิ่มกฎใหม่)
  - citation
- **scope** หนึ่ง logical change ต่อ PR อย่ารวมแก้กฎหลายข้อใน PR เดียว ยกเว้น
  เป็นการ refactor โครงสร้าง

## 5. eval expectations

การแก้กฎมักทำให้ behavior model เปลี่ยน reviewer อาจขอให้รัน eval รอบใหม่ก่อน
merge:

```sh
uv sync
uv run pytest                  # sanity (ฟรี)
uv run pytest -m generate      # full eval (ใช้ API token)
```

ผลลง `workspace/iteration-N/` — เปรียบเทียบ convergence (loop_passes,
converged) กับ baseline iteration ปัจจุบัน ถ้าระดับคุณภาพหรือจำนวน pass แย่ลง
ชัด ๆ reviewer จะ flag

ไม่ต้องรัน eval เองถ้าไม่มี API key หรือ codex setup — บอก reviewer ก็ได้

## 6. ขอบเขตที่ไม่รับ (ตอนนี้)

- LLM-judge eval — ใช้ human review จนกว่าจะพิสูจน์ได้ว่าไม่พอ
- กฎที่อ้างอิงคอลัมนิสต์ดังคนเดียว — skill ครอบคลุม pattern คนทั่วไป ไม่ใช่ลอก
  น้ำเสียงคนใดคนหนึ่ง
- **Stage 4 token-audit** (slim fix-pass bundle) — reject แล้วถาวร อย่าเสนออีก
  fix pass ต้องเห็น ruleset เต็มเสมอ ดูใน `workspace/token-audit/08-synthesis.md`

## ติดต่อ

issue / PR เปิดที่ repo นี้ตรง ๆ — ไม่มี Slack / Discord / mailing list
