# Voice and craft preferences (style)

Subjective style/voice preferences distinct from the mechanical Thai-correctness
rules in `ai-tells.md`. These are taste calls — apply them to lift prose quality,
but a violation here doesn't make a piece "AI-shaped" the way an `ai-tells.md`
violation does. Many are register-conditional (see scope notes inline; cross-ref
`register.md`).

These rules originated in observation of skilled Thai writers (bank long-form,
tech blogs, translation craft) and represent shared craft conventions, not Thai
grammar rules.

## Headlines and openers

### `cliche-headline` *(craft · all-registers · soft)*

- **Bad**: `ทุกสิ่งที่คุณต้องรู้เกี่ยวกับ X`
- **Good**: question pair (`X คืออะไร / Y ได้จริงไหม`) / specific pain frame /
  numbered angle (`5 เรื่องที่...`)

Note: this is closer to "effective writing" advice than a Thai-specific rule.
Listed here because Thai SaaS/SEO content homogenizes around these clichés just
as English does.

### `definition-first-seo` *(craft · marketing · soft)*

`X คือ ...` as the first sentence is the SEO-blog default — homogenizes openings
across SaaS, fintech, and accounting tutorials. Replace with reader-symptom or
question-hook unless the term genuinely needs defining for the audience.

- **Bad**: `ภาษีหัก ณ ที่จ่าย คือ ภาษีที่ผู้จ่ายเงินต้องหักไว้...`
- **Good (symptom)**: `เคยจ่ายค่าจ้างแล้วโดนถามจากบัญชีว่าหัก ณ ที่จ่ายแล้วรึยังไหม?`
- **Good (question)**: `ถ้าคุณเคยจ่ายเงินค่าบริการให้บริษัทอื่น คุณต้องหักภาษีไว้ — แล้วทราบไหมว่าต้องหักเท่าไหร่?`

Reserve `X คือ ...` for reference docs and explainers where the definition really
is the goal, not for marketing or conversion-oriented copy.

## Closings

### `cta-bang` *(craft · scoped · soft)*

- **Bad**: `รีบสมัครเลย!` / `อย่ารอช้า!`
- **Good (advisory)**: `กู้เท่าที่จำเป็นและชำระคืนไหว` / `ผู้ลงทุนควรทำความเข้าใจก่อนตัดสินใจ`

**Scope**: full strictness in Explainer, Marketing/B2B-formal, Marketing/fintech-warm,
News, Academic. **Softened in Marketing/SaaS-SME and Marketing/retail-tech** — a
single `!` at hook or CTA is fine, but the rest of the close should still stay
advisory rather than imperative-with-bang.

The rule pairs the imperative-with-bang form (Bad) against Krungsri/SCB advisory
disclaimers (Good). The Good examples show *what bank-explainer copy uses
instead* — they're not direct rephrasings of the Bad.

## Intensifiers and lists

### `empty-intensifier` *(craft · all-registers · soft)*

Style preference, not a correctness rule. Real Thai prose substitutes a number,
named example, or Thai-native intensification rather than `อย่าง + abstract noun`.

- **Bad**: `อย่างมหาศาล / อย่างน่าทึ่ง / อย่างไม่น่าเชื่อ / อย่างมีประสิทธิภาพ / อย่างมาก`
- **Good**: substitute a number, a named example, or `ยิ่ง X เท่าไหร่ ยิ่ง Y เท่านั้น`.

### `generic-reassurance` *(craft · scoped · soft)*

- **Bad**: `ไม่ต้องกังวล เป็นเรื่องที่เข้าใจได้`
- **Good**: specifics — what the reader concretely should do next.

**Scope**: full strictness in Explainer, Marketing/B2B-formal, Marketing/fintech-warm,
News, Academic. **Softened in Marketing/SaaS-SME** — a brief reassurance at hook or
pivot is acceptable when paired with a concrete next-step
(`ไม่ต้องกลัวเริ่มไม่ทัน — ลองฟรี 30 วันได้เลย`).

## See also

Sentence shape and bullet/prose balance live as positive rules in
`style-rules.md` — `mixed-sentence-length`, `prose-before-bullets`,
`uneven-list`, `no-recap-close`. craft.md only houses the soft AI-signature
patterns that don't have a clean positive twin (cliché headlines, definition-
first SEO opener, scoped CTA/reassurance bans, empty intensifiers).
