# Anti-patterns (split into focused files)

This file has been split for clarity. Rules now live in three peers, each with a
stable slug plus inline `type · scope · severity` metadata. Numerical IDs (#1–#47)
also remain — slugs and IDs both resolve.

- [`ai-tells.md`](./ai-tells.md) — mechanical Thai-correctness violations.
  Hard rules; apply across all registers.
- [`craft.md`](./craft.md) — voice / taste / register-conditional preferences.
  Soft rules; scope varies by register.
- [`grammar.md`](./grammar.md) — surface Thai grammar (classifiers, modals,
  function words, verb calques). Hard rules; below the discourse-frame layer.
- [`forbidden-phrases.md`](./forbidden-phrases.md) — string-match blocklist for
  the kode-thai audit pass.

Prefer slug references (`grammar.md#wrong-classifier`, `` `f4/targhak-closure` ``)
over numeric IDs in new cross-refs — slugs survive renumbering. The consistency
test (`tests/test_skill_consistency.py`) validates both forms.
