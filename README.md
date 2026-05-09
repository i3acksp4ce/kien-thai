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

## หลักคิดของ skill

skill นี้ไม่ได้เป็นแค่ checklist ของคำต้องห้าม แกนกลางคือ **discourse frames 7 ข้อ**
ที่อธิบายว่าภาษาไทยจัด clause จัดประโยค จัดย่อหน้าต่างจากภาษาอังกฤษยังไง พอ frame
ถูก กฎปลีกย่อยส่วนใหญ่ก็ resolve ตาม

1. **Topic-comment เหนือ SVO** — ไทย fronts สิ่งที่ประโยคพูดถึงก่อน ไม่ลาก subject
   หนัก ๆ มาวางหน้าเหมือน English
2. **เงื่อนไข เวลา กรอบ มาก่อน** — ข้อมูล setup วางหน้า main clause ไม่ใช่ห้อย
   ท้ายด้วย "เมื่อ..." แบบฝรั่ง
3. **เว้นวรรค + ขึ้นย่อหน้าแทน period** — ภาษาเขียนไทยไม่มี full stop ขอบเขต
   ประโยคใช้ space กับการขึ้นย่อหน้า
4. **ปิดประโยคด้วย sentence-final particle** — นะ ล่ะ สิ ครับ ไม่ใช่จุด ไม่ใช่
   "ทั้งนี้" ลอย ๆ
5. **Cohesion ด้วย zero anaphora + demonstrative** — ละ subject ที่รู้แล้ว ไม่ใช่
   ลาก "ซึ่ง" ต่อกันสามชั้น
6. **จังหวะด้วย ก็** — particle ที่ฝรั่งไม่มี ใช้ pace ประโยคและบ่งความสัมพันธ์
   loose ระหว่าง clause
7. **Pivot ด้วยคำถามเชิงวาทศิลป์** — เปลี่ยนหัวข้อย่อยด้วย "แล้วถ้า..." แทนการ
   ใช้ "อย่างไรก็ตาม" / "นอกจากนี้"

แต่ละ frame ใน `SKILL.md` link กลับไปยัง anti-pattern เฉพาะที่เกี่ยวข้อง

## โครงสร้าง skill

| ไฟล์                          | เนื้อหา                                            |
| ----------------------------- | -------------------------------------------------- |
| `SKILL.md`                    | discourse frames 7 ข้อ + workflow + register pick  |
| `references/anti-patterns.md` | 39 รูปแบบ AI-Thai ที่ต้องเลี่ยง พร้อมตัวอย่าง      |
| `references/style-rules.md`   | กฎเชิงบวก + ทับศัพท์ 4-bucket judgment             |
| `references/register.md`      | คู่มือเลือก register สำหรับงานแต่ละแบบ             |
| `references/examples.md`      | ตัวอย่าง before/after เต็มรูปแบบ                   |

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
uv run pytest -m evaluate           # heuristic เชิงปริมาณ (advisory)
```

artifact ลงที่ `thai-prose-workspace/iteration-N/<eval>/<backend>/<config>/` รีวิว
ผลร่วมกับ Claude ใน chat โดยตรง ไม่มี viewer แยก การตัดสินคุณภาพ prose เป็นงาน
ของมนุษย์ — `test_quant.py` แค่ flag คำต้องห้ามและความหนาแน่นของ connective ไม่ใช่
quality gate

## วินัยการเพิ่มกฎ

ทุกกฎใน `references/` มีที่มาจาก research งานเขียนจริง ไม่ใช่จากความรู้สึก เวลา
eval ออกมาไม่ดี ขั้นตอนคือ:

1. หา pattern ที่ผิดใน output
2. map กลับไปยังกฎที่ควรจับได้ — ถ้ามีแต่ไม่ทำงาน แก้ wording / prominence ของกฎเดิม
3. ถ้าไม่มีกฎครอบคลุม เช็ค research ก่อน — มี evidence ไหม ถ้าไม่มี กฎใหม่นั้น
   speculative ต้อง flag และเก็บไว้ provisional
4. log trace ใน `iteration-N/feedback.md`

อ่านรายละเอียดใน `CLAUDE.md` ส่วน "Iteration discipline"

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

iteration ต้น ๆ skill ถูก restructure รอบ discourse frames 7 ข้อแล้ว แต่ frame
และกฎปลีกย่อยยังไม่ผ่าน eval หลายรอบ priority และ wording จะปรับตามผลแต่ละ
iteration ใครเจอกฎที่พลาดหรือผิด เปิด issue หรือ PR ได้

## License

[MIT](LICENSE) — ใช้ได้อิสระทั้งงานส่วนตัวและงานเชิงพาณิชย์ ขอแค่เก็บ copyright
notice ไว้
