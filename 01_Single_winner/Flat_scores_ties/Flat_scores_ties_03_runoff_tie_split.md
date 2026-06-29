# Flat scores 03 — runoff tie, an even 1–1 split

**Level 201 · the other flavor of runoff tie.** Unlike case 02 (everyone *equal*), here
two voters have **real, opposing preferences**: one prefers A, one prefers B. The two
finalists are chosen cleanly, then the runoff splits **1–1** and the cascade decides:
highest score (tied) → most 5s (tied) → **lot number** → A.

→ [STAR Tie-Breaking](../../00_start_here/concepts/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· [reporting true ties](../../00_start_here/concepts/STAR_reporting/reporting_ties.md)
· BV bugs: lot rule [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063),
JSON sequence [#1371](https://github.com/Equal-Vote/bettervoting/issues/1371) · [`README`](./README.md).

---

## The ballots (2 voters)

```
A, B, C
5, 4, 0
4, 5, 0
```

Source: [`Flat_scores_ties_03_runoff_tie_split.yaml`](./Flat_scores_ties_03_runoff_tie_split.yaml).

## What LH does

A and B each total 9 (C totals 0), so A, B advance with no scoring-round tie. In the
runoff, voter 1 prefers A, voter 2 prefers B — a genuine **1–1 split** (no Equal Support).
The cascade runs: **highest score** (9 = 9), **most 5s** (1 = 1), then **lot** → A. This is a
true even split decided by the published order, not a coin flip.

## View 1 — BetterVoting (bug pending)

BV should show a 1–1 runoff resolved by lot — but with no published lot rule (#1063) and
no exported sequence (#1371), another engine can't reproduce *which* finalist BV picks.

> 📷 _Paste the BetterVoting result screenshot here; append `_<bvid>` to the filenames._

## View 2 — the LH engine

```
Scoring Round
   A -- 9 -- First place   B -- 9 -- Second place   C -- 0
 A and B advance.

Automatic Runoff Round
   A             -- 1 -- Tied for first place
   B             -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

 First tiebreaker (highest score):  A 9 = B 9   → still tied
 Second tiebreaker (most 5s):       A 1 = B 1   → still tied
 [Lot Number Priority] Tie among ['A','B'] → Resolved ['A'].

Winner: A
```

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_03_runoff_tie_split_tabulated.txt).

## The takeaway

Two runoff ties, two different causes — **all-Equal-Support** (case 02) vs **a real even
split** (this one) — resolve through the *same* cascade to the *same* reproducible answer.
The distinction matters for reading the report (Equal Support vs a head-to-head split) but
not for how the tie is broken.
