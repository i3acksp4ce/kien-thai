# Register guide

Four registers cover almost everything the skill needs to produce. Picking the wrong
register is worse than rough prose — readers feel the mismatch immediately. Identify
register first; if ambiguous, ask.

Inline-code Thai examples may exceed the 90-column rule when the example itself is
longer than that — they're treated as atomic, like URLs.

## Quick decision

| Output type                                       | Register               |
| ------------------------------------------------- | ---------------------- |
| Tech doc, README, API reference, framework guide  | Explainer (default)    |
| Marketing landing page, product copy for adults   | Explainer              |
| Bank/finance/B2B explainer, "X คืออะไร" article    | Explainer              |
| Personal blog post, dev war-story, retrospective  | Personal blog          |
| News announcement, release notes, press release   | News / reference       |
| Long-form analysis, op-ed, philosophical essay    | Academic               |
| Internal Slack-style team announcement            | Personal blog (light)  |
| Email to customers from a person                  | Personal blog (light)  |

## Register 1 — Explainer (default)

The default for tech docs, marketing copy, bank long-form, B2B explainers. Goal:
explain or persuade an adult reader without sliding into either clinical formality or
social-media chumminess.

**Particles**: zero ครับ/ค่ะ in body. Particles only in quoted speakers.

**Pronouns**:

- `เรา` — when teaching a concept the reader is new to. Inclusive, softens
  prescription.
- `คุณ` — when prescribing action, scenarios, instructions, CTAs.
- Don't mix `เรา` and `คุณ` within the same paragraph. Krungsri pattern: body in
  `เรา`, advisory line shifts to `ผู้ลงทุน` (third-person formal).
- Avoid `ท่าน` — reads as legal/old-bank.
- Avoid `เพื่อน ๆ` — too student-audience.

**Openers**: reader's symptom (`มีเงินใช้แค่เดือนชนเดือน...`), question hook
(`เคยรู้สึกไหมว่า...`), or scenario (`หากคุณมีภาระหนี้สินเชื่อ...`). Never
`ในยุคปัจจุบัน...`.

**Closings**: forward-looking line (`เพื่อให้คุณมีชีวิตทางการเงินที่ดีขึ้น`), or
single advisory line. No recap.

**Connectives**: budget one of each kind per paragraph. Rotate: `ดังนั้น` (causal) →
`นอกจากนี้` (additive, sparingly) → `แต่` for contrast → `ทั้งนี้` only near
disclaimer/CTA.

**Headings**: questions when body answers them, declarative when body elaborates.
Avoid noun-phrase-only headings.

**Sentence shape**: vary deliberately. Mix prose (2–4 sentence paragraphs) with bullets
(when 4+ parallel items). Don't bullet-dump 2-item lists.

**Tone**: warm but adult. Concrete numbers and named examples carry the prose, not
generic intensifiers.

**Models**: Krungsri The COACH, ttb fin tips, SCB Stories & Tips. KBank The Wisdom for
slightly more upmarket tone.

## Register 2 — Personal blog / dev war-story

For dev blogs, retrospectives, "I tried X, here's what happened" posts. The voice is
warm, first-person, technically dense.

**Particles**: ครับ at the opening greeting, at sign-off, and at moments of direct
address (`มาดูกันครับ`). Never at the end of every body sentence — that reads as
social-media/chat register.

**Pronouns**:

- `ผม` (or `ดิฉัน`) — first-person default for personal posts
- `เรา` — when narrating team work
- `ทุกคน` / direct address in greetings (`สวัสดีครับทุกคน`)

**Openers**: confession (`สวัสดีครับ วันนี้จะเล่าเรื่องตอน traffic พุ่งจน DB ล่ม`),
or jumping straight into the situation. Greeting + topic, no panorama.

**Closings**: handoff to reader (`เท่านี้ก่อนนะครับ ใครเคยเจอเคสแปลก ๆ มาคุยกันได้`),
or "to be continued" (`เดี๋ยวมาเล่าต่อ part หน้า`). Don't recap.

**Connectives**: looser than explainer register, but still budgeted. `แต่` over
`อย่างไรก็ตาม`. Conversational `ก็`, `แล้ว`, `พอ` for pacing.

**Sentence shape**: most variance allowed. Fragments OK (`ปวดหัวมาก.`). Conversational
asides in parens or em-dashes (`(เพื่อความง่ายขอใช้เป็น 80M)`). Rhetorical questions
(`แล้วถ้าโหลดเพิ่มอีกสิบเท่าล่ะ?`).

**Casual signals (allow sparingly)**:

- `555` or `5555+` — once per long post, max
- Emoji — light use OK, don't pepper
- `แบบว่า`, `แบบ` as approximators
- ๆ for casual reduplication

**Code-mix**: keep `deploy / scale / cluster / latency / payload` etc. in English.
Don't translate dev jargon.

**Models**: Thanaphoom Babparn (tpbabparn.medium.com), Somkiat Puisungnoen
(somkiat.cc), Nutta, Rath Panyowat (rath.asia).

## Register 3 — News / reference

For Blognone-style tech news, release notes, press releases, API reference, factual
bullet points in product docs.

**Particles**: zero. ครับ/ค่ะ banned.

**Pronouns**: no first-person. No `ผม` / `เรา`. Third-person or impersonal
constructions only.

**Openers**: lead with the fact + active verb. `Red Hat ประกาศถอด Xorg ออกจาก RHEL 10`.
Subject + verb + object in one sentence. Attribution in second sentence. Technical
detail in third.

**Closings**: factual close. Citation, version number, date. No recap, no CTA.

**Connectives**: minimal. `แต่`, `และ`, full stop. Avoid `ดังนั้น` unless the causal
link is genuine.

**Voice**: zero personal voice. Active voice. No emoji. No conversational asides.

**Sentence shape**: average ~25 words but vary. Information-dense.

**Models**: Blognone news desk, mainstream Thai tech press, RFC-style reference docs.

## Register 4 — Academic / long-form analysis

For op-eds, philosophical essays, deep policy/economic analysis, book translations of
confident essayists.

**Particles**: zero. ครับ/ค่ะ banned.

**Pronouns**:

- `เรา` — inclusive scholarly. Used for shared human/national experience.
- Abstract nouns for distance: `มนุษย์`, `ผู้คน`, `ผู้ลงทุน`, `สังคมไทย`. Shift between
  `เรา` and abstract nouns to zoom in/out.
- Avoid first-person singular unless the writer's specific perspective is the point.

**Openers**: question (`ทำไมเราถึงทำงาน?`), or specific historical/conceptual frame
(`งานศึกษาเกี่ยวกับระบบเศรษฐกิจแบบสังคมนิยมชิ้นหนึ่ง...`). Never panorama.

**Closings**: synthesis or reframe — leave the reader with the reframed problem, not a
summary. 101's pattern: `หากโจทย์ของประเทศไม่ใช่แค่...แต่เป็น...`.

**Connectives**: longer subordinate-heavy sentences acceptable, but balance with
shorter pivot sentences. `ทว่า` is OK in academic register (literary). `นอกจากนี้`,
`อย่างไรก็ตาม` allowed at genuine pivot points.

**Sentence shape**: longest sentences allowed of any register, but still mix lengths.
Sub-clauses OK if they actually carry distinct ideas.

**ทับศัพท์**: hybrid — Thai-coined terms for translatable concepts (`ผลิตภาพ`,
`กรรมสิทธิ์`, `อุดมการณ์`), Latin script or transliteration for jargon
(`neoliberalism / นีโอลิเบอรัล`, `GDP`, `IPO`). First mention gets `Thai (English)`
parenthetical for important author concepts.

**Tone**: confident, declarative. Don't pad assertions with `อาจจะ` unless source
genuinely hedges.

**Models**: The 101 World long-form, The MATTER deep features, Bookscape/openworlds
non-fiction translations, สฤณี อาชวานันทกุล's translation register.

## Cross-register: when to shift

Some pieces shift register intentionally:

- **Bank explainer with quoted expert**: body in Explainer register (no particles),
  quoted speaker in Personal-blog register (`ครับ` allowed in the quote). Don't bleed
  the quote's register into surrounding prose.
- **Tech doc with personal preface**: preface can be Personal-blog (greeting, context,
  motivation), main doc shifts to Explainer or Reference. Mark the shift visibly
  (`---`, heading).
- **Long-form analysis with reader-application section**: Academic body, then a shift
  to Explainer when zooming to "what this means for you, the reader."

## Coherence within a passage

Once you pick a register, sustain it. AI tends to drift — using a casual form
(`คนไหน`, `ยังไง`, `เยอะ`) in one sentence and a formal counterpart
(`คนใดคนหนึ่ง`, `อย่างไร`, `จำนวนมาก`) in the next. Native readers feel the wobble
even when each sentence in isolation is fine.

Common casual ↔ formal pairs to keep consistent within one passage:

- `คนไหน` ↔ `คนใด` / `คนใดคนหนึ่ง`
- `ยังไง` ↔ `อย่างไร`
- `เยอะ` ↔ `มาก` / `จำนวนมาก`
- `แบบไหน` ↔ `แบบใด` / `รูปแบบใด`
- `ทำไม` ↔ `เพราะเหตุใด`
- `ตอนนี้` ↔ `ขณะนี้` / `ในปัจจุบัน`
- `อยากรู้` ↔ `ต้องการทราบ`

Pick one column for the whole passage and stay there. Switching mid-paragraph reads
as AI register-drift; switching at section/heading breaks is fine if intentional
(see Cross-register section above).

## Default if unclear

Default to Explainer register. It's the safest for tech docs, marketing, B2B, and most
professional writing. If the user wants a more personal voice, they'll say so.
