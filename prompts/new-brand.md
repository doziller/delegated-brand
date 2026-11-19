# Prompt: set up a new brand

Copy everything between the lines into your AI coding agent (Claude Code, Codex, Cursor or similar), opened in this repository's folder. Replace the parts in angle brackets.

---

You are setting up a brand bundle for **<brand name>** in this repository.

First read `README.md` and `AGENTS.md`. Then read the example in `example/` to see what a filled bundle looks like. Do not change anything in `example/`.

Material you can use:
- <links to the website, brand guidelines PDF, tone-of-voice document, or "none">
- <path or link to the design tokens, Figma variables export, or "none">

Work in this order:

1. **Interview me first.** Before writing anything, ask me these questions, a few at a time, and wait for my answers:
   - Who decides on the brand, and who should agents hand over to? (the owner)
   - Do other people own parts of it, for example Legal for claims, Sales for quotes, Product for specifications?
   - What is the one idea the brand applies everywhere, in one sentence?
   - Which facts may copy use: names, address, prices, claims? Which of them live in other systems (price lists, product database, certificates)? Which claims must never be made?
   - Which colours, fonts and other values does it use, and where are they defined?
   - How does the brand write? Give me two sentences that sound right and two that sound wrong.
   - Which words or styles does it never use?
   - Where do two brand values collide in practice, and which one wins?
   - What must an agent never do alone?
   - Which actions do systems or agents take for customers (book, charge, cancel, reply)? What happens today when nobody answers, and what should happen? What does the brand decline even when it would be allowed?
   - Which rules are internal and must not go to partners?
2. **Fill `bundle/`.** Set the brand name and owner in `bundle/index.md`, and adjust its reading list by task. Write the one idea into `bundle/core.md` and the facts into `bundle/facts.md`. Put values in `bundle/tokens.json` (W3C Design Tokens format, primitives under `primitive`, semantic tokens outside it). Write one file per rule in `bundle/glossary/`, using the existing files as templates. Copy and rename them for more rules.
3. **For every rule:** set `type` and `x-brand-rule-type` (limit, default, principle or preference), write When, When not, Why and Rejected, and add a `sources` entry when a rule comes from my material. Set `status: draft` and `generated` to yourself. Never add `verified`.
4. **Do not guess.** Anything you are unsure about goes under "Open questions" with a proposed interim rule. Leave "Decides" for me.
5. **Check.** Run `python scripts/check_bundle.py bundle` and fix every error.
6. **Report back** with three lists: the rules you wrote, the open questions I need to answer, and the rules I should review first because agents will use them most.

---

## After the agent is done

1. Read each rule in `bundle/glossary/`. Change what is wrong.
2. When a rule is right, add your approval to its header and set it to stable:
   ```yaml
   status: stable
   verified: { by: "human:<your-name>", at: "<today>T12:00:00Z" }
   ```
3. Answer the open questions. Each answer either becomes part of a rule or stays open with its interim rule.
4. Commit the result. From now on, agents use the bundle with `prompts/use-brand.md`.
