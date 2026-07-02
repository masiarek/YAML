# STAR's Hybrid Nature — Expressive Scoring + a Majority Runoff

**One line:** STAR is deliberately a *hybrid*. It takes the **expressiveness** of a
score ballot (say *how much* you like each candidate, not just an order) and pairs it
with the **legitimacy** of a majority runoff (the winner is the one more voters
actually prefer between the top two). Score to find the finalists; majority to pick
the winner.

→ The payoff this design produces: [Runoff Reversal](../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
and [Three notions of "winner"](STAR_three_winner_notions.md).
Glossary: [`STAR`](../GLOSSARY.md).

---

## The two steps, in plain language

**STAR = Score Then Automatic Runoff.**

1. **Scoring Round.** Score each candidate from **0 to 5 stars**, like rating products
   online. Add up everyone's stars. The **two highest-scoring candidates** become the
   **Finalists**.
2. **Automatic Runoff.** Now compare *only* those two finalists. Each ballot counts as
   one full vote for whichever finalist it scored higher. The finalist preferred by
   **more voters wins**.

Two steps, both things you can do on paper, and nothing is thrown away: every ballot
is read in full, in both rounds.

## Why combine the two ideas?

Each "pure" approach has a known weakness; STAR's hybrid covers both.

- **Pure scoring (Approval / Score Voting)** is wonderfully expressive, but with only a
  sum it can hand the win to a candidate **adored by a passionate minority** over one
  **liked by a majority** — intensity can outvote numbers.
- **Pure majority / ranked methods** respect numbers, but a bare ranking throws away
  *how much* you prefer one candidate to the next, and (in the case of RCV-IRV) the
  elimination machinery brings its own
  [pathologies](../RCV_IRV/RCV_IRV_non_monotonicity.md).

STAR's move is to **use each idea for the job it's good at**: scores *measure support*
and surface the two genuine front-runners; the runoff then applies a *majority check*
so the winner can't be a minority-intense pick. You get strength-of-support **and** a
majority finish on a single, simple ballot.

## The hybrid in one tiny election

Five voters, three flavors:

```
  Almond  Brownie  Cocoa
    5       1        2      ×1
    4       5        0      ×2     (collapsed: appears twice)
```

→ run [`runoff_overturns_leader/01a_c3_b3_more-stars-fewer-voters.yaml`](../../01_STAR/runoff_overturns_leader/01a_c3_b3_more-stars-fewer-voters.yaml)

- **Scoring Round** finds the finalists: Almond (13 stars) and Brownie (11).
- **Automatic Runoff** picks the winner: 2 of 3 voters prefer **Brownie**, so Brownie
  wins 2–1 — even though Almond had more total stars.

That's the hybrid working as designed: scores *nominated* the two finalists; the
majority runoff *chose* between them. Neither half alone would land there — pure score
would crown Almond, and a method with no scores couldn't tell that Brownie was the
broadly-liked compromise.

## Where this leads

- When the scoring leader and the runoff winner **differ**, that's
  [**Runoff Reversal**](../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md) —
  the most important consequence of the hybrid design.
- When **Condorcet, Score, and Runoff** point at three different candidates, see
  [Three notions of "winner"](STAR_three_winner_notions.md).
- For where STAR sits relative to ranked methods, see
  [Scoring methods aren't RCV](../scoring-methods-vs-ranked-voting.md) and the
  step-by-step [STAR vs RCV-IRV count](../tabulation_star_vs_irv.md).

Sources: [STAR Voting (Wikipedia)](https://en.wikipedia.org/wiki/STAR_voting),
[Equal Vote Coalition — STAR Voting](https://www.starvoting.org/star).
