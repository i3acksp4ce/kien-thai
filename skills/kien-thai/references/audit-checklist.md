# Audit checklist

Compact grep-able checklist for kode-thai audit pass. Each item links to the fuller
rule definition by file + number. Run **mechanical** checks first — these are
correctness violations and apply to all registers. Then run **craft** checks
filtered by the piece's register (see `register.md` scope).

## Mechanical (correctness — apply to all registers)

### Connectives  *(`ai-tells.md`)*

- [ ] ≤1 ซึ่ง per sentence (#1)
- [ ] No ทั้งนี้+อีกทั้ง+นอกจากนี้ stacking (#2)
- [ ] อย่างไรก็ตาม dropped in half its English occurrences (#3)
- [ ] ≤1 โดย per paragraph; no โดยที่/โดยการ chains (#4)
- [ ] ในขณะที่ only for time, not contrast (#5)

### Passive (F1)  *(`ai-tells.md`)*

- [ ] No ถูก-passive on non-adversative verbs (#6)
- [ ] No ถูกพิจารณาว่าเป็น calque (#7)

### Padding / calque shapes  *(`ai-tells.md`)*

- [ ] No ทำการ + verb (#8)
- [ ] No การ-nominalization of every verb (#9)
- [ ] No มีความ + adj for non-emphatic uses (#10)
- [ ] No การที่...ทำให้ causal chain (#12)
- [ ] No ในเรื่องของ / ในส่วนของ (#13)
- [ ] No X ของ Y ของ Z chains (#14)
- [ ] No ที่มี + adj when noun-noun compound exists (#39)

### Banned openers  *(`ai-tells.md`)*

- [ ] No ในยุคปัจจุบัน / ในโลกที่ panorama (#15)
- [ ] No เป็นที่ทราบกันดี / เป็นที่รู้กันว่า (#16)

### Padding / overhedging  *(`ai-tells.md`)*

- [ ] No ไม่ว่าจะเป็น A B หรือ C overuse (#22)
- [ ] No over-hedging stacks (#23)

### Pronouns and politeness (F5, register)  *(`ai-tells.md`)*

- [ ] No ครับ/ค่ะ in body, register-aware (#25)
- [ ] No ท่าน as default (#26)
- [ ] First-person ผม/เรา in personal-blog register (#27)
- [ ] Pronouns dropped after topic established (#28)
- [ ] No dummy มัน for English "it" (#29)
- [ ] No สำหรับ for broad "for" (#30)

### Punctuation (F3)  *(`ai-tells.md`)*

- [ ] No comma-glued apposition (#31)
- [ ] No em-dashes / semicolons (#32)
- [ ] No หนึ่งใน + ที่ + superlative (#36)
- [ ] No periods mid-paragraph (#37) — closer to ban than budget

### Closure (F4)  *(`ai-tells.md`)*

- [ ] Closure particle on additive frames `ไม่ได้...อย่างเดียว` etc. (#38)
- [ ] Seam connectives present: ต่างหาก / โดย / แล้ว / pivot (#40)

### Surface grammar  *(`grammar.md`)*

- [ ] Correct classifier (ลักษณนาม) (#41) — register-aware: `อัน`/`ตัว`
      shortcuts acceptable in conversational/explainer/personal-blog; precise
      classifier required in News, Academic, Marketing/B2B-formal
- [ ] จะ on future/modal clauses (#42)
- [ ] Function words correct: จะ/จน, เมื่อ/เวลา, กับ-after-เหมาะ (#43)
- [ ] No verb-level English calque: ระเบิด / ทิ้ง / etc. (#44)
- [ ] `สามารถ + V + ได้` frame for capability statements
- [ ] `ใน` not `ของ` for time periods

### Person-arity  *(`SKILL.md` Person-arity section, `register.md`)*

- [ ] 2nd-person reader = `คุณ`; never demographic noun (`เจ้าของร้าน`, `ผู้ใช้`)
- [ ] No `เรา` ↔ `คุณ` mixing within paragraph

## Craft / voice preferences (apply per register — see `register.md` scope)

### Headlines and openers  *(`craft.md`)*

- [ ] No cliché headlines (#17)
- [ ] No definition-first SEO opening for marketing copy (#45)

### Closings  *(`craft.md`)*

- [ ] No โดยสรุป + recap (#18)
- [ ] Imperative-with-bang CTAs scoped (#19) — banned in formal registers,
      single `!` allowed at hook in SaaS-SME / retail-tech

### Intensifiers and lists  *(`craft.md`)*

- [ ] No empty intensifiers (#20)
- [ ] No symmetric tricolons (#21)
- [ ] Generic emotional reassurance scoped (#24) — banned in formal, softened in
      SaaS-SME

### Sentence shape  *(`craft.md`)*

- [ ] Sentence length variance (#33)
- [ ] Prose between headings (#34)
- [ ] Don't bullet-dump 2-item lists (#35)

## Forbidden phrase blocklist (grep targets)

These should never appear in any register **as use** (in the model's own prose).
They may appear as **mention** when wrapped in backticks or inside markdown
quote markers — for example, when skill documentation or examples.md discusses
the pattern itself. When auditing, grep for **un-backticked** occurrences only;
backticked or quoted strings are use-vs-mention exempt.

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
- `รีบ...เลย!` (imperative product CTAs — except scoped per #19)
- `นั่นเอง!` (fake-friendly closer)
