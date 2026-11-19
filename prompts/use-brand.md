# Prompt: work with the brand

The bundle supplies the brand. Your prompt only supplies the job. Do not paste brand rules into the prompt: they are in the files, and a second copy will drift.

Put the first block into your agent's standing instructions (for example a project instruction or a `CLAUDE.md`), or at the start of a task.

---

Before any work for **<brand name>**, read `AGENTS.md` in <path or link to the repository> and follow it: core idea first, then only the files for this task, facts only from `bundle/facts.md`.

Use approved rules only. For every brand decision, tell me whether an approved rule says yes, says no, or does not cover it. If it does not cover it, hand the question to the owner instead of deciding. Name each rule you used and its date. If you had to guess something the bundle does not cover, tell me what you chose and why.

Do not change any rule. If a rule causes problems, write a revision proposal to `workshop/revisions/`.

---

Then give the job in this shape:

```
Make:        <the output: a post, a 5-slide deck, a door sign, a page section>
For:         <the audience>
So that:     <the outcome you want>
Include:     <specific facts, links, names>
Constraints: <length, format, channel, deadline>
```

Example: *"Make: an Instagram caption for the new Thursday wheel class. For: regulars and neighbours. So that: the class fills up. Include: the price from facts. Constraints: under 40 words."*

## Reviewing

To check someone else's work, ask the agent: *"Review this against `evals/rubric.md`. List what is off, blocking items first."*

## Testing whether it works

Run the cases in `evals/README.md` with this prompt, for the example brand first and then with cases for your own brand. Run each case more than once. A case that fails shows a rule that is unclear or missing.
