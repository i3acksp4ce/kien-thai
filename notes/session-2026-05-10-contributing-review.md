# Session checkpoint — 2026-05-10 — CONTRIBUTING.md review

Long 1-by-1 review session of chakrit's edits to `CONTRIBUTING.md`. All issues
discussed, all decisions reached, queued tasks listed below. **Nothing has
been executed yet** — resume in a fresh session and run the batch in step 5
of the 1-by-1 protocol.

## How to resume

1. Open this file, read the task lists below.
2. Apply CONTRIBUTING.md edits in one batch (parallelize freely — tasks are
   independent except for trivial line overlaps noted in descriptions).
3. Apply notes-infrastructure edits.
4. Then handle the pending separate request (news-article eval — needs source
   pick first).

If `git status` shows the original chakrit-edited `CONTRIBUTING.md` modified
but uncommitted, that is the expected starting state.

## Pending CONTRIBUTING.md edits (7)

All target the chakrit-edited version of `CONTRIBUTING.md` already in the
working tree.

1. **`กฏ` → `กฎ`** — 4 typo instances:
   - §1 `อย่ารีบเพิ่มกฏเร็วกว่าเพิ่มหลักฐาน`
   - §1 last bullet `diff ของการแก้ไขกฏนั้นๆ`
   - §2c `cite slug ของกฏ`
   - §2c `ทำไมกฏไม่ทำงาน`

2. **ๆ spacing — normalize to spaced form** — 4 no-space drifts:
   - L24 `แย่ๆ` → `แย่ ๆ`
   - L29 `จริงๆ` → `จริง ๆ`
   - L30 `นั้นๆ` → `นั้น ๆ` (overlaps with `กฏ→กฎ` fix on same line)
   - L108 `สั้นๆ` → `สั้น ๆ`

   Decision rationale: contributor-doc register reads official-ish; honor
   Royal-Institute spacing rule for this file. Marketing/casual register is
   open and goes to research-queue.

3. **Lowercase mid-sentence English verbs** — 3 typo-shape capitalizations:
   - L119 `Submit` → `submit`
   - L132 `Issue/PR` → `issue/PR` (PR stays uppercase as acronym)
   - L132 `Run` → `run`

4. **Remove Thai-prose comma-listing in L1** — `เจอกฎที่ผิด, เจอ AI tell ที่
   skill จับไม่ได้, หรืออยากเพิ่มกฎใหม่` → space-separated form. Mirror the
   ๆ-spacing call (honor strict form for contributor-doc register).
   **Do NOT touch** English-style parenthetical lists elsewhere in the file
   (e.g. `tech blog, bank long-form, newspaper รุ่นใหม่, งานแปลฝีมือดี`) —
   different shape, not part of this issue.

5. **`นัยยะ` → `นัย`** — §5 line `ถ้าระดับคุณภาพหรือจำนวน pass แย่ลง
   อย่างมีนัยยะ ตัว pytest จะ flag ให้เอง`. Shorter, more standard form.

6. **Compress L1 nominalization** — `ขั้นตอนสำหรับการเสนอการแก้ไข` →
   `ขั้นตอนการเสนอการแก้ไข` (drop `สำหรับ`, keep verb-noun internally). The
   original `ขั้นตอนเสนอแก้ไข` was verb-verb and a calque per chakrit's
   analysis.

7. **Shorten L20 failure-mode phrasing** — `ที่ต้องการกันไม่ให้เกิดขึ้น` →
   `ที่ไม่ต้องการให้เกิดขึ้น`. Drops `กัน`. The original `ที่ป้องกัน` was a
   calque (Thai doesn't กัน failure modes).

## Pending notes-infrastructure edits (7)

All net-new files except #20 which migrates+deletes.

1. **Create `notes/research-queue.md`** — sibling to other notes/ files.
   Purpose: speculative items needing evidence. Seed with **one** item:
   *ๆ-spacing as register-scoped style.* Question: is ๆ-spacing
   register-dependent in real Thai writing? Hypothesis (chakrit's
   speculation, NOT verdict): formal/contributor → spaced; marketing/casual
   → no-space. Scope: tech blog, bank long-form, newspaper, dev casual,
   government, academic, marketing copy. Landing place: new or amended rule
   in `style-rules.md` or register-scoped slot in `register.md`.

2. **Append second item to research-queue.md** — *Comma-listing as a
   register/formality feature, AND register-vs-formality as the right
   organizing axis.* Two intertwined sub-questions: (a) does Thai-prose
   comma-listing track register, formality, both, or neither? (b) is
   "formality" a missing/replacement axis to the current 5-register taxonomy
   in `references/register.md`? Method: survey the curated corpus
   (`corpus/curated/`) across families. Landing place: new dimension in
   `register.md`, feature-by-register matrix, or separate formality axis.

3. **Create `notes/judgements/README.md`** + the `notes/judgements/`
   directory. Convention borrowed from ace-docs: `YYYY-MM-DD-slug.md` per
   entry, README.md as rules+index. Internal entry shape stays
   project-specific: Context / Call made / Verdict / Takeaway. Entry rules
   (with tightening): add an entry only when ALL hold —
   1. chakrit is the editor of the change under discussion,
   2. discussion happened,
   3. **substantive judgment disagreement** (language norm, register
      choice, design tradeoff, taste/voice call, rule scope) — NOT
      mistake-correction.

   Explicit "do not log" list: Claude getting basic facts wrong, audience
   mismatch, missed context, mechanical/factual errors, things Claude should
   have known by reading. Rationale: log is for trails of taste/judgment
   that future Claude can re-learn from, not a generic mistake tracker.

4. **Create `notes/judgements/2026-05-10-english-prose-economy-lens.md`** —
   Title concept: "English-prose-economy lens fails on Thai register/aspect
   markers." Context: review of CONTRIBUTING.md verbosity/nominalization
   edits. Call made: Claude flagged four markers as filler — `จะ` in
   `อยากจะช่วย` (L1) and `ก่อนจะเพิ่ม` (L29), `ให้` in `ให้ใช้ template`
   (L36), `ลำดับ` in `ลำดับชั้น` (L42). Verdict: every one was load-bearing —
   `จะ` carries aspect/intentionality (without it = flat statement or ห้วน
   robot-speak); `ให้` carries directive register; `ลำดับ` softens ห้วน on
   its own. Underlying error: Claude reads Thai through English Strunk-and-
   White minimalism logic. Cross-references the politeness entry as a
   related case. Takeaway: when an edit adds particles/markers that look
   like filler, do not flag as "verbose" — check first whether the marker
   is doing register/aspect/grammatical work the Thai sentence requires.
   Default-suspect own English-economy reflex.

5. **Migrate `notes/judgment-log.md` politeness entry** to
   `notes/judgements/2026-05-10-politeness-not-ai-tell.md`. Preserve the
   Context / Call made / Verdict / Takeaway shape. Then **delete the old
   `notes/judgment-log.md`** — its rules content lives in
   `notes/judgements/README.md` per item 3 above.

6. **Create `notes/work-queue.md`** — sibling. Purpose: decided work items
   awaiting design/build (distinct from research-queue's speculative items
   and judgements' retrospective entries). Seed with **one** item:
   *Thai-aware markdown wrap tooling.* Need: enforce CLAUDE.md
   hard-wrap-90 rule on Thai-heavy markdown — codepoint-based counting
   overshoots ~10–15% (Thai combining marks are zero-width); Thai has no
   word spaces (needs dictionary segmentation). Scope: uniform across all
   `.md` the repo produces or maintains. Findings: pythainlp already in
   deps (provides `word_tokenize`); ICU4C is heavier alternative. Open:
   design choice (Python+pythainlp+wcwidth vs ICU vs other), integration
   point (CLI tool, pre-commit hook, generator post-processing, or all).
   Block on this before hand-fixing wrap regressions.

7. **Append second item to work-queue.md** — *Thai dictionary lookup
   capability.* Need: when uncertain about spelling/word usage, both Claude
   and contributors should be able to verify against an authoritative Thai
   source rather than rely on memory or web search. Scope: where to source
   (RID published forms? pythainlp ships with one? other?), where to store
   (gitignored or checked in, depending on size/license), how to access
   (CLI tool, Python helper, raw file lookup). Open: licensing — RID
   dictionaries may not be redistributable, may need to be a per-developer
   download with a script. Block on this before making confident orthography
   claims in skill/contributor docs.

## Pending separate request — eval addition

**Add one more eval to `evals/evals.json` — a news article in
newspaper-รุ่นใหม่ register.** Interleave with the rest of the batch in
fresh-session execution (still keep as its own commit per "one logical
change per commit").

Open at execution time:
- Read `evals/evals.json` for existing eval shape and mirror it. Existing
  evals per CLAUDE.md are tech-doc and marketing.
- Pick or write a representative news-article prompt. Should evaluate the
  features the newspaper-รุ่นใหม่ register cares about — not over-formal
  government voice, not click-bait headline voice, but the younger-feature
  / long-form-news pattern.
- Confirm the new eval surfaces in
  `workspace/iteration-N/<eval>/<backend>/...` paths once added.

## Issues from review with NO edit (for the record)

- Dropped `## ติดต่อ` section in CONTRIBUTING.md — intentional, repo is
  obviously GitHub.
- Dropped `Stage 4 token-audit` bullet in §6 — Claude error on initial
  review (internal jargon contributors can't parse). Keep removed.
- Original `อย่าโตเร็วกว่าหลักฐาน` metaphor — was a calque of an English
  startup-writing idiom; chakrit's literal replacement is correct. Keep.
- 90-col wrap regression in CONTRIBUTING.md — deferred to wrap-tooling work
  item (work-queue.md).
- ๆ-spacing/comma-listing register questions — deferred to research items.

## Realign banner active

The session has been carrying:

> Realign: queue items only after we have reached a decision/resolution,
> not before.

If resuming in a new session, this banner does not auto-restore. The rule
behind it is real and was hard-won this session — consider re-invoking
`/realign` or just internalize it.

## Memory notes already updated this session

- `~/.claude/projects/.../memory/user_thai_native.md` — captures: politeness
  is the default register in Thai (not an AI-tell); Claude's Thai judgments
  are unreliable; defer to the user on subjective Thai-prose calls.
