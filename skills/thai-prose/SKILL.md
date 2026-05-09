---
name: thai-prose
description: Write Thai-language prose (technical documentation, marketing copy, explainers, blog posts) that reads like a real Thai writer — not generic AI output. Counters training-data skew toward over-formal, over-polite, calqued Thai. Use this skill whenever the user asks for Thai writing, asks to translate English content into Thai, or asks to edit/rewrite existing Thai prose, even if they don't explicitly say "good prose." Also use when the user is in a Thai-language conversation and asks for any non-trivial prose output (a paragraph, section, blog post, landing page, doc page, README in Thai, email, announcement). The default Thai output without this skill is mechanically polite, connective-spammed, and calque-shaped — this skill fixes that.
---

# thai-prose

## Why this skill exists

Generic AI-produced Thai has tells. Native readers feel them as friction —
re-reading sentences, skimming, abandoning. The biggest tells:

- **Connective spam**: ซึ่ง / โดย / ทั้งนี้ / อีกทั้ง / นอกจากนี้ / อย่างไรก็ตาม /
  ดังนั้น in every other clause.
- **Calqued English syntax**: ถูก-passive on actions with no real agent,
  "การที่...นั้น...", long subordinate chains glued by ซึ่ง, "หนึ่งใน...ที่...ที่สุด"
  patterns.
- **Bureaucratic padding**: ทำการ+verb, มีความ+adj, การ-nominalization of every verb.
- **Wrong register default**: ครับ/ค่ะ on every sentence, ท่าน as default address,
  "ในยุคปัจจุบัน..." openers.
- **Empty intensifiers and tricolons**: "อย่างมาก", "อย่างมีประสิทธิภาพ",
  "รวดเร็ว ปลอดภัย และมีประสิทธิภาพ".

Real Thai writers don't write like this. The goal: produce Thai that a Thai reader can
read at speed, with a distinct human voice appropriate to register.

## Core philosophy

1. **Drop the connective. Use a full stop.** Most ซึ่ง / โดย / อย่างไรก็ตาม can be
   replaced by a period. Test every connective: would a Thai reader notice it missing?
   If no, delete.

2. **Topicalize, don't passivize.** Thai prefers `topic → comment` to English's
   `subject → verb → object`. When you would calque a passive ("X is done by Y"),
   front the patient as topic and use active voice: "ข้อมูลพวกนี้ระบบจะ process"
   beats "ข้อมูลพวกนี้จะถูก process โดยระบบ".

3. **Verbs over nouns.** Prefer `แปลหนังสือ` to `ทำการแปลหนังสือ`. Prefer `ระบบขยายได้`
   to `ระบบมีความสามารถในการขยาย`. Reserve การ- and ความ- for genuinely abstract
   topics.

4. **Particles match register, not friendliness.** ครับ/ค่ะ in body copy of explainers,
   tech docs, and marketing → NO. They belong in spoken-voice contexts: personal blog
   openings/sign-offs, quoted speakers, chat-app messaging, direct-to-reader social
   posts. See `references/register.md`.

5. **Open with the reader's situation, not a panorama.** Banned openers:
   "ในยุคปัจจุบัน...", "ในโลกที่...", "เป็นที่ทราบกันดีว่า...", "ปฏิเสธไม่ได้ว่า...".
   Replace with: a symptom the reader recognizes, a concrete fact, a rhetorical
   question, or a confession.

6. **Concrete numbers and named examples beat abstract claims.**
   `p99 ลดจาก 800ms เหลือ 120ms` beats `ประสิทธิภาพดีขึ้นอย่างมีนัยสำคัญ`.
   `งบ 4 ส่วน: ใช้/ลงทุน/ออม/ฉุกเฉิน` beats `การจัดสรรเงินอย่างเหมาะสม`.

7. **Vary sentence length deliberately.** A 6-word sentence next to a 35-word one is
   normal Thai prose. AI homogenizes around 20 words and reads as monotone. Mix.

8. **Mai-yamok (ๆ) for casual reduplication.** `เรื่อย ๆ`, `ใหม่ ๆ`, `บ่อย ๆ` — natural
   Thai signal. Don't avoid it.

## Workflow when asked to write Thai prose

1. **Identify register** before writing. Ask if unclear. Four main ones live in
   `references/register.md`:
   - **News / reference** — no first-person, no particles, active voice,
     formal-neutral
   - **Explainer / bank long-form / tech doc** — no particles, problem-first,
     "เรา"/"คุณ" address, prose+bullets
   - **Personal blog / dev war-story** — first-person ผม, conversational, ครับ at
     openings and sign-offs
   - **Academic long-form** — no particles, longer sentences acceptable, synthesis
     closings

2. **Draft.** Apply the 8 core principles above. Specifically:
   - Budget: at most one ซึ่ง, one โดย, one ดังนั้น per ~100 words.
   - Drop pronominal subjects after the topic is established. Re-state only when
     control changes.
   - For tech terms: see the four-bucket ทับศัพท์ guide in `references/style-rules.md`.

3. **Self-edit pass — scan for AI tells:**
   - Search for the forbidden phrases listed in `references/anti-patterns.md`.
   - Count connectives per paragraph. If &gt; 2 of any one kind, rewrite.
   - Check sentence-length variance. If every sentence is ~20 words, break some.
   - Check ครับ/ค่ะ usage against register.
   - Check ถูก- passive: each instance should be genuinely adversative or genuinely
     agentless. Otherwise active-voice.

4. **Closing.** Don't recap. Real Thai writing ends with: a forward-looking line, a
   reframed question, a quiet handoff (`เท่านี้ก่อน`, `ลองเอาไปเล่นดู`), or just stops.
   Never `โดยสรุปแล้ว...` then re-state the body.

## When asked to edit Thai prose

Apply the same passes in reverse: hunt for AI tells, propose specific line edits with
the *why*. See `references/examples.md` for before/after worked examples.

## When asked to translate English to Thai

Translation is where AI fails hardest because it preserves English shape. The minimum:

- Reorder to topic-comment.
- Drop pronouns once topic is set.
- Break long English sentences at conceptual seams (often 2–3 Thai sentences per
  English one).
- Localize idioms; preserve authorial metaphors with consistent Thai coinage.
- Don't add politeness the source doesn't have. Confident essayists stay confident in
  Thai.
- ทับศัพท์ judgment per the four-bucket guide.

Full translation craft rules in `references/style-rules.md` (section: translation).

## References — read on demand

- `references/anti-patterns.md` — full catalog of AI tells with bad/good Thai examples.
  Consult when self-editing or when uncertain whether a pattern is AI-shaped.
- `references/style-rules.md` — positive rules, ทับศัพท์ four-bucket guide, translation
  craft rules. Consult when drafting.
- `references/register.md` — the four registers in detail, particle/pronoun/heading
  conventions per register. Consult before drafting.
- `references/examples.md` — before/after worked rewrites across registers. Consult for
  pattern-matching.

## Important: when in doubt, ask the user

If the register is ambiguous (is this for a dev blog or formal docs? is the audience
SME owners or finance pros?), ask before drafting. Wrong register is worse than rough
prose.
