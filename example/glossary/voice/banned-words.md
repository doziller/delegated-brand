---
type: Voice Rule
title: Banned words
description: Words Kiln never uses. Checked automatically on every published text.
tags: [voice]
x-brand-rule-type: limit
x-brand-knowledge: implementation
x-brand-banned-words: [artisanal, curated, crafted, elevate, experience, journey, delighted]
status: stable
generated: { by: "human:mira-lund", at: "2026-10-20T09:40:00Z" }
verified:
  - { by: "process:kiln-copy-lint", at: "2026-11-18T02:00:00Z" }
---

# Rule

None of the words in `x-brand-banned-words` appear in published text. The list is in the frontmatter so a linter can read it without parsing prose.

# Why

Each of these words is common in café and craft marketing. Using them makes Kiln sound like everyone else. See [Plain language](plain-language.md).

This is a limit, so a process may confirm it. Changing the list is a normative revision and needs the owner.
