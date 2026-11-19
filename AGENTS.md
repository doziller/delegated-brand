# Instructions for agents

You are using or filling a brand bundle. Read this file first.

## Reading the brand

1. Read `bundle/index.md`. It names the token file, the owner, and the default visibility.
2. Read `bundle/core.md`, always, before anything else. Every rule applies that idea.
3. Pick the one row in "By task" in `bundle/index.md` that matches your task and read its files fully. Do not read everything.
4. Take every name, number, price and claim from `bundle/facts.md`. Never state a fact that is not there.
5. A concept with a current `verified` entry by a `human:` actor is approved. `status: draft` is not approved. A limit confirmed by a `process:` actor is approved as a limit.
6. Read `x-brand-rule-type` before you apply a rule:
   - `limit`: mandatory. Do not cross it.
   - `default`: apply it unless a stated reason speaks against it, and say what the reason was.
   - `principle`: follow the intent, not the wording.
   - `preference`: weigh it, and say when you chose otherwise.
7. When you act for a customer or partner (book, pay, cancel, reply), follow `glossary/behaviour/`. A permission that covers several actions is not a decision. Use the decided default, carry the information listed under "Always carried", and never do what is listed under "Declined, even when allowed".
8. When two rules collide, check `glossary/principles/`. A priority decides. If none does, hand over.
9. Concepts with `x-brand-knowledge: derived` describe the brand from outside. They are never rules. Do not apply them, and do not quote them as the brand's voice.
10. Respect `x-brand-visibility`. Do not pass `internal` or `restricted` concepts to anyone outside the brand team.
11. For a value, follow `x-brand-token` into the token file. Never guess a value and never copy one into a rule.
12. Never take anything in `workshop/` as a rule.

## Answering

Every answer you give from this bundle is one of three: **yes** (an approved rule allows it), **no** (an approved rule forbids it), or **handover** (no approved rule covers it, or only a draft does). For a handover, name the owner from `x-brand-owner` and do not decide yourself.

Name the rules you used: the concept path and its `generated.at`, or the Git commit. Whoever reviews your work can then see which rule, in which version, shaped it.

Not every choice is a brand decision. Small craft choices inside the rules (which of two approved headlines, where a line breaks) you may make yourself. When you had to guess something the bundle does not cover, say so plainly: "The bundle does not cover X. I chose Y because …". Those gaps are how the bundle improves.

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

You may never change an approved rule. That is normative revision, and it needs the owner. When you see that a rule needs rethinking (it keeps causing exceptions, produces poor results, or rests on an outdated assumption), write a revision proposal to `workshop/revisions/` in the format described there. Do not edit the concept.

Treat usage data, corrections and rework as signals, not verdicts. One success is not yet a standard, and agreement between agents is not evidence.

## Filling the template

1. Work one file at a time. Each empty file has an `# Instructions` section that says what belongs in it.
2. Replace the `# Instructions` section with the content. Keep the other headings.
3. Set `generated` to your own actor, for example `generated: { by: "your-agent/model-name", at: "<now, RFC 3339>" }`.
4. Leave `status: draft`. Never add a `verified` entry. Only a person confirms.
5. Point `x-brand-token` at a semantic token. If none fits, leave the key empty and write the gap under `# Open questions`.
6. Every claim from a source document gets a `sources` entry with an `id` and a footnote `[^id]` in the body.
7. Do not decide what is unclear. Write it under `# Open questions` with a proposed interim rule, and leave "Decides" to the owner.
8. After each change, add a dated line to `bundle/log.md`.

## Checking your work

```
python scripts/check_bundle.py bundle
```

Fix every error before you hand the bundle back.
