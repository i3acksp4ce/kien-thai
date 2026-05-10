---
name: cost map
description: Iteration 00 — full token-cost survey + iteration plan
slice: repo-wide
---

# 00 — token-cost map

Baseline survey before per-slice analysis. Numbers are chars (Unicode codepoints,
`wc -m`), bytes (`wc -c`, dominated by Thai 3-byte UTF-8), and a rough token
estimate using **0.55 tokens/char** for Thai-heavy mixed content (Claude/codex
tokenizers split Thai into 1–3 codepoint subwords; this rate is conservative
mid-range).

## Bundle composition (injected on every audit + fix pass)

| File                    | Chars  | Bytes  | ~Tokens |
| ----------------------- | -----: | -----: | ------: |
| SKILL.md                | 18,597 | 23,194 |  10,228 |
| references/ai-tells.md  | 14,415 | 21,357 |   7,928 |
| references/register.md  | 15,089 | 17,881 |   8,299 |
| references/style-rules  |  9,987 | 12,669 |   5,493 |
| references/examples.md  |  7,027 | 15,831 |   3,865 |
| references/grammar.md   |  5,327 |  6,878 |   2,930 |
| references/craft.md     |  4,949 |  6,435 |   2,722 |
| references/forbidden    |  1,116 |  1,592 |     614 |
| references/anti-pat.md  |    976 |    992 |     537 |
| **Bundle total**        | **77,483** | **106,829** | **~42,605** |

Audit/fix prompt overhead adds ~3.5KB framing + Thai prose body (~1–3KB).
Observed `pass-0-prompt.txt` = 107.5KB, `pass-1-audit-prompt.txt` = 111KB —
matches.

## Per-run token cost (rough, no caching)

| Cell                       | Invocations | Bundle re-sends | ~Input tokens |
| -------------------------- | ----------: | --------------: | ------------: |
| baseline (any)             |           1 |               0 |          ~150 |
| with_skill best case       |           2 |               2 |       ~85,000 |
| with_skill 2-pass loop     |           4 |               4 |      ~170,000 |
| **codex tech-doc 5-pass**  |          11 |              11 |     **~470,000** |

Anthropic prompt caching (5-min TTL, ≥1024 tokens) recovers most of this
across passes since the bundle is identical pass-to-pass. **But codex doesn't
use Anthropic caching** — each pass is a full uncached send. Codex worst case
is the real bill.

## Where the fat is

Top 4 files = 76% of bundle (SKILL + ai-tells + register + style-rules).
Cuts elsewhere are rounding error.

Looking at the file sizes vs purpose:

- **SKILL.md (10K tokens)** — almost certainly inlines content also expanded
  in references. Likely contains Frame definitions twice (overview in SKILL,
  details in references). High-priority audit target.
- **ai-tells.md (8K tokens)** — ~29 rules per resume notes. ~270 tokens/rule.
  If rules average 5–10 lines of prose + example, this is fat-prose territory.
- **register.md (8K tokens)** — 4 marketing sub-registers + explainer. Likely
  redundant scaffolding across registers.
- **examples.md (4K tokens, 16KB bytes)** — Thai prose ratio is highest here
  (16KB bytes / 7K chars = 2.3 bytes/char, near pure Thai). Before/after
  pairs probably long.
- **style-rules.md (5.5K tokens)** — moderate.

## Architectural cuts (the big wins)

These dwarf any per-file editing:

### A. Two-tier injection

Currently the full ~43K-token bundle goes into every pass. Audit and fix
passes don't need *all* rules — they need the cited rules + a reference of
slug → rule.

Proposal:
- **Pass-0 (initial draft)**: full bundle, as today.
- **Pass-N audit**: full bundle (auditor must scan everything).
- **Pass-N fix**: only the rules cited in `pass-N-audit.md` + a slim
  "rule index" (slug → 1-line summary, ~50 tokens/rule × 50 rules ≈ 2.5K
  tokens). Estimated cut: 43K → 5–8K tokens per fix pass.

For codex tech-doc 5-pass: saves ~5 × 35K = **~175K tokens per failure case**.

Risk: fix pass loses context for adjacent rules. Mitigation: include the
audit-cited rule's siblings in the same file (cheap — file is ~3K tokens).

### B. SKILL/references deduplication

If SKILL.md inlines content that references files re-expand, fold one
direction. Likely cut: 30–50% of SKILL.md = 3–5K tokens off every pass.

### C. Prompt caching for codex

Codex uses OpenAI's API. OpenAI added prompt caching in 2024 (50% discount on
cached tokens, automatic for prompts ≥1024 tokens with stable prefix). The
bundle is identical across passes — should cache. Verify codex CLI passes
the cache-eligible prefix; if not, reorder prompt so bundle is the prefix.

### D. Audit-only / fix-only files

Some references are auditor-relevant only (forbidden-phrases.md is a
pre-check), others are author-relevant (style-rules.md, examples.md). Split:

- **Author bundle** (pass-0 + fix passes): SKILL + style-rules + examples +
  register.
- **Auditor bundle** (audit passes only): SKILL + ai-tells + grammar +
  craft + forbidden-phrases + anti-patterns.

Eyeballing files into buckets, this halves each pass's bundle. Concrete
estimate after slice-level inspection.

## Iteration plan

| #  | Slice                         | Why first                                |
| -: | ----------------------------- | ---------------------------------------- |
| 01 | SKILL.md                      | Largest single file; suspect duplication |
| 02 | ai-tells.md                   | 29 rules — measure rule-density          |
| 03 | register.md                   | Cross-register redundancy suspected      |
| 04 | examples.md                   | Pure Thai prose — compression vs cuts    |
| 05 | style-rules.md + craft.md     | Audit overlap                            |
| 06 | grammar.md + forbidden + a-p  | Smallest combined                        |
| 07 | conftest.py audit/fix prompts | Framing overhead + caching opportunity   |
| 08 | Two-tier injection design     | Synthesis of 01–07                       |
| 09 | Auditor/author split design   | Synthesis of 01–07                       |

Stop conditions: any iteration whose proposed cut is <500 tokens or <2%
of bundle gets shelved as low-value. Loop ends when no high-value cuts
remain.

## What this analysis does NOT touch

- Workspace artifact sizes (prompt files, audit traces) — disk-only,
  not in any prompt path. Out of scope.
- pythainlp word_tokenize at wrap time — runtime only, not token cost.
- Eval prompts in `evals/evals.json` — already minimal (1KB total).
