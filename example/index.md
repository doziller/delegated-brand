---
okf_version: "0.3"
title: Kurbelwerk Hessling brand bundle (fictional example)
description: "Meaning, rules, priorities and behaviour of Kurbelwerk Hessling, a fictional German family manufacturer of hand-crank coffee grinders and industrial grinders. Shows a filled bundle with several owners, two audiences and an agent that acts for customers."
license: CC-BY-4.0
x-brand-tokens: tokens.json
x-brand-owner: "human:tobias-renner"
x-brand-visibility-default: public
x-brand-assets: "https://assets.hessling.example"
---

# About this example

Kurbelwerk Hessling is invented. It is a family company in its third generation, 340 people, based in Germany, exporting to 30 countries. It sells under one brand to two audiences: people who buy a hand-crank coffee grinder for their kitchen, and coffee roasteries that buy industrial grinders and spare parts. A quote assistant handles trade enquiries; an online shop sells to consumers.

That gives the example what a real company has: several people with different decision rights, facts that live in other systems, two voices under one brand, legal limits on claims, and an agent that acts with money involved.

# Read first

* [Made to be passed on](core.md) - The one idea every other rule applies
* [Facts](facts.md) - Where every name, number, price and claim comes from

# By task

Read the core idea, then only the row that matches your task.

| If you are making | Read |
| --- | --- |
| Copy for consumers | [Plain and exact](glossary/voice/plain-and-exact.md), [Banned words](glossary/voice/banned-words.md), [Facts](facts.md) |
| Copy for roasteries and dealers | [Plain and exact](glossary/voice/plain-and-exact.md), [Trade voice](glossary/voice/trade-voice.md), [Exact over warm](glossary/principles/exact-over-warm.md), [Facts](facts.md) |
| Any claim about materials, safety or durability | [Food-contact and durability claims](glossary/claims/food-contact-and-durability.md), [Facts](facts.md) |
| A layout, page, slide or packaging | [Colour](glossary/color/), [Headline](glossary/type/headline.md), tokens.json |
| A photo brief | [Workshop light](glossary/imagery/workshop-light.md) |
| A quote, order, payment or warranty action | [When no one answers](glossary/behaviour/when-no-one-answers.md), [Who decides](glossary/principles/who-decides.md), [Facts](facts.md) |
| A decision no rule covers | [Core idea](core.md), then hand over to the owner of the area |

# Glossary

* [Colour](glossary/color/) - Brass, Paper, and the retired Signal Red
* [Type](glossary/type/) - Headline
* [Voice](glossary/voice/) - Plain and exact, trade voice, banned words
* [Claims](glossary/claims/) - Food-contact and durability claims. Owned by Legal
* [Imagery](glossary/imagery/) - Workshop light
* [Principles](glossary/principles/) - Exact over warm, and who decides
* [Behaviour](glossary/behaviour/) - What the quote assistant and the shop do when no one answers

# Signals

* [Signals](signals/) - What dealers and customers say about Hessling. Never rules

# Tokens

* [tokens.json](tokens.json) - Hessling's values in W3C Design Tokens format

# What this example shows

**Four rule types**

* Limit: [Brass](glossary/color/brass.md), [Banned words](glossary/voice/banned-words.md), [Food-contact and durability claims](glossary/claims/food-contact-and-durability.md), [Who decides](glossary/principles/who-decides.md), [When no one answers](glossary/behaviour/when-no-one-answers.md)
* Default: [Paper](glossary/color/paper.md), [Headline](glossary/type/headline.md), [Trade voice](glossary/voice/trade-voice.md)
* Principle: [Core idea](core.md), [Plain and exact](glossary/voice/plain-and-exact.md), [Exact over warm](glossary/principles/exact-over-warm.md)
* Preference: [Workshop light](glossary/imagery/workshop-light.md)

**Trust and lifecycle**

* Human-reviewed: most rules, each approval bound to the rule's content with `x-brand-hash`
* Limit confirmed by a process: [Banned words](glossary/voice/banned-words.md)
* Draft with an interim rule: [Headline](glossary/type/headline.md), written by the quote assistant
* Revision proposed, rule unchanged: [Paper](glossary/color/paper.md), see `workshop/revisions/example-2026-11-12-paper.md`
* Retired: [Signal Red](glossary/color/signal-red.md), pointing to its replacement

**Ownership, knowledge and visibility**

* Several owners: Legal owns the claims rule, Sales owns the trade voice, Brand owns the rest
* Facts that live elsewhere: prices come from the ERP, certificates from Legal's register
* Strategic, implementation and derived knowledge: [Core idea](core.md), [Brass](glossary/color/brass.md), [Dealer survey](signals/dealer-survey.md)
* Internal only: [Who decides](glossary/principles/who-decides.md)
* Gaps: the semantic tokens `color.surface-industrial` and `color.text` have no brand term yet. `scripts/check_bundle.py` reports both.
