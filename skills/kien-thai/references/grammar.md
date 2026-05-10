# Surface Thai grammar

Sentence-level Thai grammar issues that AI gets wrong because the English source
has no equivalent surface marker. Distinct from the discourse frames — these
operate at the word/phrase level. Each rule here is a hard correctness rule
applying to all registers.

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

English present tense covers future, modal, and habitual readings. Thai uses `จะ`
to mark future or hypothetical/modal clauses. AI omits it when the English source
has no explicit future marker, producing clauses that read as bare description
rather than the intended modal.

- **Bad**: `เลือกตัวไหนขึ้นอยู่กับว่า downstream รับ burst ได้แค่ไหน`
- **Good**: `จะเลือกตัวไหนขึ้นอยู่กับว่า downstream รับ burst ได้แค่ไหน`

- **Bad**: `วิธีนี้คุม average rate ได้`
- **Good**: `วิธีนี้จะคุม average rate ได้`

- **Bad**: `พอเริ่มยิงทีก็ระเบิดได้เต็มความจุ`
- **Good**: `พอจะเริ่มยิงทีก็ยิงได้เต็มความจุ` / `ตอนที่เริ่มยิงก็จะยิงได้เต็มความจุ`

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

Translating English verbs literally without checking whether Thai uses the same
verb for the same action. Distinct from idiom calque (style-rules #27) — this is
at the bare verb.

- **Bad**: `ระเบิดได้เต็มความจุ` (calque of "burst")
- **Good**: `ยิงได้เต็มความจุ`

- **Bad**: `ถ้า bucket เต็มก็ทิ้ง` (calque of "drop")
- **Good**: `ถ้า bucket เต็มก็โดน reject` / `ถ้า bucket เต็มก็จะโดนปฏิเสธ`

Heuristic: when a Thai verb feels metaphorical-but-flat, search for the English
verb it's translating. If the English verb is idiomatic-physical (burst / drop /
cap / throttle), the Thai equivalent is usually a different verb, not the literal
physical one.

### `สามารถ ... ได้` modal frame (positive rule)

Thai expresses "can / is able to" with the discontinuous frame `สามารถ + V + ได้`.
AI sometimes uses bare verbs or overuses one half of the frame. Both halves work
together; for emphatic capability, use both.

- **Bad (bare)**: `ระบบ query ผ่าน API`
- **Good**: `ระบบสามารถ query ได้ผ่าน API` (full frame)
- **Acceptable (informal)**: `ระบบ query ได้ผ่าน API` (only `ได้`)

### `ใน` vs `ของ` for time periods (positive rule)

For time periods (centuries, decades, eras), Thai uses `ใน` — *during* the period —
not `ของ` (which marks possession or relation).

- **Bad**: `นักเศรษฐศาสตร์ที่ทรงอิทธิพลที่สุดของศตวรรษที่ 20`
- **Good**: `นักเศรษฐศาสตร์ที่ทรงอิทธิพลที่สุดในศตวรรษที่ 20`
