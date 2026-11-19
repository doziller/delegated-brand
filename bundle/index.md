---
okf_version: "0.3"
title: "<Brand name> brand bundle"
description: "Meaning, rules, and priorities of the <Brand name> brand. Values live in the token file. Use it before writing, designing, or deciding in the brand's name."
license: LicenseRef-All-rights-reserved  # the licence for YOUR brand's rules; choose one, e.g. CC-BY-4.0 if you want to share them
x-brand-tokens: tokens.json
x-brand-owner: "team:<brand-team-id>"
x-brand-visibility-default: public  # public | internal | restricted; concepts may override with x-brand-visibility
x-brand-assets: "<link to your DAM or asset library, or remove this line>"
---

# Read first

* [Core idea](core.md) - The one idea every other rule applies
* [Facts](facts.md) - The only source for names, numbers, prices and claims

# By task

Read the core idea, then only the row that matches your task.

| If you are making | Read |
| --- | --- |
| Any copy | [Plain language](glossary/voice/plain-language.md), [Principles](glossary/principles/), [Facts](facts.md) |
| A layout, page or slide | [Colour](glossary/color/), [Type](glossary/type/), tokens.json |
| An action for a customer (booking, payment, reply) | [When no one answers](glossary/behaviour/when-no-one-answers.md), [Facts](facts.md) |
| A decision no rule covers | [Principles](glossary/principles/), then hand over to the owner |
| A review of someone's work | the rubric in `evals/rubric.md` at the repository root |

# Glossary

* [Colour](glossary/color/) - What each brand colour role means and when to use it
* [Type](glossary/type/) - What each type role means and when to use it
* [Voice](glossary/voice/) - How the brand writes, with examples
* [Principles](glossary/principles/) - Which value wins when two collide
* [Behaviour](glossary/behaviour/) - What systems and agents do when nobody decides

# Tokens

* [tokens.json](tokens.json) - Values in W3C Design Tokens format. Owned by the design system team. Replace with your own or point `x-brand-tokens` at your token package.
