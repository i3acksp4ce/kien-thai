# PRODIGY9 Coding School

This project's AI coding environment is managed by [ACE](https://github.com/prod9/ace).
Run `ace` to start a coding session. Run `ace setup` if not yet configured.

Skills and conventions are provided by the **PRODIGY9 Coding School** school and are
symlinked into `.claude/skills/`. Skill edits go through symlinks into the school clone
— propose changes back to the school repo when ready. Run `ace config` or `ace paths`
to debug configuration issues.

## Project: thai-prose

A skills repo (open-source target) teaching Claude to write Thai prose that:
1. Reads as little like generic AI output as possible.
2. Has a distinct, believably human voice.
3. Is easy to read for native Thai readers (no brain damage).
4. Counters training-data skew toward over-formal / over-polite Thai.

One skill at `skills/thai-prose/`. School re-imports from here.

### Layout

```
skills/thai-prose/
├── SKILL.md
└── references/
    ├── anti-patterns.md     # AI tells to avoid
    ├── style-rules.md       # positive style rules
    ├── register.md          # formality selection
    └── examples.md          # before/after rewrites
evals/evals.json             # eval prompts (tech doc + marketing)
tests/
├── lib.py                   # shared helpers (paths, BACKENDS, build_prompt)
├── conftest.py              # skill_text fixture
├── test_sanity.py           # plumbing, default-on
├── test_quant.py            # advisory heuristics, -m evaluate
└── generate/
    ├── conftest.py          # run_eval fixture, parametrize
    ├── test_claude.py       # -m generate
    └── test_codex.py        # -m generate
thai-prose-workspace/        # gitignored: iteration-N/<eval>/<backend>/<config>/
```

### Eval strategy

Two-stage, per skill-creator doctrine — subjective prose is judged by humans, not
assertions.

- **Stage 1 (generate)**: `pytest -m generate` invokes
  `claude --bare --disable-slash-commands -p` and `codex exec` in their bare modes.
  Skill is injected via prompt prepend (only diff between with_skill and baseline).
  Outputs land in
  `iteration-N/<eval>/<backend>/<config>/{output.md,prompt.txt,meta.json}`.
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

### Locked decisions

- Backends: claude + codex, both in bare modes (no skill auto-loading).
- Skill injection: full SKILL.md content prepended to prompt under `<skill>...</skill>`.
- Python: 3.13+ via `uv`. pytest 9 + pytest-xdist.
- No LLM-judge until human review proves insufficient.
- No celebrity-columnist source material. Tech writing, bank long-form
  (non-sensational), younger newspaper voices, internationally-minded translators.
