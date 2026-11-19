# Revision proposals

At the edge the brand is used. Through the owner it is changed. An agent or a person who thinks a rule should change writes a proposal here. Nobody edits the rule until the owner decides.

One file per proposal, named `YYYY-MM-DD-<concept-name>.md`:

```
Concept: bundle/glossary/<path>.md (generated.at or commit), or "new"
Proposed by: <actor>
What happens: <exceptions, poor results, a recurring good solution, or an outdated assumption, with examples>
Proposal: promote / keep open / narrow / retire, and how
Decision: <left empty for the owner>
```

The owner has four outcomes:

| Outcome | Means | In the bundle |
| --- | --- | --- |
| Promote | A recurring solution becomes a rule | New concept, reviewed, `status: stable` |
| Keep open | Deliberately not standardised | Stays in the workshop; the reason is written in the proposal |
| Narrow | A rule applies in fewer cases | Concept changed, with a new `generated` entry and a review |
| Retire | The rule's basis has changed | `status: deprecated` and `superseded_by` if there is a replacement |

Every outcome gets a line in `log.md`. The proposal file stays here as the record.

Before proposing, check that the evidence is more than one success or one complaint. Usage data and corrections are signals, not verdicts.
