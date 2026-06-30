# Flat scores 03 — runoff tie, an even 1–1 split

**Level 201 · the other flavor of runoff tie.** Unlike case 02 (everyone *equal*), here
two voters have **real, opposing preferences**: one prefers Athens, one prefers Berlin. The
two finalists are chosen cleanly, then the runoff splits **1–1** and the cascade decides:
highest score (tied) → most 5s (tied) → **lot number** → Athens.

→ [STAR Tie-Breaking](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· [reporting true ties](../../00_start_here/STAR_reporting/reporting_ties.md)
· BV: pre-published lot rule [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063),
tie-break export [#1371](https://github.com/Equal-Vote/bettervoting/issues/1371) (closed) · [`README`](README_Flat_scores_ties.md).

---

## The ballots (2 voters)

```
Athens, Berlin, Cairo
5, 4, 0
4, 5, 0
```

Source: [`Flat_scores_ties_03_runoff_tie_split.yaml`](Flat_scores_ties_03_runoff_tie_split.yaml).

## What LH does

Athens and Berlin each total 9 (Cairo totals 0), so they advance with no scoring-round
tie. In the runoff, voter 1 prefers Athens, voter 2 prefers Berlin — a genuine **1–1
split** (no Equal Support). The cascade runs: **highest score** (9 = 9), **most 5s** (1 =
1), then **lot** → Athens. A true even split decided by the published order, not a coin
flip.

## View 1 — BetterVoting (bug pending)

BV should show a 1–1 runoff resolved by lot. BV now exports its tie-break sequence
([#1371](https://github.com/Equal-Vote/bettervoting/issues/1371), **closed**), so another
engine can import that order and reproduce *which* finalist BV picks; the open ask is a
**pre-published** lot number rather than a random shuffle (#1063).

> 📷 _Paste the BetterVoting result screenshot here; append `_<bvid>` to the filenames._

## View 2 — the LH engine

```
Scoring Round
   Athens -- 9 -- First place   Berlin -- 9 -- Second place   Cairo -- 0
 Athens and Berlin advance.

Automatic Runoff Round
   Athens        -- 1 -- Tied for first place
   Berlin        -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

 First tiebreaker (highest score):  Athens 9 = Berlin 9   → still tied
 Second tiebreaker (most 5s):       Athens 1 = Berlin 1   → still tied
 [Lot Number Priority] Tie among ['Athens','Berlin'] → Resolved ['Athens'].

Winner: Athens
```

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_03_runoff_tie_split_tabulated.txt).

## The takeaway

Two runoff ties, two different causes — **all-Equal-Support** (case 02) vs **a real even
split** (this one) — resolve through the *same* cascade to the *same* reproducible answer.
The distinction matters for reading the report (Equal Support vs a head-to-head split) but
not for how the tie is broken.
