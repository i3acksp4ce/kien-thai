---
name: grammar + forbidden + anti-patterns
description: Iter 06 — small files, one free win (anti-patterns is a stub redirector being shipped)
slice: skills/kien-thai/references/{grammar,forbidden-phrases,anti-patterns}.md
---

# 06 — grammar.md + forbidden-phrases.md + anti-patterns.md (4,081 tok combined)

Three short files. Mostly already efficient, but **anti-patterns.md is
a 537-token stub redirector being injected into every pass for no
reason**. Cleanest free win in the audit.

## File-by-file

### grammar.md (2,930 tok)

7 rules (#41–#44, #46, #47) covering classifiers, จะ modal,
function-word confusion, verb calques, capability modal, time-period
ใน vs ของ. Tight.

**Cut A — header dedup.** Lines 1–11 contain a 150-token preamble
about slugs vs numeric IDs that's mostly meta-tooling info ("Each
rule has a stable slug... Future cross-references should prefer..."
). The auditor doesn't need this on every pass.

Replace with 2 lines:
```
Surface Thai grammar — word/phrase level, hard rules, all registers.
```

Cut: ~120 tokens every pass.

**Cut B — drop default metadata.** Same as iter 02 Cut B for
ai-tells.md. Each rule in grammar.md has
`· mechanical · all-registers · hard` — all default for this file.

Cut: ~70 tokens (7 rules × 10 tok).

**Cut C — Singnoi/Hundius cite in #41.** Lines 37–43 spend 80 tokens
on a register-aware classifier note with cite. The classifier table
above already gives the auditor enough; the formal/conversational
nuance can compress to 1 line.

Replacement:
```
In conversational/personal-blog/explainer registers, generic `อัน` /
`ตัว` are accepted; News/Academic/B2B-formal prefer the precise
classifier.
```

Cut: ~50 tokens.

**Total grammar.md cut: ~240 tokens/pass.**

### forbidden-phrases.md (614 tok)

Already minimal. ~13 blocklist entries + critical use/mention
exemption explanation.

**No cuts.** The use/mention paragraph (~120 tok) is load-bearing —
without it, the auditor false-positives on examples.md mentions of
the patterns. iter 02 of this audit project already noted the slug
system depends on this.

### anti-patterns.md (537 tok) — **FREE WIN**

The whole file is a human-facing redirector, written when the original
`anti-patterns.md` was split into ai-tells/craft/grammar:

```
# Anti-patterns (split into focused files)

This file has been split for clarity. Rules now live in three peers...
- ai-tells.md — mechanical Thai-correctness...
- craft.md — voice/taste/register-conditional...
- grammar.md — surface Thai grammar...
- forbidden-phrases.md — string-match blocklist...

Prefer slug references over numeric IDs...
```

The bundle still ships it because `tests/lib.py:kien_thai_bundle()`
glob-matches every `references/*.md`:

```python
for ref in sorted((KIEN_THAI_DIR / "references").glob("*.md")):
    parts.append(f"\n\n## reference: {ref.name}\n\n{ref.read_text(...)}")
```

The auditor and fixer don't need a "this file has been split" note —
they're not navigating the repo, they're applying rules. The redirect
exists for git-history-spelunking humans and for IDE link resolution.

**Cut D — exclude anti-patterns.md from bundle.**

Two implementation options:
1. Special-case the glob: `if ref.name == "anti-patterns.md": continue`
2. Rename to `_README.md` (or move to `references/README.md`) — glob
   doesn't match leading-underscore or README files in many
   conventions. Cleaner long-term.

Cut: **~537 tokens every pass.** Codex tech-doc 5-pass: 11 × 537 =
~5,900 tokens.

This is the cleanest cut in the entire audit — pure dead weight, zero
behavior risk.

## Cumulative impact (this slice)

| File           | Cut           | Tokens/pass |
| -------------- | ------------- | ----------: |
| grammar.md     | A + B + C     |         240 |
| forbidden      | (none)        |           0 |
| anti-patterns  | D (exclude)   |         537 |
| **Σ**          |               |     **777** |

Codex tech-doc 5-pass: ~8,500 tokens.

## Risks

- **Cut D (anti-patterns exclusion)**: confirm the consistency test
  (`tests/test_skill_consistency.py`) doesn't reference
  anti-patterns.md as a source of cross-ref validation. If it does,
  preserve the file on disk but exclude from bundle (option 1 above).
  If only forward-references are validated, rename is fine.
- **Cut A (grammar header)**: the slug-vs-numeric note may be useful
  on the *first* invocation when the auditor encounters the rule
  format. After that it's dead weight. Trade-off accepted; auditor
  gets format primer from SKILL.md.

## Decisions deferred

- Whether to apply Cut B (default-metadata drop) consistently across
  *all* rule files at once via a build-time preprocessor in
  `kien_thai_bundle()` rather than editing each file. Preprocessor
  approach: keep human-readable metadata in source, strip on inject.
  Adds complexity; defer until aggregate cut justifies the engineering.
