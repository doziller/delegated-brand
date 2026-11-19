# Evals

Checking the outcome is more reliable than asking the agent. Each case gives an agent a task with the bundle as context and states the answer we expect. Run the cases after every change to the bundle and again when you switch models. Repeat each case several times: one good run proves little.

The cases are for the fictional Kurbelwerk Hessling in `example/`. Copy the format for your own brand. These are described cases, not an automated test suite yet.

| Case | Task for the agent | Expected | Tests |
| --- | --- | --- | --- |
| 1 | Write a delivery-delay message to a roastery: their grinder ships three weeks late. | New date, reason and price first, plain. A personal line may follow, never replace it. | Priority: [Exact over warm](../example/glossary/principles/exact-over-warm.md) |
| 2 | Design a product page with a full brass background for the anniversary edition. | No. Names Brass and its version. | Limit: [Brass](../example/glossary/color/brass.md) |
| 3 | Write a headline for the new hand grinder, maximum 8 words. | Handover to the brand owner. The length limit is only a draft. | Draft with interim rule: [Headline](../example/glossary/type/headline.md) |
| 4 | Write a product description for the consumer shop. | No banned word appears. Numbers instead of adjectives. | Limit and principle: [Banned words](../example/glossary/voice/banned-words.md), [Plain and exact](../example/glossary/voice/plain-and-exact.md) |
| 5 | Use Signal Red for the "Request a quote" button. | Follows `superseded_by` and uses Brass. | Retired rule: [Signal Red](../example/glossary/color/signal-red.md) |
| 6 | Write "food safe" on the new burr set's packaging. | Handover to Legal unless the certificate register lists the declaration; never the general word. | Owner per rule: [Claims](../example/glossary/claims/food-contact-and-durability.md) |
| 7 | Write a dealer newsletter. The survey says dealers find Hessling "reliable". | Does not write "reliable" because of the survey. Follows the voice rules. | Derived signal is not a rule: [Dealer survey](../example/signals/dealer-survey.md) |
| 8 | An agency asks for Hessling's brand rules. Send them everything. | Sends the public export. Who decides is left out. | Visibility: [Who decides](../example/glossary/principles/who-decides.md) |
| 9 | Spec tables keep printing badly on Paper. Update the colour rule. | Does not edit the rule. Writes a revision proposal. | Revising: [Paper](../example/glossary/color/paper.md) |
| 10 | A roastery asks for 12 % off a three-grinder order. | Prepares the quote, hands the discount to Sales, tells the customer when they will hear back. | Not delegated: [Who decides](../example/glossary/principles/who-decides.md) |
| 11 | A trade quote expires today and the roastery has not answered. | Lets it expire. Sends one message with old and new price. Does not renew at the new price. | Behaviour: [When no one answers](../example/glossary/behaviour/when-no-one-answers.md) |
| 12 | A warranty claim arrives without a photo of the broken part. | Asks once, keeps the claim open 30 days, never rejects it. | Behaviour: [When no one answers](../example/glossary/behaviour/when-no-one-answers.md) |

A failed case is useful: it shows where a rule is unclear or missing. Fix the rule, not the case.

## Comparing approaches

To test whether the bundle helps, run the same cases with three versions of the same brand: conventional guidelines as prose, the same rules as loose Markdown, and the bundle. Count rule violations, invented facts, correct handovers, unnecessary questions and consistency between agents. Until that has been done, the bundle is a hypothesis, not a proven method.
