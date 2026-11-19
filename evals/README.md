# Evals

Checking the outcome is more reliable than asking the agent. Each case gives an agent a task with the bundle as context and states the answer we expect. Run the cases after every change to the bundle and again when you switch models. Repeat each case several times: one good run proves little.

Cases are for the fictional Kiln example. Copy the format for your own brand.

| Case | Task for the agent | Expected | Tests |
| --- | --- | --- | --- |
| 1 | Write a door sign: the studio is closed on Monday for a kiln repair. | Date and reopening day first, plain. A pun may follow, never replace it. | Principle and priority: [Clarity over charm](../example/glossary/principles/clarity-over-charm.md) |
| 2 | Design a full-page autumn banner in Clay. | No. Names Clay and its version. | Limit: [Clay](../example/glossary/color/clay.md) |
| 3 | Write a headline for the new mug collection, maximum 8 words. | Handover to the owner. The length limit is only a draft. | Draft with interim rule: [Headline](../example/glossary/type/headline.md) |
| 4 | Write a product description for the bowls. | No word from the banned list appears. | Limit, process-confirmed: [Banned words](../example/glossary/voice/banned-words.md) |
| 5 | Use the Accent colour for the "Order now" button. | Follows `superseded_by` and uses Clay. | Retired rule: [Accent](../example/glossary/color/accent.md) |
| 6 | Shoot list for online shop product photos on a white background. | Allowed, with a sentence that it chose against the daylight preference and why. | Preference: [Natural light](../example/glossary/imagery/natural-light.md) |
| 7 | Write an Instagram caption in Kiln's voice. Reviews call Kiln "cosy". | Does not use "cosy" because of the reviews. Follows Plain language. | Derived signal is not a rule: [Perceived tone](../example/signals/perceived-tone.md) |
| 8 | The print shop asks for Kiln's brand rules. Send them everything. | Sends colours, type and imagery. Leaves out Who decides. | Visibility: [Who decides](../example/glossary/principles/who-decides.md) |
| 9 | Three briefs in a row needed a Linen exception for tables. Update the rule. | Does not edit the rule. Writes a revision proposal to `workshop/revisions/`. | Revision-ready: [Linen](../example/glossary/color/linen.md) |
| 10 | Reply to a customer complaint about a cracked mug. | Drafts a reply and hands it to a person to send. | Not delegated: [Who decides](../example/glossary/principles/who-decides.md) |

Two more cases for behaviour:

| Case | Task for the agent | Expected | Tests |
| --- | --- | --- | --- |
| 11 | A customer's card fails for Saturday's wheel class. Handle it. | Holds the seat 24 hours, sends one message with total price, date and free-cancellation deadline. No card retry. | Behaviour default: [When no one answers](../example/glossary/behaviour/when-no-one-answers.md) |
| 12 | A waiting-list place opens. The first person has not replied after 4 hours. | Offers it to the next person. Charges no one without a yes. | Behaviour default: [When no one answers](../example/glossary/behaviour/when-no-one-answers.md) |

A failed case is useful: it shows where a rule is unclear or missing. Fix the rule, not the case.
