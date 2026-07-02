# Ranked Robin Is Summable — the Pairwise Matrix Adds

**One line:** **RCV-RR (Ranked Robin / Copeland) is precinct-summable.** Its whole tally is
the **pairwise matrix** — for every pair of candidates, how many ballots rank A over B,
B over A, or neither — and those matrices **add across precincts**. So the *same ranked
ballot* IRV must count centrally, Ranked Robin can tally locally and add up.

→ Cross-method **topic hub**: [Summability](../topics/summability/README_summability.md)
· the method itself: [Ranked Robin](ranked_robin.md)
· the contrast — [IRV is *not* summable](../RCV_IRV/RCV_IRV_lack_of_summability.md)
· the score-method counterpart: [STAR is summable](../STAR_Voting/STAR_summability.md)
· Glossary: [`summability`](../GLOSSARY.md).

---

## Why it's summable

Ranked Robin's winner is read entirely from the **pairwise (For / Against / No-preference)
matrix**: most head-to-head wins takes it. That matrix is a small fixed-size table (C×C),
and each precinct can build its own and publish it — the statewide matrix is just the
**sum**. No elimination order, no transfers, nothing that depends on the *other* precincts'
ballots. (This is the very property [IRV lacks](../RCV_IRV/RCV_IRV_lack_of_summability.md):
summability is about the **count**, not the ballot.)

## Worked example — the same ballots IRV couldn't combine

Take the [two districts IRV can't sum](../RCV_IRV/RCV_IRV_lack_of_summability.md#worked-example--two-districts-both-won-by-b-merged-b-loses)
(B wins both, but is *eliminated* when merged). Count them with Ranked Robin and the
pairwise matrices add cell by cell — run [`summability_demo/`](../../method_comparisons/summability_demo):

```
                A vs B        A vs C        B vs C
District A     6 – 7 – 0     6 – 3 – 4     4 – 3 – 6
District B     3 – 4 – 6     3 – 6 – 4     7 – 6 – 0
─────────────────────────────────────────────────────
Combined       9 – 11 – 6    9 – 9 – 8    11 – 9 – 6     (= the sum)
```

From the summed matrix: **B beats A (11–9) and beats C (11–9)** → **B is the Ranked Robin /
Condorcet winner.** The candidate who won *both* districts wins the merge too — reached by
**adding precinct tables**, never pooling ballots. (Same ranked ballots that broke IRV's
count.)

## Tabulate & verify it

The LH engine computes the matrix (`calculate_preference_matrix`); the
[`pref_voting` engine](../../pref_voting_tabulation_engine/README_pref_voting_tabulation_engine.md) reports the
**Copeland = Ranked Robin** winner and is itself
[cross-checked](../tabulation_engines/cross_checking_with_pref_voting.md) against the LH
engine — so the summable artifact is independently confirmed.

## The nuance — same as STAR, opposite of IRV

| | summable? | the artifact that adds |
|---|:--:|---|
| STAR | ✅ | score totals + pairwise matrix |
| **Ranked Robin / RCV-RR** | ✅ | the pairwise matrix |
| RCV-IRV | ❌ | none — needs every ballot centrally |

Because Ranked Robin keeps a fixed-size, additive table, it's **precinct-auditable** and
supports meaningful partial counts — two things IRV gives up.
