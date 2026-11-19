---
type: Voice Rule
title: Banned words
description: Words Hessling never uses. Checked automatically on every published text.
tags: [voice]
x-brand-rule-type: limit
x-brand-knowledge: implementation
x-brand-banned-words: [timeless, artisanal, premium, experience, journey, unparalleled, iconic]
status: stable
generated: { by: "human:tobias-renner", at: "2026-10-20T09:40:00Z" }
verified:
  - { by: "process:hessling-copy-lint", at: "2026-11-18T02:00:00Z", x-brand-hash: "sha256:a15c9618e04d0e04838324c7807aef31cb313dcec65d81d9114c0f60cf6bf3b2" }
---

# Rule

None of the words in `x-brand-banned-words` appear in published text. The list is in the header so a linter can read it without parsing prose.

# Why

Each of these words is common in coffee-equipment marketing. Using them makes Hessling sound like everyone else, and none of them can be checked. See [Plain and exact](plain-and-exact.md).

This is a limit, so a process may confirm it. Changing the list is a change to a shared rule and goes through the owner.
