# Instructions for agents

You are using or filling a brand bundle. Read this file first.

## Reading the brand

1. Read `bundle/index.md`. It names the token file, the owner, and the default visibility.
2. Read `bundle/core.md`, always, before anything else. Every rule applies that idea.
3. Pick the one row in "By task" in `bundle/index.md` that matches your task and read its files fully. Do not read everything.
4. Take every name, number, price and claim from `bundle/facts.md`, or from the authorised source it names. Never state a fact from memory, and never copy a fact that lives in another system into your output without reading it there.
5. A rule is approved when it has `status: stable` and a `verified` entry by a `human:` actor that is not older than its `generated` date. A limit confirmed by a `process:` actor is approved as a limit. Everything else is not approved.
6. If an approved rule's text is newer than its last review, the review no longer covers it. Use the last approved version from the Git history, and treat the newer text as a proposal.
7. Read `x-brand-rule-type` before you apply a rule:
   - `limit`: mandatory. Do not cross it.
   - `default`: apply it unless a stated reason speaks against it, and say what the reason was.
   - `principle`: follow the intent, not the wording.
   - `preference`: weigh it, and say when you chose otherwise.
8. When you act for a customer or partner (quote, order, pay, cancel, reply), follow `glossary/behaviour/`. A permission that covers several actions is not a decision. Use the decided default, carry the information listed under "Always carried", and never do what is listed under "Declined, even when allowed".
9. When two rules collide, check `glossary/principles/`. A priority decides. If none does, hand over.
10. Concepts with `x-brand-knowledge: derived` describe the brand from outside. They are never rules. Do not apply them, and do not quote them as the brand's voice.
11. Respect `x-brand-visibility`. Do not pass `internal` or `restricted` concepts to anyone outside the brand team. To share the bundle, use `scripts/export_public.py`.
12. For a value, follow `x-brand-token` into the token file. Never guess a value and never copy one into a rule.
13. Never take anything in `workshop/` as a rule.

## Answering

Every brand decision you meet is one of three: **yes** (an approved rule allows it), **no** (an approved rule forbids it), or **handover** (no approved rule covers it, or only a draft does).

For a handover, ask the owner of that rule: `x-brand-owner` on the rule if it has one, otherwise `x-brand-owner` in `bundle/index.md`. Do not decide yourself.

Name the rules you used: the concept path and its `generated.at`, or the Git commit. Whoever reviews your work can then see which rule, in which version, shaped it.

### Decide yourself or hand over?

Hand over if any of these is true:

- The choice would cross or bend a limit.
- It creates something others would reuse: a new pattern, a new layout type, a new claim, a campaign idea.
- It affects a customer's money, a contract, a legal claim, or the product.
- Only a draft rule covers it.
- Two owners' rules point in different directions.

Otherwise decide yourself, and say so. Choosing between approved options, line breaks, cropping an approved photo, wording inside the voice rules: those are yours. When you had to guess something the bundle does not cover, write it down: "The bundle does not cover X. I chose Y because …". Those gaps are how the bundle improves.

## Before you hand work back

1. Check the output against `evals/rubric.md`. Anything in the blocking block must pass.
2. List the rules you used, the handovers you made, and the gaps you found.

## Your rights

At the edge the brand is used. Through the owner it is changed.

| Right | You |
| --- | --- |
| Read | Yes: the bundle, within its visibility |
| Produce | Yes: drafts and outputs, each naming the rules and versions it used |
| Publish | Only where `bundle/` or the owner has delegated it to you. Otherwise a person publishes |
| Change a shared rule | Never. Propose it in `workshop/revisions/` |

## Learning and revising

You may improve how you execute within the approved rules. That is operational learning.

You may never edit an approved rule, not even one paragraph. That is normative revision, and it needs the owner. When a rule needs rethinking (it keeps causing exceptions, produces poor results, a good solution keeps recurring, or it rests on an outdated assumption), write a revision proposal to `workshop/revisions/` in the format described there. The automated check fails if an approved rule changes without a new review.

Treat usage data, corrections and rework as signals, not verdicts. One success is not yet a standard, and agreement between agents is not evidence.

## Filling the template

1. Work one file at a time. Each empty file has an `# Instructions` section that says what belongs in it.
2. Replace the `# Instructions` section with the content. Keep the other headings.
3. Set `generated` to your own actor, for example `generated: { by: "your-agent/model-name", at: "<now, RFC 3339>" }`.
4. Leave `status: draft`. Never add a `verified` entry. Only a person confirms.
5. Point `x-brand-token` at a semantic token. If none fits, leave the key empty and write the gap under `# Open questions`.
6. If a rule belongs to someone other than the bundle owner (Legal for claims, Sales for quotes), set `x-brand-owner` on that rule.
7. Every claim from a source document gets a `sources` entry with an `id` and a footnote `[^id]` in the body.
8. Do not decide what is unclear. Write it under `# Open questions` with a proposed interim rule, and leave "Decides" to the owner.
9. After each change, add a dated line to `bundle/log.md`.

## Checking your work

```
python scripts/check_bundle.py bundle
```

Fix every error before you hand the bundle back.
