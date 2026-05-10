# Audit — gaps in commits e9b8146..019a6fe

Pre-iter-2 audit of the four-commit restructure session. Status per item is
TBD until discussed 1-by-1. No edits made.

Commits inspected:
- `2809b2f` — split anti-patterns.md → ai-tells / craft / grammar; add consistency test
- `4d8543f` — grammar.md slug pilot; audit-checklist as audit entry point; examples.md Thai rewrite
- `6f3d4eb` — scholar citations folded into existing rules; use/mention exemption on blocklist
- `019a6fe` — workspace/iteration-2/PLAN.md (resume plan only)

## Real gaps

### G1 — kode-thai/SKILL.md references stale 4-file layout

`skills/kode-thai/SKILL.md:18-21` says "Load kien-thai in full — SKILL.md
plus all four references (`anti-patterns.md`, `style-rules.md`, `register.md`,
`examples.md`)." After 2809b2f the references are seven (`ai-tells.md`,
`craft.md`, `grammar.md`, `style-rules.md`, `register.md`, `examples.md`,
`audit-checklist.md`). Direct `/kode-thai` invocations under-load. The
conftest loop bundles full skill_text so iter-2 generation isn't blocked,
but the docstring contract is wrong.

Status: TBD.

### G2 — kien-thai/SKILL.md self-edit step points to redirect stub

`skills/kien-thai/SKILL.md:282` says "Search for the forbidden phrases in
`references/anti-patterns.md`." That file is now a 21-line redirect; the
blocklist lives in `audit-checklist.md`. Should match the audit-pass wiring
in `conftest.py:_audit_prompt`.

Status: TBD.

### G3 — style-rules.md self-description is stale

`style-rules.md:3` says "Counterpart to `anti-patterns.md`." After the split
the counterpart is `ai-tells.md` + `craft.md` + `grammar.md`.

Status: TBD.

### G4 — Two new grammar.md rules carry no `#NN`

`grammar.md:109` (`สามารถ ... ได้` modal frame) and `grammar.md:121` (`ใน`
vs `ของ` for time periods) are headed without numeric IDs. `audit-checklist.md`
references them at lines 72–73 by name only.

Consequences:
- `tests/test_skill_consistency.py` only validates `#NN` / `Frame N` —
  these rules are outside its coverage.
- Audit prompt asks for "rule slug … or #NN"; auditor can cite neither
  cleanly.

Options: assign #46/#47, give them slugs and extend the consistency test
to validate slugs, or both.

Status: TBD.

### G5 — Slug pilot has no consistency test

4d8543f added slugs to `grammar.md` (`wrong-classifier`, `missing-cha-modal`,
etc.) and the audit prompt asks the auditor to cite slugs. The consistency
test (added in 2809b2f) only knows about `#NN` and `Frame N`. A typo'd or
deleted slug citation won't be caught.

Status: TBD.

### G6 — Audit prompt has no register signal

`_audit_prompt` says "Craft (filter ตาม register ของ prose)" but never tells
the auditor which register the prose is in. The auditor must infer from prose
alone. For ambiguous outputs (Explainer vs SaaS-SME), craft rules with
register-scoped exemptions (#19 CTA bang, #24 emotional reassurance, #25
ครับ/ค่ะ, #41 classifier shortcuts) will misfire either direction.

The eval already knows the register family (encoded in the eval prompt) —
pipe `eval_case.id` or its register tag through to the audit prompt.

Status: TBD.

### G7 — Frame 4 ต่างหาก closure and Frame 6 ก็-resumptive bridge aren't discrete audit items

Both added in 6f3d4eb to SKILL.md proper. `audit-checklist.md` only carries
umbrella entries (#38 closure particle, #40 seam connectives). PLAN.md
§"What to look for" expects the loop to fire on these specifically — at
current granularity it'll cite #38 or #40 generically.

Status: TBD.

### G8 — Iter-2 has not been run end-to-end

`workspace/iteration-2/` contains PLAN.md only. The point of the four
commits' wireup is unverified — the loop driver
(`conftest.py:_run_loop`, 5-pass cap, audit/fix subprocess pair) has never
executed against a real backend.

Status: TBD.

## Cosmetic / low-priority

- `kien-thai/SKILL.md:52` says "Covers anti-patterns #6, #12" — fine since
  IDs stable, but the file no longer exists as such; could read "Covers
  ai-tells.md #6, #12".
- `kode-thai/SKILL.md:57` refers generically to "kien-thai's rules" — OK.

## Discussion log (filled during 1-by-1 walkthrough)

(empty)
