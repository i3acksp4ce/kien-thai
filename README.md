# เขียนไทย

**skill สอน Claude เขียนภาษาไทยให้คนไทยอ่านสบาย**

> ภาษาไทยที่ AI สร้างมีกลิ่น

คนไทยอ่านแล้วต้องย้อนอ่านใหม่ บางครั้งก็เลิกอ่านไปเลย ปัญหานี้ไม่ได้เกิดจากความรู้
ภาษาของ AI แต่เกิดจาก training data ที่เอนไปทางภาษาราชการและการแปลตรงตัวจากภาษา
อังกฤษ ผลคือประโยคยาว ๆ ต่อกันด้วย "ซึ่ง" และ "โดย" ครับ/ค่ะ ทุกประโยค คำว่า
"ในยุคปัจจุบัน" ขึ้นต้นทุกบทความ

repo นี้รวบรวมกฎการเขียนภาษาไทยที่กลั่นจากนักเขียน blog สาย dev จริง บทความ explainer
ของธนาคารใหญ่ คอลัมนิสต์รุ่นใหม่ และนักแปลหนังสือสำนักพิมพ์ที่มีรสนิยม ขึ้นรูปเป็น
skill สำหรับ Claude ปลายทาง: Thai prose ที่อ่านลื่น มีน้ำเสียง และเลือก register
ได้ถูกบริบท

## เหมาะกับใคร

- developer ที่ใช้ AI เขียน technical doc / README / changelog ภาษาไทย
- ทีม content marketing ที่ต้องผลิตงานภาษาไทยเร็วและสม่ำเสมอ
- ใครก็ตามที่เคยเจอ output ภาษาไทยจาก AI แล้วตะหงิดใจ

## เริ่มใช้ยังไง

skill อยู่ที่ `skills/thai-prose/` ให้ copy ทั้ง folder ไปไว้ใน `.claude/skills/`
ของ project ที่ต้องการ หรือ import ผ่านระบบ skill management ที่คุณใช้อยู่

(ตัวอย่าง: ใน [ACE](https://github.com/ace-rs/ace) ใช้ `ace import skills/thai-prose`
จาก clone ของ repo นี้)

## โครงสร้าง skill

| ไฟล์                            | เนื้อหา                                          |
| ------------------------------- | ------------------------------------------------ |
| `SKILL.md`                      | หลักคิดหลัก + workflow                           |
| `references/anti-patterns.md`   | 36 รูปแบบ AI-Thai ที่ต้องเลี่ยง พร้อมตัวอย่าง    |
| `references/style-rules.md`     | กฎเชิงบวก + ทับศัพท์ 4-bucket judgment           |
| `references/register.md`        | คู่มือเลือก register สำหรับงานแต่ละแบบ           |
| `references/examples.md`        | ตัวอย่าง before/after เต็มรูปแบบ                 |

skill โหลด `SKILL.md` เป็น context หลัก แล้วอ่าน reference อื่น ๆ เมื่อจำเป็น
ตามหลัก progressive disclosure

## Eval ทำงานยังไง

repo นี้ไม่ได้มากับกฎอย่างเดียว มี eval harness ใช้ pytest ผูกกับ `claude` และ
`codex` ใน bare mode คู่กัน เพื่อเทียบผลก่อนกับหลังการ inject skill ด้วย

```bash
uv sync
uv run pytest                       # sanity เร็ว ๆ ไม่เรียก API
uv run pytest -m generate           # ยิงจริง ใช้ token จริง
uv run pytest -m generate -k claude # เลือก backend เดียว
```

artifact ลงที่ `thai-prose-workspace/iteration-N/<eval>/<backend>/<config>/` รีวิว
ผลร่วมกับ Claude ใน chat โดยตรง ไม่มี viewer แยก

## ที่มาของกฎทุกข้อ

ทุกกฎใน skill นี้กลั่นจากตัวอย่างงานเขียนจริง:

- **blog dev ไทย** — Blognone long-form, Somkiat Puisungnoen, Thanaphoom Babparn,
  Nutta, Rath Panyowat
- **explainer สาย finance** — Krungsri The COACH, ttb fin tips, SCB Stories & Tips,
  KBank The Wisdom
- **newspaper รุ่นใหม่** — The Standard, The MATTER, The 101 World, Workpoint Today
- **งานแปล non-fiction** — Bookscape, openworlds, Salt Publishing,
  สฤณี อาชวานันทกุล

ในรายการนี้ไม่มีคอลัมนิสต์ดัง ๆ คนไหน ก็เป็นความตั้งใจ กฎควรครอบคลุมงานเขียน
คุณภาพทั่วไป ไม่ใช่ลอกเสียงใครคนเดียว

## สถานะ

iteration ต้น ๆ กฎทั้ง 36 ข้อใน `anti-patterns.md` ผ่านการ research แล้ว แต่ยัง
ไม่ผ่าน eval หลายรอบ priority และ wording ของแต่ละกฎจะปรับตามผล eval แต่ละรอบ
ใครเจอกฎที่พลาดหรือผิด เปิด issue หรือ PR ได้

## License

ยังไม่กำหนด รอเลือกหลังโครงสร้างนิ่ง
