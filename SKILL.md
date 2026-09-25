---
name: time-value-decision
description: Research and compare choices that trade money for time, convenience, energy, or certainty. Use for travel, commuting, delivery, subscriptions, outsourcing, upgrades, purchases, and other “is paying more worth it?” decisions. Can verify current facts, calculate scenarios, or challenge whether the user genuinely wants the purchase, without assigning a fixed value of time or deciding for them by default.
---

# Time Value Decision

Help the user see the trade-off clearly. Treat the calculation as a decision aid, not a universal answer.

## Choose the mode

- **Compare:** Use the information supplied, calculate the trade-off, and expose the switching point.
- **Fact Check:** When the user asks for real, current, or verified information, read [references/fact-check.md](references/fact-check.md) and research before calculating.
- **Grill Me:** Only when the user asks to be challenged, read [references/grill-me.md](references/grill-me.md) and pressure-test the desire before recommending a purchase.

Combine modes when requested. For example, verify real flight details, calculate the trade-off, then grill the user on whether the convenience is actually valuable to them.

## Build the comparison

Capture each option using the same fields when they matter:

- cash cost;
- time spent or saved;
- usable time rather than clock time alone;
- friction such as queues, transfers, luggage, coordination, fatigue, or repeated setup;
- uncertainty and the consequence of failure;
- whether the activity itself has value, such as walking, cooking, resting, or spending time with someone.

Ask up to three focused questions only when missing information could materially change the result. Otherwise proceed with clearly labeled assumptions. Never invent precise risk probabilities.

## Calculate

Use these relationships:

- `Time cost = time spent × value of time`
- `Effective cost = cash cost + time cost`
- `Break-even value of time = premium paid ÷ time saved in hours`
- `Expected risk time = probability × time consequence`

Add friction or risk to the monetary total only when the user supplies a monetary estimate or explicitly wants one. Otherwise keep those factors visible as qualitative differences.

For a numeric comparison, read [references/calculator.md](references/calculator.md) and use the bundled calculator when useful. Double-check units, especially minutes versus hours and one-way trips versus round trips.

## Test the decision

Show what changes the result:

- run sensitivity at values of time supplied by the user;
- if none are supplied, use a small illustrative range and label it as illustrative;
- identify the switching point rather than claiming one option is always best;
- test ambiguous assumptions separately, such as two journeys versus two round trips;
- distinguish arrival time from time the user can actually use;
- use a pre-mortem when uncertainty matters: “If this option turns out badly, what probably happened?”

Do not equate value of time with salary per hour. Saving an hour does not automatically create an hour of income. Do not monetize every free minute or imply that faster is inherently better.

## Present the result

Prefer this compact order:

1. assumptions that materially affect the result;
2. side-by-side option comparison;
3. break-even and sensitivity results;
4. friction, risk, and intrinsic-value factors;
5. the condition under which each option makes sense.

End with a decision lens such as: “Option A fits if certainty matters most; option B fits if saving 4,000 baht matters more and the early-arrival hours are not usable.” Do not choose for the user unless they ask. If they ask, make the recommendation conditional on the priorities they stated and explain what would reverse it.
