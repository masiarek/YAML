# IRV Is Not Summable — Every Ballot Must Be Counted Centrally

**One line:** **RCV-IRV cannot be tallied by adding up precinct totals.** Because the
winner depends on the *elimination order*, and the elimination order depends on every
ballot, you need the **full ballot set in one place** to run the count.

> **Applies to:** **all** sequential-elimination variants — [Hare](RCV-IRV-Hare.md),
> [BTR](RCV-IRV-BTR.md), [Coombs](RCV-IRV-Coombs.md),
> [Baldwin/Nanson](RCV-IRV-Baldwin-Nanson.md), and STV — since every one of them
> depends on elimination order. The **summable** alternatives are the pairwise
> [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) (precinct matrices just add up)
> and positional methods. See [Which RCV-IRV?](RCV_IRV_variants.md).

> Why this page matters: summability sounds like a dry administrative detail, but it
> drives real things voters care about — how elections are audited, whether a precinct
> can verify its own result, and whether early/partial counts mean anything. IRV
> quietly gives all of that up.

→ Cross-method **topic hub**: [Summability](../topics/summability/README_summability.md) (STAR / Ranked
Robin / IRV side by side). STAR keeps this property —
[`STAR is summable`](../STAR_Voting/STAR_summability.md). Glossary:
[`summability`](../GLOSSARY.md).

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
verified on the engine — run [`summability_demo/`](../../01_Single_winner/summability_demo/)):

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
[`whats_so_good_about_STAR_Voting.md`](../../interviews_conversations/whats_so_good_about_STAR_Voting.md).)

## The nuance — it's IRV's count, not ranked ballots

Summability is about the **tabulation**, not the ballot. The *same* ranked ballot,
counted by a **Condorcet** method (Ranked Robin), **is** summable — via a pairwise
matrix that adds across precincts. So "ranked ballots can't be summed" is wrong; it's
**IRV's elimination count** specifically that can't. (See
[`TIPS_terminology.md`](../TIPS_terminology.md) and the STAR counterpart,
[`STAR is summable`](../STAR_Voting/STAR_summability.md).)

### Same ballots, summed — Ranked Robin on the example above

Take the *exact* two districts IRV couldn't combine and build each one's **pairwise
matrix** (For–Against–NoPref for every pair). The matrices **add**, cell by cell:

```
                A vs B        A vs C        B vs C
District A     6 – 7 – 0     6 – 3 – 4     4 – 3 – 6
District B     3 – 4 – 6     3 – 6 – 4     7 – 6 – 0
─────────────────────────────────────────────────────
Combined       9 – 11 – 6    9 – 9 – 8    11 – 9 – 6     (= the sum)
```

From that summed matrix: **B beats A (11–9) and beats C (11–9)** → **B is the Ranked
Robin / Condorcet winner.** So the candidate who won *both* districts wins the merged
election too — and you reach it by **adding precinct tables**, never pooling ballots.
Same ranked ballots that broke IRV's count; Ranked Robin sums them and gets the
sensible answer. (Produced by the LH engine's `calculate_preference_matrix`; the
[`pref_voting` engine](../../pref_voting_tabulation_engine/README_pref_voting_tabulation_engine.md) reports the same
**Copeland = Ranked Robin** winner. Files:
[`summability_demo/`](../../01_Single_winner/summability_demo/).) **Full RR-side
treatment:** [Ranked Robin is summable](../RCV_Ranked_Robin/RCV_RR_summability.md).
