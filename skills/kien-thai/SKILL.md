---
name: kien-thai
description: Write Thai-language prose (technical documentation, marketing copy, explainers, blog posts) that reads like a real Thai writer — not generic AI output. Counters training-data skew toward over-formal, over-polite, calqued Thai. Use this skill whenever the user asks for Thai writing, asks to translate English content into Thai, or asks to edit/rewrite existing Thai prose, even if they don't explicitly say "good prose." Also use when the user is in a Thai-language conversation and asks for any non-trivial prose output (a paragraph, section, blog post, landing page, doc page, README in Thai, email, announcement). The default Thai output without this skill is mechanically polite, connective-spammed, and calque-shaped — this skill fixes that.
---

# kien-thai

## Why this skill exists

Generic AI-produced Thai has tells. Native readers feel them as friction —
re-reading sentences, skimming, abandoning. The biggest tells:

- **Connective spam**: ซึ่ง / โดย / ทั้งนี้ / อีกทั้ง / นอกจากนี้ / อย่างไรก็ตาม /
  ดังนั้น in every other clause.
- **Calqued English syntax**: ถูก-passive on actions with no real agent,
  "การที่...นั้น...", long subordinate chains glued by ซึ่ง.
- **Bureaucratic padding**: ทำการ+verb, มีความ+adj, การ-nominalization of every verb.
- **Wrong register default**: ครับ/ค่ะ on every sentence, ท่าน as default address,
  "ในยุคปัจจุบัน..." openers.

Real Thai writers don't write like this. The goal: produce Thai that a Thai reader
can read at speed, with a distinct human voice appropriate to register.

## The deeper problem: discourse frames

Surface-level rules ("don't use ทั้งนี้") treat symptoms. The cause is structural:
**AI-generated Thai imports English's discourse mechanics whole-cloth.** Thai has its
own way of connecting clauses, marking sentence boundaries, closing thoughts,
maintaining cohesion, pacing prose, and pivoting between ideas. When you preserve
English mechanics in Thai words, the result reads as translated AI, even when every
word is grammatical.

Internalize these seven frames first. The granular rules in
`references/ai-tells.md` (mechanical Thai-correctness), `references/grammar.md`
(surface grammar), and `references/craft.md` (voice / taste preferences) become
applications of the frames — many of them auto-resolve once the frames are right.

### Frame 1 — Topic-comment over subject-verb-object

English defaults to SVO. Thai often fronts the topic (whatever the sentence is *about*)
and then comments on it. When the English source has a heavy subject ("the fact that
X is..."), calquing it into Thai produces `การที่...นั้น...` chains that no Thai
reader produces unprompted.

- English (SVO): `The system processes this data every five minutes.`
- Calqued: `ระบบประมวลผลข้อมูลพวกนี้ทุก ๆ 5 นาที`
- Topicalized: `ข้อมูลพวกนี้ ระบบจะ process ทุก 5 นาที`

Heuristic: if the English subject is heavy, abstract, or really the patient of the
verb, front it as topic in Thai.

Covers anti-patterns #6 (ถูก-passive), #12 (การที่...ทำให้).

### Frame 2 — Condition, time, and frame go first

English puts conditions and time-frames after the main clause: "X happens when Y" /
"X if Y". Thai prefers the inverse: condition first, main clause after.

- English: `The DB starts timing out when traffic spikes.`
- Calqued: `DB จะเริ่ม timeout เมื่อ traffic พุ่งสูง`
- Native: `พอ traffic พุ่งสูง DB ก็เริ่ม timeout`

Common Thai openers for fronted conditions/times: `พอ...ก็...`, `ถ้า...จะ...`,
`เมื่อ...`, `ตอน...`, `หาก...`.

### Frame 3 — Sentence boundaries via space and paragraph, not period

English uses a period after every sentence. Modern Thai web writing
(blog, marketing, explainer, news) uses periods sparingly. Sentence boundaries are
carried by spaces and paragraph breaks; periods are reserved for end-of-paragraph
snap or genuinely terminal statements.

- AI density: `ระบบทำงานเร็วขึ้น. ใช้ memory น้อยลง. ทีมพอใจมาก.`
- Native: `ระบบทำงานเร็วขึ้น ใช้ memory น้อยลง ทีมพอใจมาก`

Heuristic: drop mid-paragraph periods; let space carry the boundary. Keep periods
only where a snap or finality is genuinely intended.

The Royal Institute's *หลักเกณฑ์การเว้นวรรค* formalizes a two-tier space system —
clause-internal vs sentence boundary. Modern keyboards emit a single ASCII space
either way, so the distinction surfaces as visual rhythm. Treat: short single
space within a clause; paragraph break at sentence boundaries.

Covers anti-pattern #37 (period spam — see `references/ai-tells.md`).

### Frame 4 — Closure via sentence-final particles

English doesn't need closure particles. Thai uses a small inventory of them to wrap
clauses cleanly: `ด้วย` (also/too — closes additive thoughts), `แล้ว` (completion,
transition), `ไป` (movement away/done), `อยู่` (ongoing state), `เลย` (intensification
or "right then"), `ก็แล้วกัน` (let's just leave it / decision), `อยู่ดี`
(still / nonetheless), `ต่างหาก` (contrastive correction — "actually X, not Y").

Note on `แล้ว` variants (per Olsson 2013 on Thai iamitive): `แล้ว` alone marks
completion / "by now". `X แล้ว ก็ Y` adds sequence + pacing (see Frame 6).
`เสร็จแล้ว` is the perfective-completion variant — action finished, with finality
beyond just temporal completion. Pick the form that matches whether the close
needs pure completion, sequenced flow, or finished-action force.

When AI omits these because the English source has no equivalent token, Thai
sentences feel dangling — like the writer trailed off.

- Dangling: `repo นี้ไม่ได้มากับกฎอย่างเดียว มี eval harness ผูกกับ claude และ codex`
- Closed: `repo นี้ไม่ได้มากับกฎอย่างเดียว มี eval harness ผูกกับ claude และ codex ด้วย`

Especially watch for `ไม่ได้...อย่างเดียว`, `ไม่ใช่แค่...`, `ไม่เพียงแต่...` frames —
they almost always need a closure particle to finish the implicit "also Y".

Contrastive correction frames (`ไม่ได้ X อยู่ที่/เป็น/คือ Y`) take `ต่างหาก` — Thai's
emphatic-correction particle that closes the "actually it's Y, not X" thought.

- Dangling: `ปัญหาส่วนใหญ่ไม่ได้อยู่ที่ยอดขาย อยู่ที่ต้นทุน`
- Closed: `ปัญหาส่วนใหญ่ไม่ได้อยู่ที่ยอดขาย อยู่ที่ต้นทุนต่างหาก`

### Frame 5 — Cohesion via zero anaphora and demonstratives

English needs explicit pronouns: *it / they / he / she / this / that*. Thai has three
main strategies that AI underuses:

1. **Zero anaphora** — once the topic is established, drop the subject entirely.
   Re-state only when control changes. A paragraph beginning `เราเรียนรู้จากความผิดพลาด...`
   can run several sentences before *เรา* needs to reappear.
2. **Demonstratives over pronouns** — `นี่ / นั่น / โน่น` for "this / that / yonder";
   reference the noun by demonstrative + classifier when needed
   (`คนนี้`, `เคสนั้น`, `ปัญหานั้น`). AI overuses `มัน`, `เขา`, `พวกเขา` because they
   map to English `it / he / they`.
3. **Demonstrative as inter-clause bridge** — between clauses where English would
   repeat the subject, Thai uses a demonstrative referring back to the just-stated
   fact: `ตรงนี้แหละที่...`, `นี่คือเหตุผลที่...`, `ส่วนนี้...`. Especially valuable
   for problem→solution pivots (see also Frame 7).

   - Dangling: `ของค้างก็กลายเป็นต้นทุนเงียบ ระบบนี้ช่วย...`
   - Bridged: `ของค้างก็กลายเป็นต้นทุนเงียบ ตรงนี้แหละที่ระบบช่วยได้`

- Calqued: `เราต้องเข้าใจว่าเราอยู่ในโลกที่เราสร้างขึ้นมาเอง มันมีกฎของมันเอง`
- Native: `ต้องเข้าใจว่าโลกที่เราอยู่ คือโลกที่สร้างขึ้นเอง มีกฎของตัวมันเอง`

**Caveat — zero anaphora has limits.** Aggressive subject-drop creates subjectless
robot-prose when the referent isn't recoverable from context. If a clause starts
with a connective (`เพราะ...`, `ดังนั้น...`, `ส่วน...`) and immediately presents a
verb without a topic, restore reference via a demonstrative bridge or a
topic-comment restructure rather than reaching for `มัน` (banned by anti-pattern #29).

- Robot: `เพราะรับประกัน output rate`
- Native (bridge): `เพราะแบบนี้ output rate จะคงที่`
- Native (restored topic): `algorithm นี้รับประกัน output rate`

### Frame 6 — Pacing via ก็

`ก็` is a uniquely Thai pacing particle. It marks expectation, sequence, mild
concession, and "as expected" causation. English has no direct equivalent, so AI
drops it, and Thai prose without ก็ reads choppy or robotic.

- Without ก็: `พอ traffic ขึ้น DB เริ่มอืด`
- With ก็: `พอ traffic ขึ้น DB ก็เริ่มอืด`

Common patterns: `พอ X ก็ Y`, `X แล้ว ก็ Y`, `ถ้า X ก็ Y`, `เลย...ก็...`,
`X ไม่ทัน ก็เลย Y`. Standalone `แล้ว` (without `ก็`) also bridges sequenced action
clauses where English would use no connective:

- Choppy: `ถ่ายรูปบิลจากตลาด ระบบอ่านรายการให้เอง`
- Bridged: `ถ่ายรูปบิลแล้วระบบจะอ่านรายการให้เอง`

**Sub-pattern: ก็ as topic-resumptive bridge** (formalized in Takahashi 2023 on
ก็ as a pragmatic particle). When a sentence states a topic and then offers a
comment that would otherwise feel clipped, ก็ at the start of the comment gives
the natural "as expected / belongs together" beat. AI tends to write the comment
without ก็ and produce a snap that lands wrong.

- Clipped: `ในรายการนี้ ไม่มีคอลัมนิสต์ดังคนไหน เป็นความตั้งใจ`
- Bridged: `ในรายการนี้ ไม่มีคอลัมนิสต์ดังคนไหน ก็เป็นความตั้งใจ`

Use ก็ as breath/rhythm, not as a connective replacement. Don't force it where it
doesn't fit; do allow it where Thai naturally wants the beat.

### Frame 7 — Pivots via question, demonstrative, or simple แต่

English pivots between ideas using formal connectives: *however*, *moreover*,
*on the other hand*, *furthermore*. Thai prose pivots more often via:

1. **Rhetorical question** — `แล้วถ้า X ล่ะ?`, `นั่นแปลว่ายังไง?`, `ทำไมถึงเป็นแบบนั้น?`.
2. **Demonstrative bridge** — `ตรงนี้แหละ...`, `นี่คือเหตุผลที่...` (see also Frame 5).
3. **Simple `แต่`** — replaces `อย่างไรก็ตาม` in roughly half of its English occurrences.

- AI pivot: `อย่างไรก็ตาม การใช้งานในระดับ production มีข้อจำกัด`
- Native pivot: `แต่พอเอาขึ้น production จริง ก็มีอะไรให้ปวดหัวอีก`
- Native (question pivot): `แล้วถ้าโหลดเพิ่มอีกสิบเท่าล่ะ? ตรงนี้แหละที่เริ่มน่าสนใจ`

**Special case — problem-list to solution pivot.** After listing 2–3 reader
pain-points, AI tends to dive straight into the product/solution clause without a
pivot, producing bullet-list cadence. Insert a question pivot, demonstrative bridge,
or contrastive `แต่` to mark the shift.

- Bullet-cadence: `ของหมดก็เสียยอดขาย ของค้างก็กลายเป็นต้นทุนเงียบ ระบบนี้ช่วย...`
- Pivoted (question): `ของหมดก็เสียยอดขาย ของค้างก็กลายเป็นต้นทุนเงียบ — แล้วทำไงให้คุมของได้แม่น?`
- Pivoted (demonstrative): `ของหมดก็เสียยอดขาย ของค้างก็กลายเป็นต้นทุนเงียบ ตรงนี้แหละที่ระบบนี้ช่วยได้`

Heuristic: every "however" you'd write, ask whether a question or just `แต่` would
do better. Drop one in two.

## Person-arity (apply before drafting any piece with a reader)

In any piece, identify three roles. Most critical for Marketing copy.

- **1st person — speaker**. Marketing: brand as `เรา`. Personal blog: author as
  `ผม`/`ดิฉัน`. News/reference: no first-person.
- **2nd person — addressee**. Marketing: reader as `คุณ` directly. **Never substitute
  the audience's demographic noun** (`เจ้าของร้าน`, `ผู้ใช้`, `นักลงทุน`,
  `ผู้ประกอบการ`) for `คุณ` in body copy. Demographic nouns belong in headers and
  category framing, not as the active 2nd-person referent.
- **3rd person — product, concept, third party**. Marketing: `ระบบนี้`,
  `เครื่องมือนี้`, `แอปนี้`.

- Bad (3rd-person address substitutes demographic noun):
  `เครื่องมือนี้ทำให้เจ้าของร้านเห็นภาพจริงของร้านตัวเอง`
- Good (direct 2nd-person):
  `ระบบนี้ช่วยให้คุณเห็นภาพจริงของร้านได้ทันที`

Don't mix `เรา` and `คุณ` within the same paragraph (Krungsri pattern). Body in
`เรา` when teaching a concept; advisory line shifts to `คุณ` for action. See
`references/register.md` for register-specific person-arity defaults.

## Stylistic conventions (apply on top of the frames)

Once the frames are right, these surface-level conventions fine-tune the voice.

1. **Verbs over noun forms.** Prefer `แปลหนังสือ` to `ทำการแปลหนังสือ`. Prefer
   `ระบบขยายได้` to `ระบบมีความสามารถในการขยาย`. Reserve การ- and ความ- for
   genuinely abstract topics.

2. **Particles match register, not friendliness.** ครับ/ค่ะ in body copy of
   explainers, tech docs, and marketing → NO. They belong in spoken-voice contexts:
   personal blog openings/sign-offs, quoted speakers, chat-app messaging,
   direct-to-reader social posts. See `references/register.md`.

3. **Open with the reader's situation, not a panorama.** Banned openers:
   `ในยุคปัจจุบัน...`, `ในโลกที่...`, `เป็นที่ทราบกันดีว่า...`, `ปฏิเสธไม่ได้ว่า...`.
   Replace with: a symptom the reader recognizes, a concrete fact, a rhetorical
   question, or a confession.

4. **Concrete numbers and named examples beat abstract claims.**
   `p99 ลดจาก 800ms เหลือ 120ms` beats `ประสิทธิภาพดีขึ้นอย่างมีนัยสำคัญ`.

5. **Vary sentence length deliberately.** A 6-word sentence next to a 35-word one is
   normal Thai prose. AI homogenizes around 20 words and reads as monotone. Mix.

6. **Mai-yamok (ๆ) for casual reduplication.** `เรื่อย ๆ`, `ใหม่ ๆ`, `บ่อย ๆ` —
   natural Thai signal. Don't avoid it.

## Workflow when asked to write Thai prose

1. **Identify register and voice** before writing. ASK if either is unclear. Five
   register families live in `references/register.md`:
   - **News / reference** — no first-person, no particles, active voice
   - **Explainer** — bank/tech long-form, no particles, problem-first, `เรา`/`คุณ`
     address
   - **Marketing (family)** — SaaS-SME / B2B-formal / fintech-warm / retail-tech
     sub-registers; person-arity required
   - **Personal blog / dev war-story** — first-person `ผม` *or* `ดิฉัน` per gender,
     ครับ/ค่ะ at openings and sign-offs only. **ASK gender if not stated** — don't
     silently default to `ผม`.
   - **Academic long-form** — no particles, longer sentences acceptable, synthesis
     closings

   Voice attributes (gender, brand mood, formality level) are orthogonal to
   register — pick both.

1.5. **Identify person-arity** for any piece with a reader, especially Marketing.
   1st (brand `เรา`) / 2nd (reader `คุณ` — never demographic noun) / 3rd (product).
   See Person-arity section above.

2. **Draft frame-first.** Before picking words, ask:
   - What's the topic? Is it fronted (Frame 1)?
   - Are conditions/times leading (Frame 2)?
   - Are sentences flowing without period spam (Frame 3)?
   - Do clauses close with appropriate particles (Frame 4)?
   - Is cohesion via zero anaphora + demonstratives (Frame 5)?
   - Is ก็ pacing where Thai wants the beat (Frame 6)?
   - Are pivots via question or simple `แต่`, not formal connectives (Frame 7)?

3. **Self-edit pass — scan for AI tells:**
   - Search for the forbidden phrases in `references/anti-patterns.md`.
   - Connective budget: at most one ซึ่ง, one โดย, one ดังนั้น per ~100 words.
   - Period audit: drop mid-paragraph periods.
   - Closure audit: any `ไม่ได้...อย่างเดียว` / `ไม่ใช่แค่...` needs a closure particle.
   - Sentence-length variance.
   - ครับ/ค่ะ usage matches register.
   - ถูก- passive: each instance genuinely adversative or genuinely agentless?

4. **Closing.** Don't recap. Real Thai writing ends with: a forward-looking line, a
   reframed question, a quiet handoff (`เท่านี้ก่อน`, `ลองเอาไปเล่นดู`), or just
   stops. Never `โดยสรุปแล้ว...` then re-state the body.

## When asked to edit Thai prose

Apply the same passes in reverse: hunt for frame violations and AI tells, propose
specific line edits with the *why*. See `references/examples.md` for before/after
worked examples.

## When asked to translate English to Thai

Translation is where AI fails hardest because it preserves English shape — meaning
all seven frames are at maximum risk.

Minimum checklist:

- Reorder to topic-comment (Frame 1).
- Move condition/time clauses to front (Frame 2).
- Drop English-style mid-paragraph periods (Frame 3).
- Add Thai closure particles where the English-shaped sentence dangles (Frame 4).
- Drop pronouns once topic is set; use demonstratives where English uses pronouns
  (Frame 5).
- Insert ก็ where Thai wants the beat (Frame 6).
- Convert "however / moreover" to questions or simple `แต่` (Frame 7).
- Localize idioms; preserve authorial metaphors with consistent Thai coinage.
- Don't add politeness the source doesn't have. Confident essayists stay confident
  in Thai.
- ทับศัพท์ judgment per the four-bucket guide in `references/style-rules.md`.

## References — read on demand

- `references/ai-tells.md` — mechanical Thai-correctness violations. Hard rules
  applying across registers. Consult when self-editing or when uncertain whether
  a pattern is AI-shaped.
- `references/grammar.md` — surface Thai grammar: classifiers, modal markers,
  function-word distinctions, verb-level calques. Hard rules.
- `references/craft.md` — voice / taste / register-conditional preferences. Soft
  rules with scope notes.
- `references/style-rules.md` — positive style rules, ทับศัพท์ four-bucket guide,
  translation craft rules. Consult when drafting.
- `references/register.md` — register family + voice + person-arity. Consult
  before drafting; pick register and voice first.
- `references/examples.md` — before/after worked rewrites across registers.
  Consult for pattern-matching.
- `references/audit-checklist.md` — condensed grep-able checklist for kode-thai
  audit pass.

Citation-grade backing for many rules (Iwasaki & Ingkaphirom, Smyth, Higbie &
Thinsan, Li & Thompson, Prasithrathsint, Takahashi, Olsson, Thai Discourse
Treebank, Singnoi, Royal Institute spacing manual, Marcel Barang) lives in
`corpus/curated/scholarly/<source-slug>.md` — author/year extracts with direct
rule mappings. Corpus prose is gitignored due to copyright; the index in
`corpus/README.md` lists what's available locally.

## Important: when in doubt, ask the user

If the register is ambiguous (is this for a dev blog or formal docs? is the audience
SME owners or finance pros?), ask before drafting. Wrong register is worse than
rough prose.
