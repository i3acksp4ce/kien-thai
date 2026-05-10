# Anti-patterns (split into focused files)

This file has been split for clarity. The numerical IDs (#1–#45) remain stable
across the split — they map to the same content, relocated.

- [`ai-tells.md`](./ai-tells.md) — mechanical Thai-correctness violations.
  Most rules from this file's earlier life. Hard rules; apply across all
  registers.
- [`craft.md`](./craft.md) — voice / taste / register-conditional preferences.
  Soft rules; scope varies by register.
- [`grammar.md`](./grammar.md) — surface Thai grammar (classifiers, modals,
  function words, verb calques). Hard rules; below the discourse-frame layer.
- [`audit-checklist.md`](./audit-checklist.md) — condensed grep-able checklist
  for kode-thai audit pass.

Cross-references inside the skill that mention rule numbers (`#NN`) still resolve
— the consistency test (`tests/test_skill_consistency.py`) validates this on
every commit.
