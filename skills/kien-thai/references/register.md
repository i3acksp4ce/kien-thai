# Register and voice guide

Register and voice are two top-level concerns. **Register** governs structural
conventions (particles, openers, closings, connectives, person deixis defaults).
**Voice** governs personality cues within those conventions (gender, brand mood,
formality). Pick both before drafting; if either is ambiguous, ASK. Wrong register
is worse than rough prose.

Inline-code Thai examples may exceed the 90-column rule when the example itself is
longer than that — they're treated as atomic, like URLs.

## Quick register decision

| Output type                                       | Register                  |
| ------------------------------------------------- | ------------------------- |
| Tech doc, README, API reference, framework guide  | Explainer                 |
| Bank/finance educational, "X คืออะไร" article      | Explainer                 |
| Marketing landing for SaaS / SMB owners           | Marketing/SaaS-SME        |
| Marketing landing for enterprise / B2B            | Marketing/B2B-formal      |
| Marketing for consumer fintech                    | Marketing/fintech-warm    |
| Marketing for merchant tooling (Lazada/Grab-style)| Marketing/retail-tech     |
| Personal blog post, dev war-story, retrospective  | Personal blog             |
| News announcement, release notes, press release   | News / reference          |
| Long-form analysis, op-ed, philosophical essay    | Academic                  |
| Internal Slack-style team announcement            | Personal blog (light)     |
| Email to customers from a person                  | Personal blog (light)     |

## Voice attributes (orthogonal to register)

Voice attributes apply across registers but matter most where personality varies:
Marketing (brand mood) and Personal blog (gender, formality).

- **Gender** — required for Personal blog. Selects `ผม`/`ดิฉัน` + `ครับ`/`ค่ะ` in
  greetings and sign-offs. ASK before drafting if unstated. Don't silently default
  to `ผม`.
- **Brand mood** — for Marketing. Distinguishes warm-direct (FoodStory, Page365),
  cold-formal (Bluebik), warm-pro (SCB Stories, Krungsri Plearn), practical-direct
  (Lalamove merchant). Pick from corpus exemplars.
- **Formality level within register** — opener choice (slang vs explainer), particle
  frequency, English code-switch density all shift formality without changing
  register.

## Person deixis

Identify three roles for any piece. Most critical for Marketing:

- **1st person — speaker**. Marketing: brand as `เรา` ("our team", "this company").
  Personal blog: author as `ผม`/`ดิฉัน`. News/reference: no first-person at all.
- **2nd person — addressee**. Marketing: reader as `คุณ` directly. **Never** substitute
  the audience's demographic noun (`เจ้าของร้าน`, `ผู้ใช้`, `นักลงทุน`, `ผู้ประกอบการ`)
  for `คุณ` in body copy. Demographic nouns belong in headers and category framing,
  not as the active 2nd-person referent.
- **3rd person — product, concept, third party**. Marketing: `ระบบนี้`,
  `เครื่องมือนี้`, `แอปนี้`.

Marketing example:

- **Bad** (3rd-person address substitutes demographic noun):
  `เครื่องมือนี้ทำให้เจ้าของร้านเห็นภาพจริงของร้านตัวเอง`
- **Good** (direct 2nd-person):
  `ระบบนี้ช่วยให้คุณเห็นภาพจริงของร้านได้ทันที`

Don't mix `เรา` and `คุณ` within the same paragraph (Krungsri pattern). Body in
`เรา` when teaching a concept; advisory line shifts to `คุณ` for action.

### `deixis-continuity` *(mechanical · all-registers · hard)*

Once a deixis frame is established for a stretch of prose — including the
**zero / implicit-2nd-person** frame, where no pronoun is named but the reader
is the implied addressee — the rest of the passage must hold it. AI tends to
slip an indefinite-someone (`ใคร`, `คน`, `ใครๆ`) into passages running in
implicit-2nd-person mode, because English freely interpolates "no one" /
"someone" without breaking address. Thai readers track deixis tighter — the
slip reads as a fragment with a missing subject.

- **Bad** (third-party `ใคร` dropped into implicit-2nd-person passage):
  `จานเดิมที่เคยกำไรดี ตอนนี้กลายเป็นขาดทุน แต่ไม่มีใครรู้`
- **Good** (deixis stays implicit-2nd-person; *you* don't realize):
  `จานเดิมที่เคยกำไรดี ตอนนี้กลายเป็นขาดทุนโดยไม่รู้ตัว`

When the surrounding passage has no explicit `คุณ` yet but is clearly
addressing the reader, treat the frame as implicit-2nd-person and keep all
references inside that frame. Promote a loose afterthought tail to a modifier
(`โดยไม่รู้ตัว`, `โดยไม่ทันสังเกต`) rather than introducing a third party.

## Register 1 — Explainer

Default for tech docs, README/API reference, bank educational long-form, B2B-formal
explainer. Goal: explain or persuade an adult reader without sliding into clinical
formality or social-media chumminess. **Not for SaaS/SME marketing copy** — see the
Marketing family below.

**Particles**: zero ครับ/ค่ะ in body. Particles only in quoted speakers.

**Pronouns**:

- `เรา` — when teaching a concept the reader is new to. Inclusive, softens
  prescription.
- `คุณ` — when prescribing action, scenarios, instructions, CTAs. **Address the
  reader directly with `คุณ`; never substitute their demographic noun**
  (`เจ้าของร้าน`, `ผู้ใช้`) for `คุณ` in body copy.
- Don't mix `เรา` and `คุณ` within the same paragraph. Krungsri pattern: body in
  `เรา`, advisory line shifts to `ผู้ลงทุน` (third-person formal) or `คุณ`.
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

## Register 2 — Marketing (family)

Marketing is its own register *family* with four sub-registers, each derived from
distinct corpus voices. Pick the sub-register, then apply its conventions.

**Common to all Marketing sub-registers**:

- **Particles**: zero ครับ/ค่ะ in body. Only inside customer testimonial quotes.
- **Person deixis**: required (see Person deixis above). Brand `เรา`, reader `คุณ`,
  product `ระบบนี้`/`แอปนี้`. Demographic-noun substitution is a hard fail.
- **Openers**: prefer reader's pain symptom or question hook over definition-first
  (`X คือ...`). Definition-first is the SEO default but reads as homogenized — use
  only when the term genuinely needs defining for the audience.
- **Connectives**: tight budget. One `ซึ่ง`, one `ด้วย`, one `โดย` max per paragraph.
- **`cta-bang`, `generic-reassurance`** (banning `รีบสมัครเลย!` and generic emotional
  reassurance) apply at *bank-explainer* strictness for B2B-formal and fintech-warm,
  but relax in SaaS-SME and retail-tech as noted below.

### 2.1 Marketing/SaaS-SME

Source corpus: FoodStory, Page365, FlowAccount, PEAK Account.
Voice: warm-direct, addresses non-tech SMB owners.

**Punctuation as warmth**: `!` allowed once, at hook or CTA. Soft particle close
(`ได้เลย`, `ก็แล้วกัน`) preferred over bare clipped CTAs. (`ต่างหาก` is
contrastive correction, not CTA close — see `f4/targhak-closure`.)

**Openers**: pain symptom (`ขายดีทุกวัน แต่พอสิ้นเดือนเงินไม่เหลือ`), question hook
(`เคยรู้สึกไหมว่า...`).

**Closings**: advisory CTA (`ลองใช้ฟรี 30 วันได้เลย`) over imperative-with-bang
(`รีบสมัครเลย!`). `cta-bang` *softened*: a single `!` at hook or CTA is fine
when the rest of the close stays advisory.

### 2.2 Marketing/B2B-formal

Source corpus: Bluebik, Wisesight, AWS Thailand corporate posts.
Voice: advisory authority, third-person institutional.

**Person deixis**: institutional brand third-person (`บริษัท`, team name) over `เรา`;
reader `คุณ` only in instructional sections.

**Code-switch**: heavy English/Thai bilingual with bracketed-bilingual gloss
(`Thai term (English Original)`) — the B2B-formal signature.

**Closings**: capability summary or contact CTA. No emotional appeal. `cta-bang`
and `generic-reassurance` apply at full bank-explainer strictness.

### 2.3 Marketing/fintech-warm

Source corpus: SCB Stories & Tips, Krungsri Plearn / The COACH, ttb fin tips.
Voice: warm-pro, lifestyle-coach. Closest to the existing Explainer register but
with marketing-shaped openers and CTAs.

**Punctuation as warmth**: `…` (three-dot ellipsis) at coaching pauses is the
bank-warm signature (`อยากซื้อบ้านแต่กังวล…`). `!` is rare.

**Person deixis**: brand `เรา` for teaching, switches to `คุณ` for action/advisory.

**Openers**: lifestyle scenario, age-bracket framing (`คนอายุ 30+ ควร...`).

**Closings**: forward-looking advisory. `cta-bang`, `generic-reassurance` apply at full
strictness.

### 2.4 Marketing/retail-tech

Source corpus: Lalamove merchant blog and similar merchant-tooling content.
Voice: practical-direct, instructional, hook with `!`.

**Punctuation**: `!` allowed at hook/CTA. Vivid colloquial markers (`สาย-` slang for
identifying merchant types) are signature.

**Person deixis**: reader `คุณ` direct, brand third-person institutional.

**Openers**: pain-point hook + service framing.

**Closings**: feature CTA or signposting next read. `cta-bang` *softened*:
single `!` at hook or CTA is fine.

## Register 3 — Personal blog / dev war-story

For dev blogs, retrospectives, "I tried X, here's what happened" posts. Voice is
warm, first-person, technically dense.

**Gender** (required — ASK before drafting if not stated):

- Male voice: `ผม` for first-person, `ครับ` for greeting/sign-off particles.
- Female voice: `ดิฉัน` for first-person, `ค่ะ` for greeting/sign-off particles.
- Don't silently default to `ผม` — many Thai dev writers use female voice.

**Particles**: ครับ/ค่ะ at the opening greeting, at sign-off, and at moments of
direct address (`มาดูกันครับ` / `มาดูกันค่ะ`). Never at the end of every body
sentence — that reads as social-media/chat register.

**Pronouns**:

- `ผม` / `ดิฉัน` — first-person default per gender.
- `เรา` — when narrating team work.
- `ทุกคน` / direct address in greetings (`สวัสดีครับทุกคน` / `สวัสดีค่ะทุกคน`).

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
- `!!` (double-bang) — somkiat-style emphasis, signature of older-school Thai dev
  blogs; use sparingly outside that voice.

**Code-mix**: keep `deploy / scale / cluster / latency / payload` etc. in English.
Don't translate dev jargon.

**Models**: Thanaphoom Babparn (tpbabparn.medium.com), Somkiat Puisungnoen
(somkiat.cc), Nutta, Rath Panyowat (rath.asia).

## Register 4 — News / reference

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

## Register 5 — Academic / long-form analysis

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

**Closings**: synthesis or reframe — leave the reader with the reframed problem, not
a summary. 101's pattern: `หากโจทย์ของประเทศไม่ใช่แค่...แต่เป็น...`.

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
- **Marketing with customer testimonial**: Marketing register in body, Personal-blog
  register inside testimonial blockquotes (ครับ/ค่ะ allowed inside quote).

## Coherence within a passage

### `register-drift` *(mechanical · all-registers · hard)*

Once you pick a register, sustain it. AI tends to drift — using a casual form
(`คนไหน`, `ยังไง`, `เยอะ`) in one sentence and a formal counterpart
(`คนใดคนหนึ่ง`, `อย่างไร`, `จำนวนมาก`) in the next. Native readers feel the
wobble even when each sentence in isolation is fine.

Common casual ↔ formal pairs to keep consistent within one passage:

- `คนไหน` ↔ `คนใด` / `คนใดคนหนึ่ง`
- `ยังไง` ↔ `อย่างไร`
- `เยอะ` ↔ `มาก` / `จำนวนมาก`
- `แบบไหน` ↔ `แบบใด` / `รูปแบบใด`
- `ทำไม` ↔ `เพราะเหตุใด`
- `ตอนนี้` ↔ `ขณะนี้` / `ในปัจจุบัน`
- `อยากรู้` ↔ `ต้องการทราบ`

Pick one column for the whole passage and stay there. Switching mid-paragraph
reads as AI register-drift; switching at section/heading breaks is fine if
intentional (see Cross-register section above).

## Default if unclear

Default to **Explainer** for bank/tech docs. **Marketing/SaaS-SME** for product copy
targeting SMB owners. ASK when the audience or brand voice is unclear — wrong
register is worse than rough prose.
