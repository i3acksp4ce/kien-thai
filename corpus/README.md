# corpus

Thai-prose source material backing the rules in `skills/kien-thai/`. Every rule
in the skill should be traceable to a sample here — "rules don't get added on
vibes" (CLAUDE.md).

## Layout

```
corpus/
├── curated/                 # 1–4 paragraph hand-picked snippets
│   └── <category>/<source-slug>.md
└── raw/                     # full article body, HTML/nav/ads stripped
    └── <category>/<source-slug>.md
```

`curated/` files are the study samples — short enough to read at a glance,
classified by register and voice. `raw/` retains more of the article in case
later analysis needs context the snippet drops.

## Categories

| Path                      | Voice                                    |
| ------------------------- | ---------------------------------------- |
| `marketing/saas-sme/`     | warm-direct, SaaS landing for SMB owners |
| `marketing/b2b-formal/`   | advisory authority, enterprise/B2B       |
| `marketing/fintech-warm/` | warm-pro, consumer fintech               |
| `marketing/retail-tech/`  | practical-direct, merchant tooling       |
| `tech-writing/`           | first-person dev war-story / explainer   |
| `bank-longform/`          | educational advisory, no body particles  |
| `newspaper-feature/`      | literary analytical long-form            |
| `translation/`            | confident essayist, hybrid vocabulary    |

## Per-entry frontmatter

```markdown
---
source_url: https://...
retrieved: 2026-05-10
register: marketing/saas-sme
voice: warm-direct
notes: คุณ throughout, ! at hook, no body particles
---
[prose verbatim]
```

`notes` calls out the voice/register signals that justified inclusion — what
particles, connectives, cadence, person-arity choices the sample demonstrates.

## Out of scope

Per CLAUDE.md locked decisions: no celebrity columnists, no FMCG/insurance ad
sensationalism, no retail flash-sale copy, no translated foreign SaaS landing
pages (likely calqued).
