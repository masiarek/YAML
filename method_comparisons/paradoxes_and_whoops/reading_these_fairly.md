# Reading these fairly — the test for an honest "whoops"

Edge cases are powerful and dangerous. With a contrived enough construction you can make
*any* voting method look ridiculous — so a gallery like this can quietly become
propaganda. This page is the guardrail. **Apply it before adding a case, and apply it to
your own favorite method first.**

## Why the danger is real

- **Every method fails something.** Arrow's theorem (no ranked method satisfies a short
  list of reasonable fairness criteria at once) and Gibbard–Satterthwaite (every method is
  manipulable by strategy) guarantee it. So "method X fails criterion Y" is *always* true
  for some Y. The honest question is never *whether* it fails, but *which* failures matter
  and *how often* they bite.
- **The strategic angle muds everyone.** Because every method is manipulable, "you can
  game it" is the cheapest attack — it applies to STAR, Approval, Condorcet, and IRV
  alike. Lead with it and you're just throwing mud.

## The four-part test

A case earns a place here when it passes all four:

1. **Structural, not measure-zero.** Does the failure occupy a *region* of realistic
   configurations, or does it need a knife-edge with absurd weights and exact ties? Center
   squeeze is a whole zone of normal spatial electorates (fair); a result that needs
   1000-to-1 weights and three-decimal scores is not.
2. **Sincere, not strategic.** Failures under *honest* voting are fair currency. If a
   critique needs coordinated strategy, **say so, loudly** — and remember the same trick
   usually works against your favorite method too.
3. **Realistic electorate.** 1-D / 2-D spatial models, natural preference distributions —
   not alien voter behavior invented to trip one method.
4. **Bonus: it really happened.** A real election (Burlington 2009, Alaska 2022) is
   evidence, not a construction. Strongest footing of all.

## Symmetry is the rule (and fairness ≠ false balance)

Hold every method to the **same** standard, with **equal prominence**:

| Method | Its honest "whoops" | Roughly how often / how bad |
|--------|---------------------|------------------------------|
| Plurality | spoilers / elects a candidate a majority opposes | common; the reason this whole field exists |
| RCV-IRV | center squeeze; non-monotonicity; exhausted ballots | structural; real cases (Burlington, Alaska) |
| **STAR** | can miss the Condorcet winner; reversal surprises people | rare (~98% Condorcet-efficient in spatial models) but structural |
| Approval | threshold strategy; bland lowest-common-denominator winner | strategy-sensitive by design |
| Condorcet / Ranked Robin | cycles (no winner without a tiebreak); ignores intensity | cycles rare with many voters; intensity-blindness is inherent |
| Borda | teaming / clone vulnerability; easy to manipulate | strategy-sensitive |

**But same standard ≠ pretending all methods are equally broken.** That's its own
distortion. Honesty means stating *frequency and severity*, with sources — "here is IRV's
failure and how often it shows up; here is STAR's analogous failure and *its* (lower)
rate." Let the proportions show; don't flatten them, and don't inflate them.

## The fairness box (paste into every case)

Every lesson in this folder ends with this block, filled in honestly:

```
> ### Reading this fairly
> - **How common:** structural region · rare-but-real · knife-edge construction
> - **Sincere or strategic:** does it need anyone to vote dishonestly?
> - **What this method does well:** the other side of the ledger
> - **The symmetric whoops:** the analogous failure in STAR / Approval / RR / IRV
```

## A gut-check before you publish

> If this example embarrassed **your favorite** method instead of your least favorite,
> would you still call it fair? If not, don't use it. If yes, you've found an honest one —
> and you should go build the one that embarrasses your favorite, too.

→ Standing house policy on terminology and not-being-a-purist:
[`TIPS_terminology.md`](../../00_start_here/TIPS_terminology.md). The even-handedness
duty is also why STAR's own limits are documented as peers, not footnotes:
[STAR's limits](../../00_start_here/STAR_Voting/STAR_Automatic_Runoff.md#what-the-runoff-buys-you--and-its-limits)
· [three winner notions](../../00_start_here/STAR_Voting/STAR_three_winner_notions.md).
