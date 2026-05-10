# PRODIGY9 Coding School

This project's AI coding environment is managed by [ACE](https://github.com/ace-rs/ace).
Run `ace` to start a coding session. Run `ace setup` if not yet configured.

Skills and conventions are provided by the **PRODIGY9 Coding School** school and are
symlinked into `.claude/skills/`. Skill edits go through symlinks into the school clone
— propose changes back to the school repo when ready. Run `ace config` or `ace paths`
to debug configuration issues.

## Project: kien-thai — what the skill teaches

A skills repo (open-source target) teaching Claude to write Thai prose that:

1. Reads as little like generic AI output as possible.
2. Has a distinct, believably human voice.
3. Is easy to read for native Thai readers (no brain damage).
4. Counters training-data skew toward over-formal / over-polite Thai.

Two skills:

- `skills/kien-thai/` — content rules: 7 frames + anti-patterns + style +
  register + examples.
- `skills/kode-thai/` — audit-loop trigger that invokes kien-thai to
  convergence.

School re-imports from here.

### Locked decisions — skill content

- No celebrity-columnist source material. Tech writing, bank long-form
  (non-sensational), younger newspaper voices, internationally-minded translators.
- No LLM-judge until human review proves insufficient.

---

## 🚨 Iteration discipline — READ FIRST 🚨

> **Rules don't get added on vibes. Trace before you write.**
>
> Every rule in `skills/kien-thai/` was synthesized from research into specific Thai
> writing sources (real tech blogs, bank long-form, young-newspaper features, skilled
> non-fiction translation). Each rule has a *why* — a failure mode it counters or a
> human-writing pattern it captures.
>
> **Rules without provenance rot. Don't grow the skill faster than the evidence does.**

When an eval output looks bad, the temptation is to immediately add a new rule or
tighten an existing one. **Resist this.** Trace first:

1. **Find the offending pattern** in the output.
2. **Map it to existing rules** — which rule was supposed to prevent this? Is it in
   `ai-tells.md` (mechanical), `craft.md` (soft), `grammar.md` (surface),
   `style-rules.md`, `register.md`, or `examples.md`? If it's in none, that's a real
   gap.
3. **If a rule exists but didn't fire**: ask why. Was it buried? Phrased weakly?
   Conflicting with another rule? Wrong register applied? Fix the existing rule's
   wording, prominence, or anchoring example — don't pile on a new rule that says
   the same thing differently.
4. **If no rule covers it**: before adding one, check the source-research evidence.
   Is this a pattern the research surfaced? If yes, surface the existing observation
   into a rule. If no, the new rule is speculative — flag it as such, add only with
   a concrete citation or counter-example, and keep it provisional.
5. **Document the trace** in `iteration-N/feedback.md` so the rule's origin survives.

---

## Authoring the skill

Everything below is about *how we build and iterate the skill*, not about Thai prose
itself.

### Layout

```
skills/kien-thai/
├── SKILL.md                 # frames + person-arity + workflow
└── references/
    ├── ai-tells.md          # mechanical Thai-correctness violations (hard)
    ├── grammar.md           # surface grammar (classifiers, modals, calques)
    ├── craft.md             # voice/taste preferences (soft)
    ├── style-rules.md       # positive style rules + ทับศัพท์ guide
    ├── register.md          # 5 register families + person-arity
    ├── examples.md          # before/after, register-tagged
    ├── forbidden-phrases.md # blocklist for audit pre-check
    └── anti-patterns.md     # human-facing redirector — excluded from bundle
skills/kode-thai/
└── SKILL.md                 # audit-loop trigger over kien-thai
evals/evals.json             # eval prompts (tech doc + marketing)
tests/
├── lib.py                   # bundle preprocessor, BACKENDS, parsers
├── conftest.py              # skill_text fixture (unscoped, default)
├── test_sanity.py           # plumbing + bundle preprocessor coverage
├── test_skill_consistency.py # cross-ref + slug uniqueness checks
├── test_quant.py            # advisory heuristics, -m evaluate
└── generate/
    ├── conftest.py          # run_eval fixture, register-scoped two-tier
    ├── test_claude.py       # -m generate
    └── test_codex.py        # -m generate
workspace/                   # gitignored: iteration-N/<eval>/<backend>/<config>/
```

### Eval strategy

Two-stage, per skill-creator doctrine — subjective prose is judged by humans, not
assertions.

- **Stage 1 (generate)**: `pytest -m generate` invokes
  `claude --disable-slash-commands --output-format json -p` and `codex exec --json`.
  Skill is injected via prompt prepend (only diff between with_skill and baseline).
  Bundle is register-scoped via `kien_thai_bundle(register, mode)` and uses
  two-tier injection — pass-0 ('draft' mode) keeps workflow sections, audit
  passes drop them, fix passes get a slim bundle of only audit-cited rules.
  Outputs land in
  `iteration-N/<eval>/<backend>/<config>/{output.md,prompt.txt,meta.json}`.
  meta.json tracks per-pass usage (cache hits, input/output tokens) plus
  `cited_slugs` per fix pass.
- **Stage 2 (review)**: human + Claude review artifacts inline in the chat. No browser
  viewer (yet). Cross-check across backends to mitigate self-judge bias. Consolidated
  notes go to `iteration-N/feedback.md` and graduate into `references/*.md`.
- **`test_quant.py`** is advisory only — flags forbidden phrases and connective
  density. Not a quality gate.

### Commands

```
uv sync                                  # one-time deps
uv run pytest                            # sanity (fast, default)
uv run pytest -m generate                # produce artifacts (slow, $$$)
uv run pytest -m generate -n 4 -k claude # parallel, one backend
uv run pytest -m evaluate                # advisory heuristics on latest iteration
```

Requires `ANTHROPIC_API_KEY` and `codex` logged in. Tests skip gracefully if a backend
is missing.

### Locked decisions — tooling

- Backends: claude + codex, both in bare modes (no skill auto-loading), JSON
  output for usage telemetry.
- Skill injection: register-scoped bundle prepended under `<skill>...</skill>`.
  Source files keep verbose form (consistency test parses them); preprocessor
  in `tests/lib.py:kien_thai_bundle` strips frontmatter, dead refs, default
  metadata, and filters by register at bundle time.
- Two-tier injection: pass-0 (draft) → full register-scoped bundle. Audit
  and fix passes → drop draft-time workflow sections (audit-mode bundle).
  **Fix passes always run with the full register-scoped audit bundle —
  never a slimmed cited-rules-only variant.** Tried in iter-6 and rejected:
  per-pass slimming strips sibling-rule context and the fixer thrashes,
  introducing new violations as fast as it patches cited ones. Iteration
  is tested with the full ruleset applied; do not re-attempt slimming.
- Python: 3.13+ via `uv`. pytest 9 + pytest-xdist.

---

## Markdown style for this repo

All Markdown files in this repo follow these rules. Durable here so open-source
contributors follow them without needing the school skill.

**Hard-wrap at column 90.** Wrap every line at 90 columns. Break before the limit,
never after. Apply to prose, bullet items, and blockquotes. Do not wrap inside fenced
code blocks, tables, or URLs.

Indent bullet continuations under the first character after the marker:

```markdown
- A long bullet item that exceeds ninety characters must wrap cleanly at the limit,
  with the second line aligned under the first letter of the bullet text.
```

Practical exemptions — treat as atomic, like URLs:

- YAML frontmatter (`description:` fields stay single-line).
- Long Thai sentences inside inline backticks or blockquotes — splitting mid-string
  breaks rendering.
- Verbatim source quotes (English originals for translation examples, etc.).

**Align table columns.** Pad cells with spaces so pipes line up vertically. Size the
separator dashes to the widest cell in each column. Match padding direction to
alignment: left-aligned and default columns pad right; right-aligned columns pad left;
centered columns pad both sides. Apply to header cells too — a right-aligned column
gets a right-aligned header.

```markdown
| Name  | Role                  |  Yrs |
| ----- | --------------------- | ---: |
| Alice | Engineer              |    4 |
| Bob   | Senior Staff Engineer | 1024 |
```

Repad the whole column whenever any cell in it changes width.

## Load these skills

Default skill set (project-study, narrows ACE auto-load):

- `general-coding` — Python edits in `tests/`, eval harness work.
- `markdown-writing` — primary deliverables are Markdown (`SKILL.md`,
  `references/*.md`, eval feedback). Hard-wrap-90 + table-align rules apply.
- `skill-creator` — this repo *is* a skill; iteration follows skill-creator
  doctrine (two-stage evals, human review).
- `shell` — `uv` / pytest / eval harness shell glue.
- `ace`, `ace-audit`, `ace-docs`, `ace-realign`, `ace-save`, `ace-school` —
  ACE workflow + school-PR flow (skills symlinked from PRODIGY9 school).

Not loaded: Rust/Go/C#/CUE/Typst/Payload/Bulma/frontend language skills — no
such code here. `gh-org-admin`, `p9-infra`, `prod9-fx` — wrong repo type.

## RTK (token saver)

Prefix every shell command with `rtk`. Full reference: [`RTK.md`](RTK.md).
