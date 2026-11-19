# Delegated Brand

**A reference implementation of Brand as Infrastructure, built to test The Delegated Brand.**
By [Dominik Ziller](https://dzgn.work/about/), [DZGN Research](https://dzgn.work/research/).

A template for a brand that people and AI agents read from the same files. Agents may draft rules. Only people approve them. Plain Markdown in Git, following the [Open Knowledge Format (OKF) v0.3](https://github.com/open-knowledge-format/open-knowledge-format).

## Start here

You need no prior knowledge. You need an AI coding agent (Claude Code, Codex, Cursor or similar) and about an hour.

1. **Get a copy.** On GitHub, click "Use this template", or download the repository as a ZIP and unzip it.
2. **Look at the example.** Open `example/index.md`, then `example/core.md`. Kurbelwerk Hessling is a fictional German family manufacturer of coffee grinders, with several owners, two audiences and an agent that handles quotes. Its files show what a finished bundle looks like.
3. **Let an agent set up your brand.** Open the folder in your agent and paste the prompt from [`prompts/new-brand.md`](prompts/new-brand.md). The agent interviews you, reads the material you give it, and drafts the rules.
4. **Approve the rules.** Read each draft, correct it, and approve it with `python scripts/approve.py <rule> --by human:<your-name>`. `prompts/new-brand.md` shows how.
5. **Use it.** Start brand tasks with [`prompts/use-brand.md`](prompts/use-brand.md). Agents then answer from your approved rules and hand everything else to you.

### Words used here

| Word | Meaning |
| --- | --- |
| Agent | An AI that carries out tasks, for example writing copy or building a page |
| Bundle | The folder with your brand's rules, `bundle/` |
| Rule | One file in `bundle/glossary/` that says what applies, how binding it is, and why |
| Token | A named value such as a colour or a font, kept in `tokens.json` |
| Semantic token | A token named by its role (`brand-background`) rather than its look (`green-400`) |
| Owner | The person who decides when no rule covers a case. A bundle has one; single rules can name their own, for example Legal for claims |
| Draft / approved | Written but not yet checked by a person / checked and confirmed by a person |
| OKF | Open Knowledge Format, an open standard for knowledge as Markdown files. This template follows it |
| Frontmatter | The short header between `---` lines at the top of each file |

## Why

When brand work is delegated, it becomes visible which parts of brand management rested on implicit knowledge, human interpretation and informal authority. That is the thesis of **The Delegated Brand**, a working frame (paper in progress). Guidelines written for people leave those parts unsaid. Agents cannot fill the gaps, so this template makes them explicit: what applies, how binding it is, who decided, what is still open, and who may change it.

It belongs to three connected pieces of work:

| Piece | Role |
| --- | --- |
| *Brand as Infrastructure* | The structure: knowledge, rules and governance that make brand decisions executable |
| *The Delegated Brand* | The frame: what happens when brand decisions are spread across people, systems and agents |
| [The Brand Diamond](https://dzgn.work/the-brand-diamond/) | The working model: how an organisation makes and changes its brand when agents make many decisions |
| [Brand Infrastructure Index](https://dzgn.work/brand-infrastructure-index/) and [Report 2026](https://dzgn.work/brand-infrastructure-report-2026/) | The evidence |

## The parts

| Part | What it is | Why it exists | Connects to | Needed? |
| --- | --- | --- | --- | --- |
| `bundle/` | The empty template. One file per brand rule. | The approved brand, readable by people and agents | Everything else points here | Yes |
| `bundle/index.md` | Entry point: brand name, owner, token file, reading list by task | An agent starts here, knows whom to ask and reads only what the task needs | Token file, owner, all rules | Yes |
| `bundle/core.md` | The one idea every rule applies | Read first. Helps decide cases no rule covers | Every rule | Yes |
| `bundle/facts.md` | Names, numbers, prices, claims | The only place a fact lives, so nothing gets invented | Copy of any kind | Yes |
| `bundle/glossary/` | Rules: terms, voice, priorities, decision rights, behaviour | Meaning lives here, once | Tokens via `x-brand-token` | Yes |
| `bundle/tokens.json` | Values: colours, type, spacing (W3C Design Tokens) | Values have one owner, the design system | Glossary terms point at it | Yes, or your own token package |
| `bundle/log.md` | Dated list of changes | Shows what changed, when, and why | Every rule change | Recommended |
| `AGENTS.md` | Instructions for agents | Tells an agent how to read, answer, revise and fill | The whole bundle | Yes, if agents use it |
| `prompts/` | Two ready prompts: set up a new brand, work with the brand | Lets anyone start without knowing the details | `AGENTS.md`, `bundle/` | Recommended |
| `scripts/approve.py` | Approves a rule and stores a fingerprint of its content | A later change to an approved rule becomes detectable | `verified` | Recommended |
| `scripts/check_bundle.py` | A check that runs on every push | Catches approved rules changed after approval, broken token references and wrong field values | Glossary, tokens | Recommended |
| `scripts/export_public.py` | Writes a copy without internal rules, internal tokens and logs | A convenience for sharing with partners. Not a security boundary: read the copy before sharing | `x-brand-visibility` | Recommended |
| `tests/` | Regression tests for the scripts | The checks keep doing what the README says | `scripts/` | Recommended |
| `.github/CODEOWNERS` | Who must approve changes to which files | GitHub can then block changes without the owner's approval | Owners in the bundle | Recommended on GitHub |
| `evals/` | Test tasks with expected answers, and a review rubric | A rule is ready when agents follow it, not when it reads well | Single rules | Recommended |
| `workshop/` | Unfinished thinking and revision proposals | Ideas need a place that agents never take as rules | Becomes a draft in `bundle/` when ready | Optional |
| `signals/` | What others infer about the brand, e.g. from reviews | Useful input, but never a rule | Informs people who review rules | Optional |
| `example/` | The fictional manufacturer Kurbelwerk Hessling, fully filled | Shows every field, state and owner in use | Mirrors `bundle/` | Reference only |
| `llms.txt` | A short map of the repository for AI tools | Lets an agent find the right files quickly | All of the above | Optional |

## How it fits together

```
           design system                      brand team
                │                                 │
          tokens.json  ◄── x-brand-token ──  glossary/ rule
           (values)                           (meaning, type, owner)
                                                  │
     workshop/ ── draft ──► status: draft ── person reviews ──► verified, stable
         ▲                                        │
         │                                   agent reads it
         │                                        │
   revision proposal ◄── rule needs rethinking ── answers: yes / no / handover
                                                  │
                                         evals/ check the result
```

A rule starts as a draft, written by a person or an agent. A person reviews it and it becomes approved. Agents answer from approved rules only and hand over everything else. When a rule stops working, or a good solution keeps recurring, an agent proposes a revision. The owner decides one of four outcomes: promote, keep open, narrow or retire. Retired rules stay as `deprecated` and point to their replacement. At the edge the brand is used. Through the owner it is changed.

## A rule file

Each rule is one Markdown file with a short header. Only two fields are needed to start.

```markdown
---
type: Brand Term                 # needed: what kind of rule
x-brand-rule-type: limit         # needed: how binding it is
title: Clay
x-brand-token: color.brand-background
status: stable
verified: { by: "human:jonas-berg", at: "2026-10-22T14:30:00Z" }
---

# When        where it applies
# When not    where it does not, including the common misuse
# Why         the reason, in the brand's own terms
# Rejected    what was considered and dropped
# Open questions   each with an interim rule and who decides
```

## Fields

| Field | Needed? | What it says | Why |
| --- | --- | --- | --- |
| `type` | Yes | Kind of rule: `Brand Core`, `Brand Facts`, `Brand Term`, `Voice Rule`, `Brand Priority`, `Brand Decision Rights`, `Brand Behaviour` | Without it, the file is not a rule (OKF) |
| `x-brand-rule-type` | Yes | How binding: see the table below | Agents read a limit differently from a preference |
| `status` | Recommended | `draft`, `stable`, `deprecated` | Separates approved from not yet approved |
| `generated` | Recommended | Who wrote the current text, and when | Makes agent-written rules visible |
| `verified` | Recommended | Who approved it, when, and a fingerprint of the content (`x-brand-hash`), written by `approve.py` | A rule is authorised only after a person approves it, and only for the content they saw |
| `x-brand-token` | When the rule has a value | Path to a semantic token | The value stays in one place |
| `x-brand-knowledge` | Optional | `strategic`, `implementation`, `derived` | Derived signals must never become rules |
| `x-brand-visibility` | Optional | `public`, `internal`, `restricted` | A partner needs the type rules, not the escalation rules |
| `x-brand-owner` | Optional | Who decides on this rule, if not the bundle owner: a `human:` or `team:` actor | Legal can own claims, Sales can own quotes |
| `stale_after` | Optional | Date for the next review | Rules get checked before they go stale |
| `superseded_by` | With `deprecated` | Path to the replacement rule | Old links and prompts still lead somewhere |
| `sources` | Optional | Where a rule comes from | Claims can be traced to their source |

On `bundle/index.md`: `x-brand-tokens` (needed), `x-brand-owner` (needed, decides on handovers), `x-brand-visibility-default` (optional), `x-brand-assets` (optional, link to your asset library: logos, images and templates stay there).

In `tokens.json`, a token or group with `"$extensions": {"x-brand-visibility": "internal"}` stays out of the public export.

Fields without the `x-brand-` prefix are standard OKF v0.3.

### Four types of rule

From the Report, Table 9. Not every rule binds the same way.

| `x-brand-rule-type` | Binding | Room to interpret | Who may confirm | Example |
| --- | --- | --- | --- | --- |
| `limit` | Mandatory | None | A person or an automated check | No forbidden logo variant |
| `default` | Until a stated reason speaks against it | Limited | A person | A preferred type size |
| `principle` | In intent, not in wording | Wide | A person | Communicate respectfully |
| `preference` | To be weighed | Wide | A person | Prefer natural photography |

## How agents behave

Full instructions: `AGENTS.md`. In short:

- Read the core idea first, then only the files for the task. Take facts only from `facts.md`.
- Answer from approved rules only: **yes**, **no**, or **handover** to the owner of that rule.
- Hand over when a choice bends a limit, creates something reusable, touches money, contracts, claims or the product, or rests on a draft. Smaller craft choices are theirs, stated openly.
- Read and produce freely. Publish only where that is delegated. Never change a shared rule.
- When acting for a customer, follow the decided defaults in `glossary/behaviour/`. A permission is not a decision.
- Name the rule and its version in every answer, so decisions can be traced.
- Improve execution within the rules. Never change a rule. Propose revisions in `workshop/revisions/`.
- Never apply derived signals, never pass on internal rules, never take the workshop as rules.

## Check it

The check runs automatically on GitHub after every change. To run it yourself:

```
pip install pyyaml
python scripts/check_bundle.py bundle
python path/to/open-knowledge-format/skills/okf-generate/scripts/validate.py bundle
python scripts/export_public.py bundle public-bundle
python -m unittest discover tests
```

### What is enforced, and what is only described

A repository can enforce some of the governance, not all of it.

| Mechanism | How | Enforced? |
| --- | --- | --- |
| An approved rule changes after approval | `approve.py` stores a fingerprint of the content; `check_bundle.py` fails if the rule no longer matches it | Yes, in CI. But anyone who can edit files can also re-approve. Who may do that is controlled by the next line |
| Who may change and approve which files | `.github/CODEOWNERS` plus branch protection on GitHub | Yes, once you set it up on GitHub |
| Token references and field values | `check_bundle.py` | Yes, in CI |
| Internal rules and tokens reach partners | `export_public.py` leaves out what is marked non-public | Partly. It cannot find internal facts written into public text. Read the export before sharing |
| An agent answers yes, no or handover | `AGENTS.md` | No. Described; depends on the agent and its tools |
| An agent publishes or acts with money | `AGENTS.md`, behaviour rules | No. Permissions belong in the systems the agent uses |
| Whether rules contradict each other | People, evals | No |

The scripts have regression tests in `tests/` that run with every change. The bundle is the specification; the systems that run your agents have to respect it.

## What it does not do

- **Define the brand.** People decide what the brand stands for. No format does that for them.
- **Execute.** It holds the rules. Writing, designing and building happen in your tools and agents.
- **Replace your design system or a surface spec.** A `DESIGN.md` for a website can sit next to it and point here for meaning. Conflicts go to the owner.
- **Prove that it works.** Whether structured brand knowledge improves agents' brand work is not yet measured. The evals are where you find out for your brand.

## Behaviour, not only appearance

When an agent acts for the brand (books, charges, cancels, replies), one permission often covers several very different actions. Protocols check whether an action is valid, not whether it fits the brand. If nobody decides, the default decides, usually for whatever is quickest or earns most.

`glossary/behaviour/when-no-one-answers.md` makes those defaults explicit: what happens today when no one answers, what is legally allowed, what the brand claims, and the default the brand decides. It also lists the information every transaction carries, because tone does not survive when another system rewords a message and structure does, and what the brand declines even when allowed. Hessling's version starts with one rule: nothing is charged, renewed or rejected without a person's yes.

From the essay [Authority and Permission](https://dzgn.work/authority-and-permission/).

## How it maps to the Brand Diamond

[The Brand Diamond](https://dzgn.work/the-brand-diamond/) describes the parts and the movement. This repository is one way to build the Brand Knowledge corner and the tip:

| Brand Diamond | In this repository |
| --- | --- |
| Brand Knowledge (resource) | `bundle/`: core idea, facts, rules |
| Design System (resource) | `tokens.json`, or your token package via `x-brand-tokens` |
| DAM & Assets (resource) | Not stored here. Linked with `x-brand-assets` |
| People, Agents, Tools (users) | People approve and decide; agents follow `AGENTS.md`; any tool that reads Markdown |
| Default (girdle) | Rules of type `default`, and the reading list by task |
| Craft (crown) | Not codified. Creative excellence stays with people |
| Checks, Triage, Judgment (pavilion) | Limits checked by `scripts/check_bundle.py`; agents triage with yes, no or handover; people judge principles and preferences |
| Governance (tip) | The owner, `workshop/revisions/`, and the four outcomes: promote, keep open, narrow, retire |
| Four rights | Read and produce at the edge; publish only where delegated; change only through the owner |
| Production loop | Outputs name the rules and versions they used |
| Learning loop | Revision proposals with evidence, decided by the owner |
| Material status | Approved rule (`stable` + current `verified`), generated draft (`draft`), deliberate exception (stated in the output), proposed change (`workshop/revisions/`), retired (`deprecated`) |
| Outside | Partners get concepts marked `public` |

What the Diamond leaves open, the repository leaves open too: who decides when two sources disagree (for example Brand and Product), and how to notice outputs that comply but grow uniform. The Hessling example shows one possible answer to the first, escalation to the managing director. The template does not prescribe one.

## How it maps to the Report

The template answers some of the Report's open questions, as a working proposal, not as tested proof:

| Open question | Answer here |
| --- | --- |
| Can you take your brand rules with you when you change provider? | Plain files in an open format, in Git |
| How does implicit knowledge become explicit? | Rule type, reason and rejected options in every rule |
| Who decides when no rule covers a case? | Handover to a named owner |
| Who deletes rules? | Revision proposals, `deprecated`, `superseded_by`, and the log |

Of the Report's seven activities, the template covers **describe**, **retrieve and interpret**, **decide**, **evaluate** and **change**. **Define** and **execute** stay with people and tools. Of the three forms of lock-in, plain files address knowledge lock-in, the lack of any runtime addresses execution lock-in, and the open check and evals address validation lock-in. Whether two agents apply the same bundle the same way stays open.

Detailed guidance will follow in *A Guide to Building Brand Infrastructure*, announced in the Report. This repository is its working companion.

## Sources and ideas

- Open Knowledge Format v0.3: structure, trust, lifecycle. https://github.com/open-knowledge-format/open-knowledge-format
- W3C Design Tokens format 2025.10: values. https://www.designtokens.org/tr/2025.10/format/
- Robert Haase: rules with accountability, yes/no/handover. https://robert-haase.de/marke-als-mcp-server.html
- Caio Pizzol: durable identity separated from surface design. https://github.com/caiopizzol/brand.md
- Julius Jäger: workshop and showcase, priorities for value conflicts. https://kidentitaet.substack.com/p/markenfuhrung-braucht-jetzt-einen
- Ana State: machine-readable versus agent-ready, extended here by revision-ready. https://github.com/AI-by-design/primitiv
- Meddle: core idea read first, reading list by task, one facts file, review rubric, open questions with interim rules. https://brand.meddle.studio/brand/mojo.md
- Murphy Trueman and PJ Onori: test agent outputs instead of trusting documentation. https://blog.murphytrueman.com/design-systems-need-evals/
- Gloaguen et al.: keep agent instruction files short and task-relevant. https://arxiv.org/abs/2602.11988v3
- Dominik Ziller, Authority and Permission: defaults inside a permission are a brand question. https://dzgn.work/authority-and-permission/
- Dominik Ziller, The Brand Diamond: edge and tip, four rights, four outcomes. https://dzgn.work/the-brand-diamond/
- Brand Infrastructure Report 2026 and Index. https://dzgn.work/research/
- Discussion on a brand use case for OKF. https://github.com/open-knowledge-format/open-knowledge-format/discussions/10

## Cite

Ziller, D. (2026). *Delegated Brand: a reference implementation of Brand as Infrastructure* (Version 0.1.2). DZGN Research. https://github.com/doziller/delegated-brand

Machine-readable: `CITATION.cff`. For the frame and the evidence, cite the [Brand Infrastructure Report 2026](https://dzgn.work/brand-infrastructure-report-2026/).

## Author

Dominik Ziller, Senior Art Director and Brand Designer, Stockholm. Essays and research on brand, technology and judgement at [dzgn.work](https://dzgn.work). [LinkedIn](https://www.linkedin.com/in/dominik-ziller/). Contact: hello@dzgn.work.

Agents did a lot of the typing. A human made the decisions. Which is more or less the point of this repository.

## Using it for something big?

Say hi: hello@dzgn.work. Cite it, link it, star it. Making money with it? Even better, tell me anyway.

That's it. That's the whole sales funnel.

## License

Use it freely. Name the source where the licence asks for it.

| Part | Licence | What it means |
| --- | --- | --- |
| `bundle/` (the empty template) | [CC0 1.0](LICENSE-CC0-1.0.txt) | Free to use without attribution. The brand you write into it is yours, under the licence you choose in `bundle/index.md` (all rights reserved by default) |
| `scripts/`, `tests/`, `.github/` (code) | [Apache 2.0](LICENSE) | Free to use, change and ship, including commercially. Keep the licence and `NOTICE` |
| Everything else: README, `AGENTS.md`, `prompts/`, `evals/`, `workshop/`, `example/`, `llms.txt` | [CC BY 4.0](LICENSE-CC-BY-4.0.txt) | Free to use, change and share, including commercially, with attribution |

Attribution for CC BY material:

> "Delegated Brand" by Dominik Ziller (DZGN Research), https://github.com/doziller/delegated-brand, licensed under CC BY 4.0. Changes: <say what you changed, or "none">.

The rule types and other terms adapted from the [Brand Infrastructure Report 2026](https://dzgn.work/brand-infrastructure-report-2026/) are by the same author and licensed here under CC BY 4.0. The Report itself and the Index on dzgn.work keep their own licences. Third-party standards and ideas are credited under "Sources and ideas"; no third-party text or code is included. Details in `NOTICE`.

*Intent over noise.*
