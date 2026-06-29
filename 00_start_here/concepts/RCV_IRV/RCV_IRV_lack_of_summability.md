# IRV Is Not Summable — Every Ballot Must Be Counted Centrally

**One line:** **RCV-IRV cannot be tallied by adding up precinct totals.** Because the
winner depends on the *elimination order*, and the elimination order depends on every
ballot, you need the **full ballot set in one place** to run the count.

> Why this page matters: summability sounds like a dry administrative detail, but it
> drives real things voters care about — how elections are audited, whether a precinct
> can verify its own result, and whether early/partial counts mean anything. IRV
> quietly gives all of that up.

→ STAR keeps this property — see [`STAR is summable`](../STAR_Voting/STAR_summability.md).
Glossary: [`summability`](../../GLOSSARY.md).

---

## Why IRV isn't summable

IRV is a **sequence of eliminations**. Which candidate is eliminated in round 2
depends on the *combined* round-1 result of every precinct — you cannot add up
precinct winners, because a candidate who leads several precincts can still be
eliminated statewide. To know who transfers to whom, you need each individual ballot's
full ranking, centrally.

There's no small fixed-size table a precinct can publish that sums to the whole. The
only "summable" object is the entire pile of ballots.

## Worked example — two districts both won by B, merged, B *loses*

The classic demonstration (after [rangevoting.org](https://www.rangevoting.org/IrvNonAdd.html),
verified on the engine — run [`summability_demo/`](../../../01_Single_winner/summability_demo/)):

```
District A          District B          Combined (A + B)
  6 : A               6 : C               6 : A   6 : C
  4 : B               4 : B               4 : B   4 : B
  3 : C>B>A           3 : A>B>C           3 : C>B>A   3 : A>B>C

IRV: C out → B 7, A 6   IRV: A out → B 7, C 6   first-choices: A 9, C 9, B 8
  → B wins                → B wins              → B (fewest) ELIMINATED → A/C tie
```

**B wins each district outright, yet is *eliminated* when the districts are combined.**
That's the whole problem in one example: the district winners (B, B) tell you nothing
about the combined winner, and there is no precinct subtotal you could have published that
would add up to it. To get the real answer you must pool every ballot and recount from
scratch. (Contrast STAR below, where the precinct subtotals *do* add up.)

## What that costs

- **Central tabulation** — ballots (or full cast-vote records) must be gathered in one
  place, a single point of failure and a heavier, slower audit.
- **No meaningful precinct subtotals** — a precinct can't certify its own contribution
  to the outcome the way it can under summable methods.
- **Partial counts can mislead** — the candidate "ahead" in first-choices partway
  through can lose once transfers run, so early IRV numbers are easy to misread.

(This is one row on the method scorecard: *Summable / local tally? — STAR: yes,
RCV-IRV: no.* See the flagship Segment 6 in
[`whats_so_good_about_STAR_Voting.md`](../../../interviews_conversations/whats_so_good_about_STAR_Voting.md).)

## The nuance — it's IRV's count, not ranked ballots

Summability is about the **tabulation**, not the ballot. The *same* ranked ballot,
counted by a **Condorcet** method (Ranked Robin), **is** summable — via a pairwise
matrix that adds across precincts. So "ranked ballots can't be summed" is wrong; it's
**IRV's elimination count** specifically that can't. (See
[`TIPS_terminology.md`](../../TIPS_terminology.md) and the STAR counterpart,
[`STAR is summable`](../STAR_Voting/STAR_summability.md).)
