---
name: prompts and caching
description: Iter 07 — audit/fix prompt templates + prompt-caching reorder
slice: tests/generate/conftest.py + invocation strategy
---

# 07 — audit/fix prompt templates + caching strategy

The harness's prompt templates in `tests/generate/conftest.py` are
small (each <100 tok of framing). The big lever here isn't the
templates — it's **prompt ordering for cache hits**.

## Current prompt structure

`_audit_prompt(prose, bundle, register)` (lines 58–73 of conftest.py):

```
ใช้แนวทางการเขียนต่อไปนี้:

<skill>
{bundle}                       <- 42K tokens, identical pass-to-pass
</skill>

prose นี้เป็น register `{register}` — ใช้ scope ตาม `register.md` ...

งาน: อ่าน prose ทั้งหมดให้จบก่อน แล้วค่อย flag issues ...

<prose>
{prose}                        <- ~500 tok, changes every pass
</prose>
```

`_fix_prompt(prose, audit, bundle, register)` (lines 76–86):

```
ใช้แนวทางการเขียนต่อไปนี้:

<skill>
{bundle}                       <- 42K tokens, identical
</skill>

prose นี้เป็น register `{register}` — ...

issue ที่ต้องแก้:

{audit}                        <- ~500 tok, changes every pass

prose ปัจจุบัน:

<prose>
{prose}                        <- ~500 tok, changes every pass
</prose>

งาน: แก้ prose ตาม issue ข้างบน ...
```

The skill bundle is the prefix — good for caching. But two issues:

### Issue 1 — register tag inside the prefix

Line 62–63 inserts the register name (`prose นี้เป็น register
\`{register}\` ...`) **after** the bundle but the bundle itself is
already cache-eligible. With the iter 03 + 04 register-scoped bundles,
the bundle text becomes register-dependent, which **changes the cache
prefix** per-register.

Within a single eval run, all passes on one cell share the same
register, so caching within the cell still works. Cross-cell caching
(reuse claude/tech-doc bundle when running claude/marketing) **breaks**
because the register-scoped bundles differ.

Mitigation: order independent of register prefixed first.
```
<rules-core>
  SKILL.md (without register-specific bits)
  ai-tells.md
  grammar.md
  craft.md (rules only, scope notes inline)
  style-rules.md
  forbidden-phrases.md
</rules-core>
<register>
  active register block(s)
  matching example(s)
</register>
<task-prose>
  ...
</task-prose>
```

The `<rules-core>` chunk becomes ~30K tok and is identical across
*every* eval cell on the same backend. Cache hits across all cells
within the 5-min TTL window.

### Issue 2 — codex prompt caching

Codex (OpenAI) prompt caching:
- Automatic for prompts ≥1024 tokens with stable prefix.
- 50% discount on cached tokens.
- Verify codex CLI passes the prompt as a single user-message turn so
  the prefix stabilizes.

Currently `_invoke()` calls `codex exec <prompt>` as one CLI arg. The
codex CLI's behavior on caching depends on whether it sends as a
single message or fragments. **Action: instrument one run with
`codex exec --verbose` (or whatever the cache-info flag is) and
confirm the bundle hits cache pass-to-pass.**

If codex doesn't cache the bundle automatically, two options:
- (a) Use the OpenAI Responses API directly (skip the CLI), structure
  the bundle as a system prompt; cache hits become explicit.
- (b) Concatenate eval cells per-backend so the same process runs
  multiple cells, increasing chance of cache reuse.

Cost estimate (best case, with caching working):
- Codex tech-doc 5-pass without cache: 11 × 42K = 462K input tokens.
- Same with cache after pass-0: ~42K + 10 × ~500 = 47K uncached + the
  rest cached at 50% = effective ~256K equivalent tokens.
- **~45% reduction at the API layer** without touching the bundle at all.

### Issue 3 — prose echo in fix prompt

`_fix_prompt` includes the *current prose* and the *audit issues*. For
a 5-pass case, by pass-5 the prose has been edited 4 times — but the
prompt still ships the bundle in full each pass. Caching helps, but a
more aggressive design:

**Cut A — fix-pass slim bundle (deferred, design preview).** As
flagged in 00-cost-map.md, fix passes don't need the full rule set —
just the cited rules + a registry index. Implementation in iter 08.

## Concrete cuts

### Cut A — reorder bundle for cross-cell caching
**No content change**, pure rearrangement. Move register-specific
content (register.md active block, examples.md active example) to
*after* the rules-core. Bundle becomes:

1. SKILL.md (with stylistic-conventions section moved to style-rules,
   per iter 01 Cut F / iter 05 Cut A — already a register-independent
   doc).
2. references/ai-tells.md, grammar.md, craft.md, style-rules.md,
   forbidden-phrases.md (rules-core, register-independent).
3. references/register.md (slim index + active block; iter 03 Cut A).
4. references/examples.md (active example; iter 04 Cut A).
5. Per-pass content (register tag annotation, prose, audit text).

Net effect: rules-core (~30K tok after iter-01–06 cuts) caches across
all cells on a backend. Bundle "tail" (register-specific) recomputes
per cell but is small (~3.6K tok per iter 04's combined number).

Token cost reduction (claude side, with caching):
- First cell on backend: full bundle send (~33K tok cost).
- Subsequent cells: 30K cached + ~3.6K uncached tail.
- 4 cells per backend → roughly 33K + 3 × 3.6K ≈ 44K vs. 4 × 33K = 132K.
- **~67% reduction at the API layer cross-cell.**

### Cut B — drop `register.md` from prompt-prefix advisory text
**Tiny.** Lines 62–63 say `prose นี้เป็น register \`{register}\` —
ใช้ scope ตาม \`register.md\` (โดยเฉพาะ craft rules ที่มี
register-scoped exemption)`. Once register-scoping (iter 03) is in,
this advisory becomes redundant — the bundle only contains the active
register, so "use scope per register.md" is implicit.

Cut: ~30 tokens × 11 passes = 330 tokens on bad case.

### Cut C — single-line task description
**Tiny.** The current task text:
```
งาน: อ่าน prose ทั้งหมดให้จบก่อน แล้วค่อย flag issues — อย่าสแกนทีละบรรทัด.
Pre-check: scan `forbidden-phrases.md` blocklist กับ prose ...
จากนั้น audit ตามกฎใน skill เต็มชุด. สำหรับทุก issue ให้ cite ด้วย
slug ก่อน ...
```

~120 tokens of audit instructions. Most of this is auditor-priming
that should live in the **bundle** (e.g., a top-of-SKILL.md "audit
protocol" section) and be cached. Move:

- "อ่าน prose ทั้งหมดให้จบก่อน" → SKILL.md (or kode-thai protocol
  section already says this — just point at it).
- "Pre-check: scan forbidden-phrases" → forbidden-phrases.md preamble
  (already says this).
- "Cite with slug first" → SKILL.md citation-format section.

Then `_audit_prompt` becomes:
```
{bundle}

<task>register: {register}; audit prose; if clean reply CLEAN only.</task>

<prose>{prose}</prose>
```

Per-pass framing drops from ~150 tok to ~30 tok. Saves ~120 tok per
audit pass. But the bundle gains a one-time ~120 tok of moved content.
**Net per-cell: zero. Net cross-cell: bundle caches, framing doesn't
— modest win.**

### Cut D — measure first
Don't implement cache-friendly reordering blind. **Action: run a
single-cell instrumented eval** with `usage` logging on both backends
and confirm:
- Anthropic: cache_creation_input_tokens / cache_read_input_tokens
  values per pass. Expect pass-0 = creation, pass-1+ = read.
- OpenAI: prompt cache hit count from response metadata.

Instrument by adding `--print-stats` or equivalent flag in
`BACKENDS[backend]`, capture stderr, append to meta.json.

Without measurement, the cache wins above are estimates. Measurement
is a half-day task, low risk, high information value.

## Cumulative impact (this slice)

| Cut | Cost reduction          | Type                     |
| :-: | ----------------------- | ------------------------ |
|  A  | ~67% cross-cell          | API layer, no token cut  |
|  B  | ~30 tok/pass            | Per-pass framing         |
|  C  | ~120 tok/pass           | Per-pass framing (moves) |
|  D  | (instrumentation)       | Validates A/B/C          |

The **layered/cached** strategy is where this slice's biggest leverage
lives — it can deliver ~45–67% API-cost reduction *without* cutting
any rule content. Stacks multiplicatively with iter 03 + 04 register
scoping (which cuts the per-pass bundle size; this cuts the per-pass
*billed* size).

## Risks

- **Cut A — backend caching parity**: Anthropic and OpenAI cache
  semantics differ; Cut A's reorder may benefit one and not the other.
  Measure (Cut D) before committing.
- **Cut C — moved instructions get lost in long bundle**: when audit
  protocol moves to SKILL.md, ensure it stays prominent (early
  section, clearly labeled). Otherwise the auditor may apply it
  weakly. Test in eval before rolling out.

## Decisions deferred

- Whether to use the Claude API directly instead of `claude
  --disable-slash-commands -p`. Direct API gives explicit cache
  control via `cache_control: {"type": "ephemeral"}` blocks; CLI
  caching is automatic but opaque. Direct API also unlocks the
  fix-pass slim bundle (Cut A from 00-cost-map). **Likely worth
  doing post-iter-08 design.**
- Whether to consolidate prompt templates into a `prompts/` directory
  rather than inline string concatenation in conftest.py. Pure
  hygiene, not token-relevant.
