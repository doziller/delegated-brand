---
type: Brand Behaviour
title: When no one answers
description: If no answer arrives, nothing is charged and nothing is booked.
tags: [behaviour]
x-brand-rule-type: limit
x-brand-knowledge: strategic
status: stable
generated: { by: "human:mira-lund", at: "2026-11-08T10:00:00Z" }
verified:
  - { by: "human:jonas-berg", at: "2026-11-09T09:00:00Z" }
stale_after: "2027-05-01T00:00:00Z"
---

# Defaults

Kiln's booking assistant has permission to manage wheel-class bookings and payments. That permission covers very different actions. These are the defaults when the customer does not answer.

| Action | Before this rule | Legally allowed | What we claim | Decided default |
| --- | --- | --- | --- | --- |
| Card payment fails for a booked class | Retried the card three times | Retry, cancel, or hold | "Made upstairs, said plainly" | Hold the seat 24 hours, send one message, then release it. No retries |
| Customer asks to move a class, no new date chosen | Booked the next free slot | Move, cancel, or keep | Plain, no surprises | Keep the original booking and ask once |
| Class cancelled by Kiln | Offered a voucher | Refund or voucher | Fair to regulars | Full refund to the card. A voucher only if the customer picks it |
| Waiting list place opens | Booked and charged the first person | Book, offer, or skip | No surprises | Offer it for 4 hours. No answer, offer the next person. Never charge without a yes |
| Gift card expires next month | Nothing | Remind or not | Plain | One reminder, 30 days before |

The first two rows were inconsistent: one action waited, the other ran. Nobody had decided that.

# Always carried

Every booking message carries these, even when nobody asks and even when another assistant passes it on:

- The total price, in one number.
- The date and time.
- How to cancel, and until when it is free.

# Declined, even when allowed

- No automatic card retries.
- No booking or charge without an explicit yes.
- No upselling of a second class in a booking confirmation.

# Why

People book a wheel class for themselves or as a gift. A surprise charge breaks the reason they came to a small place. "If no answer arrives, nothing is executed" is the rule a system can follow; "we're friendly" is not.

See [Core idea](../../core.md) and [Who decides](../principles/who-decides.md).
