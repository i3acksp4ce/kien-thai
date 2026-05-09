# Worked before/after examples

Longer rewrites showing multiple anti-patterns fixed at once. For pattern-matching when
self-editing or evaluating Thai prose.

Long Thai prose inside blockquotes is treated as atomic — it may exceed 90 columns.

## Example 1: Tech doc paragraph

### Before (AI-Thai)

> ในยุคปัจจุบันที่เทคโนโลยีพัฒนาอย่างก้าวกระโดด การทำการพัฒนาระบบที่มีความสามารถในการรองรับผู้ใช้จำนวนมากนั้น เป็นสิ่งสำคัญที่ต้องตระหนัก ซึ่ง Rate Limiting เป็นเทคนิคที่ถูกใช้อย่างแพร่หลาย ซึ่งช่วยในการควบคุมจำนวนคำขอที่ถูกส่งเข้ามายังระบบ ทั้งนี้ Algorithm ที่ได้รับความนิยม ได้แก่ Token Bucket และ Leaky Bucket ซึ่งมีความแตกต่างกันในด้านการทำงาน อีกทั้งยังมีข้อดีและข้อเสียที่แตกต่างกันอีกด้วย

**Tells**: panorama opener, ทำการ + การ-, การที่...นั้น, four ซึ่ง stacked, ถูก-
passive, ทั้งนี้ as paragraph opener, มีความ + adj, อีกทั้ง padding.

### After (Explainer register)

> Rate limiting คือเทคนิคจำกัดจำนวน request ที่ระบบรับ ใช้กันแพร่หลายเพราะมันคุมโหลดและกัน abuse ได้ในตัวเดียว.
>
> มี algorithm ที่นิยม 2 แบบ — Token Bucket กับ Leaky Bucket. ทั้งคู่ทำงานคนละแนว และเหมาะกับโจทย์คนละแบบ.

**Fixes**: panorama → fact-first opening; ทำการ/การ- removed; passive recast active;
ซึ่ง budget restored (only one); concrete connector "เพราะ"; specific count "2 แบบ"
beats "ที่ได้รับความนิยม"; em-dash replaced with parens-friendly punctuation;
period-and-restart instead of stacked clauses.

## Example 2: Marketing landing page (SaaS for restaurants)

### Before (AI-Thai)

> ในโลกธุรกิจร้านอาหารที่มีการแข่งขันอย่างดุเดือด การที่เจ้าของร้านสามารถบริหารจัดการต้นทุนได้อย่างมีประสิทธิภาพนั้น เป็นปัจจัยสำคัญที่จะทำให้ธุรกิจประสบความสำเร็จ ซึ่งระบบของเราถูกออกแบบมาเพื่อช่วยให้คุณสามารถจัดการสต็อกวัตถุดิบและคำนวณต้นทุนต่อจานได้อย่างง่ายดายและรวดเร็ว ทั้งนี้คุณจะสามารถเห็นกำไรที่แท้จริงของแต่ละเมนูได้อย่างชัดเจน อีกทั้งยังช่วยลดเวลาในการทำงานได้อย่างมหาศาล รีบสมัครเลยวันนี้!

**Tells**: panorama opener, การที่...นั้น, อย่างมีประสิทธิภาพ, ถูก-passive, ซึ่ง
stacked, ทั้งนี้ + อีกทั้ง padding, อย่างมหาศาล empty intensifier, imperative product
CTA.

### After (Explainer register, SME owner audience)

> เปิดร้านอาหารมา 3 ปีแล้ว ยังไม่รู้ว่าจานไหนกำไรจริง?
>
> เกิดขึ้นกับเจ้าของร้านส่วนใหญ่ — สั่งวัตถุดิบเข้ามา ราคาขึ้นลงทุกอาทิตย์ พอจะคิดต้นทุนต่อจาน ก็ไม่รู้จะเริ่มยังไง.
>
> เราออกแบบระบบนี้มาให้เจ้าของร้านที่ไม่ได้สาย tech ใช้ได้จริง:
>
> - บันทึกสต็อกได้จากมือถือ ไม่ต้องนั่งทำ Excel
> - คำนวณต้นทุนต่อจานอัตโนมัติเมื่อราคาวัตถุดิบเปลี่ยน
> - เห็นกำไรของแต่ละเมนูเป็นตัวเลขจริง ๆ ไม่ใช่ความรู้สึก
>
> ลองใช้ฟรี 30 วัน ไม่ต้องผูกบัตร.

**Fixes**: panorama → reader's symptom (rhetorical question); abstract benefit list →
3 specific bullets with concrete pain points; ถูกออกแบบ → active "เราออกแบบ"; ทำการ +
การที่...นั้น removed; imperative CTA → low-friction trial offer; particle-free body
(Explainer register); concrete number "3 ปี"; uneven bullets with specific values, not
symmetric tricolon.

## Example 3: Translation — confident essayist

### Source (English)

> The fact that meritocracy has become the dominant ideology of our age is, in itself, a remarkable historical development. It was not always so. For most of human history, people inherited their station; the idea that one's position in society should reflect one's individual achievement is, in the long view, a recent and radical proposition.

### Calqued draft (AI-Thai)

> ความจริงที่ว่าระบบคุณธรรมได้กลายเป็นอุดมการณ์ที่โดดเด่นในยุคของเรานั้น เป็นพัฒนาการทางประวัติศาสตร์ที่น่าทึ่งในตัวมันเอง สิ่งนี้ไม่ได้เป็นเช่นนี้เสมอไป ตลอดช่วงเวลาส่วนใหญ่ของประวัติศาสตร์มนุษย์ ผู้คนได้รับการสืบทอดสถานะของพวกเขา การที่ตำแหน่งของบุคคลในสังคมควรสะท้อนถึงความสำเร็จส่วนบุคคลนั้น เป็นข้อเสนอที่ใหม่และรุนแรงในมุมมองระยะยาว

**Tells**: ความจริงที่ว่า / การที่...นั้น chains, calqued passive `ได้รับการสืบทอด`,
dummy "สิ่งนี้" calque of "it", "พวกเขา" English-pronoun-leak,
"ตลอดช่วงเวลาส่วนใหญ่ของประวัติศาสตร์" calques "for most of human history" verbatim,
"ในมุมมองระยะยาว" calques "in the long view".

### Crafted (Academic register, Bookscape-style)

> ระบบคุณธรรม (meritocracy) กลายเป็นอุดมการณ์หลักของยุคนี้ — ในตัวมันเอง นี่คือพัฒนาการทางประวัติศาสตร์ที่น่าทึ่ง.
>
> ก่อนหน้านี้ไม่ได้เป็นแบบนั้น. มนุษย์ส่วนใหญ่ตลอดประวัติศาสตร์สืบทอดสถานะมาจากครอบครัว. ความคิดที่ว่าตำแหน่งของคนในสังคมควรสะท้อนความสำเร็จของตัวเอง — มองในมุมระยะยาว นี่คือข้อเสนอที่ใหม่และรุนแรงเอามาก ๆ.

**Fixes**:

- `ความจริงที่ว่า` removed entirely
- `การที่...นั้น` removed
- ทับศัพท์ Bucket 4 treatment for `meritocracy` on first mention; Thai-coined
  `ระบบคุณธรรม` after
- Passive `ได้รับการสืบทอด` → active `สืบทอดสถานะมาจากครอบครัว` (added `ครอบครัว` to
  compensate for English's implicit agent — natural in Thai)
- Dummy `สิ่งนี้` → `แบบนั้น` (anaphoric demonstrative, more idiomatic)
- `พวกเขา` dropped (Thai pro-drop)
- Sentence breaks at conceptual seams (3 English sentences → 4 Thai)
- `ในมุมมองระยะยาว` → `มองในมุมระยะยาว` (verb form, more natural)
- Authorial confidence preserved — no `อาจจะ` added.

## Example 4: Personal blog opener (dev war-story)

### Before (AI-Thai)

> ในยุคที่ระบบของเราต้องรองรับผู้ใช้จำนวนมาก ทีมของเราได้ทำการเผชิญกับความท้าทายที่สำคัญ ซึ่งเกี่ยวข้องกับการจัดการ database ที่ถูกใช้งานอย่างหนัก ทั้งนี้ในบทความนี้ผมจะมาแชร์ประสบการณ์ที่ได้พบเจอ

**Tells**: panorama opener, ทำการเผชิญ, ซึ่ง, ถูก-passive, ทั้งนี้ as opener,
"ที่สำคัญ" filler.

### After (Personal blog register)

> สวัสดีครับทุกคน
>
> วันนี้จะเล่าเรื่องตอน DB ของเราล่มกลางดึก ตอน user แตะ 70 ล้านคน. ปวดหัวมาก. แต่ก็ได้บทเรียนกลับมาเยอะ.
>
> เริ่มเลยละกัน.

**Fixes**: panorama → greeting + concrete situation with number (`70 ล้านคน`); short
fragments allowed in this register (`ปวดหัวมาก.`); ครับ at greeting (Personal-blog
register); first-person `ผม` natural; `แต่` over `อย่างไรก็ตาม`; abrupt transition to
body (`เริ่มเลยละกัน`) instead of formal "ในบทความนี้".

## Example 5: News register — release announcement

### Before (AI-Thai)

> ในยุคที่ AI กำลังพัฒนาอย่างก้าวกระโดด บริษัทของเราได้ทำการเปิดตัวฟีเจอร์ใหม่ที่มีความสำคัญ ซึ่งจะช่วยให้ผู้ใช้สามารถทำงานได้อย่างมีประสิทธิภาพมากยิ่งขึ้น ทั้งนี้ฟีเจอร์ดังกล่าวถูกพัฒนาขึ้นโดยทีมวิศวกรของเราอย่างต่อเนื่องเป็นระยะเวลากว่า 6 เดือน

**Tells**: panorama, first-person `เรา` in news register, ทำการเปิดตัว, มีความสำคัญ,
ซึ่ง, อย่างมีประสิทธิภาพ, ถูก-passive.

### After (News register)

> Acme เปิดตัว AutoSync ฟีเจอร์ sync ข้ามอุปกรณ์อัตโนมัติ.
>
> AutoSync ทำงานในเบื้องหลังเมื่อผู้ใช้สลับระหว่างมือถือกับเดสก์ท็อป ลดเวลาที่ใช้ในการคัดลอกข้อมูลข้ามอุปกรณ์ลงประมาณ 80% ตามตัวเลขจาก beta program. ทีมพัฒนาใช้เวลา 6 เดือนในการสร้างฟีเจอร์นี้.
>
> AutoSync เปิดให้ใช้บน Pro plan ตั้งแต่วันที่ 15 พฤษภาคม.

**Fixes**: panorama → fact-first lead (subject + verb + object); first-person `เรา`
removed; ทำการเปิดตัว → `เปิดตัว`; ถูก-passive removed; concrete metric `80%` replaces
`อย่างมีประสิทธิภาพ`; specific date and plan tier replace generic "ทั้งนี้";
particle-free; active voice throughout.
