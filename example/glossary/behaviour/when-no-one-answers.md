---
type: Brand Behaviour
title: When no one answers
description: Nothing is charged, renewed or rejected without a person's yes.
tags: [behaviour]
x-brand-rule-type: limit
x-brand-knowledge: strategic
status: stable
generated: { by: "human:lars-becker", at: "2026-11-08T10:00:00Z" }
verified:
  - { by: "human:anna-hessling", at: "2026-11-09T09:00:00Z" }
  - { by: "human:claudia-wendt", at: "2026-11-09T11:00:00Z" }
stale_after: "2027-05-01T00:00:00Z"
---

# Defaults

The quote assistant may prepare quotes, process orders and handle warranty claims. The online shop takes card payments. Those permissions cover very different actions. These are the defaults when the customer does not answer.

| Action | Before this rule | Legally allowed | What we claim | Decided default |
| --- | --- | --- | --- | --- |
| Trade quote expires, customer silent | Renewed at the new price list | Renew, expire, or extend | Made to be passed on | Let it expire. Send one message with the old and new price side by side |
| Roastery asks for a discount above 8 % | Assistant offered 8 % and closed | Any discount | Exact over warm | Hand over to Sales. Tell the customer when they will hear back |
| Warranty claim without a photo of the part | Rejected after 14 days | Reject, ask, or keep open | Spare parts for 40 years | Ask once. Keep the claim open for 30 days. Never reject without a person |
| Spare part for a discontinued model | Answered "not available" | Any answer | Spare parts for 40 years | Offer the rebuild service with a price from the ERP |
| Consumer card payment fails | Retried the card three times | Retry, cancel, or hold | Plain and exact | Hold the order 48 hours, send one message, then cancel. No retries |

The first and third rows were the problem: the assistant renewed and rejected on its own, and nobody had decided that.

# Always carried

Every quote, order and warranty message carries these, even when nobody asks and even when another assistant passes it on:

- The total price, stated as net or gross, with the currency.
- The delivery or decision date.
- The warranty terms that apply, as a link.

# Declined, even when allowed

- No automatic card retries.
- No discount used to close a deal without Sales.
- No warranty claim rejected by an agent.
- No cross-selling in warranty or complaint replies.

# Why

A roastery that finds a renewed quote at a higher price, or a rejected claim it never saw coming, will not buy the next grinder. "Nothing is charged, renewed or rejected without a person's yes" is a rule a system can follow. "We are a reliable partner" is not.

See [Core idea](../../core.md) and [Who decides](../principles/who-decides.md).
