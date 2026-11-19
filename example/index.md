---
okf_version: "0.3"
title: Kiln brand bundle (fictional example)
description: "Meaning, rules, and priorities of Kiln, a fictional neighbourhood ceramics studio and café. Shows a filled bundle with every rule type and trust state."
license: CC-BY-4.0
x-brand-tokens: tokens.json
x-brand-owner: "human:mira-lund"
x-brand-visibility-default: public
---

# Read first

* [Made upstairs, said plainly](core.md) - The one idea every other rule applies
* [Facts](facts.md) - The only source for names, numbers, prices and claims

# By task

Read the core idea, then only the row that matches your task.

| If you are making | Read |
| --- | --- |
| Any copy | [Plain language](glossary/voice/plain-language.md), [Banned words](glossary/voice/banned-words.md), [Clarity over charm](glossary/principles/clarity-over-charm.md), [Facts](facts.md) |
| A layout, page or slide | [Colour](glossary/color/), [Headline](glossary/type/headline.md), tokens.json |
| A photo brief | [Natural light](glossary/imagery/natural-light.md) |
| A booking or payment action | [When no one answers](glossary/behaviour/when-no-one-answers.md), [Facts](facts.md) |
| A reply to a customer | [Plain language](glossary/voice/plain-language.md), [Who decides](glossary/principles/who-decides.md), [Facts](facts.md) |
| A decision no rule covers | [Core idea](core.md), then hand over to the owner |

# Glossary

* [Colour](glossary/color/) - Clay, Linen, and the retired Accent
* [Type](glossary/type/) - Headline
* [Imagery](glossary/imagery/) - Natural light
* [Voice](glossary/voice/) - Plain language and words Kiln never uses
* [Principles](glossary/principles/) - Clarity over charm, and who decides
* [Behaviour](glossary/behaviour/) - If no answer arrives, nothing is charged and nothing is booked

# Signals

* [Signals](signals/) - Derived knowledge about Kiln from outside. Never rules

# Tokens

* [tokens.json](tokens.json) - Kiln's values in W3C Design Tokens format

# What this example shows

**Four rule types**

* Limit: [Clay](glossary/color/clay.md), [Banned words](glossary/voice/banned-words.md), [Who decides](glossary/principles/who-decides.md), [When no one answers](glossary/behaviour/when-no-one-answers.md)
* Default: [Linen](glossary/color/linen.md), [Headline](glossary/type/headline.md)
* Principle: [Plain language](glossary/voice/plain-language.md), [Clarity over charm](glossary/principles/clarity-over-charm.md)
* Preference: [Natural light](glossary/imagery/natural-light.md)

**Trust and lifecycle**

* Human-reviewed: [Clay](glossary/color/clay.md), [Clarity over charm](glossary/principles/clarity-over-charm.md)
* Review out of date: [Linen](glossary/color/linen.md), changed by an agent after a person reviewed it
* Machine-confirmed limit: [Banned words](glossary/voice/banned-words.md), checked by a process
* Unverified draft with an interim rule: [Headline](glossary/type/headline.md)
* Retired: [Accent](glossary/color/accent.md), deprecated and pointing to its replacement

**Knowledge and visibility**

* Strategic, implementation, and derived knowledge: [Plain language](glossary/voice/plain-language.md), [Clay](glossary/color/clay.md), [Perceived tone](signals/perceived-tone.md)
* Internal only: [Who decides](glossary/principles/who-decides.md)
* Gap: the semantic token `color.text` has no brand term yet. `scripts/check_bundle.py` reports it.
