# Resuming the corpus research agent

If the background research agent (spawned from a prior session) was interrupted
before completing, here's how to pick up where it left off without redoing work.

## State of the world

The corpus directory IS the state. Every file under `corpus/curated/` and
`corpus/raw/` is durable, persisted work. The original agent prompt is in this
file (see "Original agent task" below) so it can be re-issued verbatim.

There is no progress file separate from the filesystem — each curated entry is
its own checkpoint.

## How to resume

1. Inventory existing work:

   ```sh
   find corpus/curated -name '*.md' | sort
   find corpus/raw -name '*.md' | sort
   ```

   These are the sources already done. Pull `source_url` from each curated
   entry's frontmatter to get the canonical list of completed URLs.

2. Spawn a new research agent (general-purpose, background) with the original
   task prompt PLUS a leading instruction:

   > Before doing anything, list every file under `corpus/curated/` and read
   > each one's `source_url` frontmatter field. Treat those URLs as already
   > done. Skip them. Resume work on categories with fewer than 5–10 entries
   > and on URLs not yet covered. Do not re-fetch or re-curate any
   > already-covered source.

3. The new agent should produce a brief delta report at the end: which
   categories needed more samples, which URLs were added in this resumption
   pass, any sources that failed both attempts.

## When to call it complete

A category is "done enough" when it has 5–10 representative samples covering
the voice spectrum claimed in `corpus/README.md`. If a category falls short
after two scour attempts, document the shortfall in the README rather than
padding with mediocre samples.

## Original agent task

The full task prompt the original agent was given is reproduced below verbatim
so it can be re-issued without reconstructing it.

---

You are building a Thai-prose research corpus for the kien-thai skill at
`/Users/chakrit/Documents/chakrit/เขียนไทย`. The corpus directory tree
(`corpus/curated/<category>/`, `corpus/raw/<category>/`) and `corpus/README.md`
already exist — read those first, plus `CLAUDE.md` and
`skills/kien-thai/SKILL.md`, before doing anything.

### Why this corpus exists

Every rule in `skills/kien-thai/` must be traceable to real Thai prose
evidence. The current skill's locked source decisions excluded chatty/marketing
voices, but the eval prompts target SaaS/SME marketing — that's an internal
contradiction we're fixing. Your job is to gather representative samples
across all 8 categories so the skill can be re-derived against a real corpus.

### Categories and target sources

For each category, find 5–10 representative samples. Don't pad with mediocre
ones; if a category yields fewer, document why.

1. **marketing/saas-sme** — Thai SaaS for SMEs (warm-direct voice, addresses
   non-tech business owners with `คุณ`)
   FoodStory, Page365, Wongnai for businesses, Hungry Hub, OmiseGO,
   Buzzebees, Loga, PEAK Account, FlowAccount.

2. **marketing/b2b-formal** — enterprise/B2B Thai (advisory authority, formal)
   Bluebik, Wisesight Insights, AWS Thailand blog (Thai posts), Microsoft
   Azure Thai, Krungsri B2B, SCB Business.

3. **marketing/fintech-warm** — newer Thai consumer fintech (warm-pro)
   Make by KBank, K PLUS, Robinhood (Thai stock app), Ascend Money /
   TrueMoney, KKP, Bluebik finance, Lightnet.

4. **marketing/retail-tech** — vertical SaaS for SMBs (practical,
   instructional)
   Lazada Seller Center education, Shopee Seller education, Flash Express
   merchant, Lalamove merchant, Grab Merchant, Kerry Express merchant.

5. **tech-writing** — Thai dev/tech blogs (first-person war-story, explainer)
   tpbabparn.medium.com, somkiat.cc, Nutta, rath.asia, Medium Thailand dev
   community, Blognone op-eds.

6. **bank-longform** — bank explainer (educational advisory, zero body
   particles)
   Krungsri The COACH, ttb fin tips, SCB Stories & Tips, KBank The Wisdom,
   BBL knowledge, Krung Thai.

7. **newspaper-feature** — Thai long-form features (literary analytical)
   The 101 World long-form, The MATTER deep features, WAY magazine, Reporter,
   BrandThink (long-form only, not listicles).

8. **translation** — skilled non-fiction Thai translations (confident
   essayist)
   Bookscape / openworlds, สฤณี อาชวานันทกุล (Salaree), salt publishing.

### Per-entry workflow

For each source you pick:

1. WebFetch the page. If unfetchable / JS-rendered / paywalled — note in
   final report and move on.
2. Strip nav, footer, ads, comments, related-posts, social share buttons.
   Keep just the article body prose. Save to
   `corpus/raw/<category>/<source-slug>.md`.
3. Pick 1–3 representative paragraphs (or 2–4 for long-form) — the part that
   best shows the voice. Save to `corpus/curated/<category>/<source-slug>.md`
   with frontmatter:

   ```markdown
   ---
   source_url: https://...
   retrieved: 2026-05-10
   register: <category>
   voice: <short voice descriptor>
   notes: <particles, connectives, person-arity, cadence signals>
   ---
   [prose verbatim]
   ```

The `notes` field is the most valuable part — call out specific signals: how
does this sample handle person-arity, what closure particles appear, what's
the connective density, does it use ครับ/ค่ะ in body, what register-tells
distinguish it.

Slug naming: `<source>-<topic-or-page-slug>.md`. Lowercase, hyphens.
e.g. `foodstory-pricing.md`, `krungsri-coach-emergency-fund.md`.

### Quality criteria

- Excludes (per CLAUDE.md): celebrity columnists, FMCG/insurance ad
  sensationalism, retail flash-sale copy, translated-from-English SaaS
  landing pages (likely calqued).
- Each sample must be representative of its category's claimed voice. If you
  find a "marketing/saas-sme" page that's actually written in B2B-formal
  voice, classify it correctly or skip.
- Don't include comment-section content, only authored prose.

### Deliverables

When done, return a summary:
- Count per category, sample list with one-line voice descriptors
- Sources tried that didn't yield (unfetchable / wrong voice / paywalled)
- Cross-category patterns you noticed
- Recommendations: gaps in coverage, categories that need more depth

Update `corpus/README.md` with a curation index — one line per entry.

### Time / scope

Aim for thorough coverage but stop at 5–10 entries per category. Total
target: 40–80 samples. If a site blocks scraping, move on — don't burn time
fighting infrastructure.

Today's date when the original task was issued: 2026-05-10. The user is a
native Thai speaker building this skill open-source. Be honest about what
worked and what didn't.
