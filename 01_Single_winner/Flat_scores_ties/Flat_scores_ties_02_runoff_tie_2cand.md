# Flat scores 02 — runoff tie, two candidates (everyone equal)

**Level 101 · the smallest tie there is.** Two ice-cream flavors, both scored **5** by
every voter. Both advance (there are only two), the runoff is **0–0 Equal Support**, and
the **tie-break cascade** decides: highest score (tied) → most 5s (tied) → **lot number** →
Almond.

> ⚠️ **BV reporting bug (pending).** On equal ties and equal preferences BetterVoting can
> display **`NaN`** instead of a clean tie result — tracked as
> **[BV200 / #1035](https://github.com/Equal-Vote/bettervoting/issues/1035)**. BV **now
> exports** its tie-break sequence ([#1371](https://github.com/Equal-Vote/bettervoting/issues/1371),
> recently added), so the result is reproducible by importing that order; the remaining ask
> is a **pre-published** lot number rather than a random shuffle
> ([#1063](https://github.com/Equal-Vote/bettervoting/issues/1063)).

→ [STAR Tie-Breaking](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· [reporting true ties](../../00_start_here/STAR_reporting/reporting_ties.md)
· [`GLOSSARY` (Equal Support)](../../00_start_here/GLOSSARY.md) · [`README`](README.md).

---

## The ballots (2 voters)

```
Almond, Brownie
5, 5
5, 5
```

Source: [`Flat_scores_ties_02_runoff_tie_2cand.yaml`](Flat_scores_ties_02_runoff_tie_2cand.yaml).

## What LH does

Both flavors total 10 and both advance. In the runoff every ballot scored Almond and
Brownie **equally**, so both are **Equal Support** — the runoff is 0–0. The cascade runs:
**highest score** (10 = 10, tied), **most 5s** (2 = 2, tied), then the **lot number** picks
Almond (highest priority). Deterministic and fully explained.

## View 1 — BetterVoting (bug pending)

BV should report a clean two-way tie resolved by lot; instead watch for **`NaN`** in the
runoff display (#1035).

> 📷 _Paste the BetterVoting result screenshot here — capture the `NaN` / equal-tie
> display — and append `_<bvid>` to the filenames._

## View 2 — the LH engine

```
Scoring Round
   Almond        -- 10 -- First place
   Brownie       -- 10 -- Second place
 Almond and Brownie advance.

Automatic Runoff Round
   Almond        -- 0 -- Tied for first place
   Brownie       -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

 First tiebreaker (highest score):  Almond 10 = Brownie 10   → still tied
 Second tiebreaker (most 5s):       Almond  2 = Brownie  2   → still tied
 [Lot Number Priority] Tie among ['Almond','Brownie'] → Resolved ['Almond'].

Winner: Almond
```

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_02_runoff_tie_2cand_tabulated.txt).

## The takeaway

A pure flat ballot is a *cast vote with no preference* (Equal Support), not an
abstention — and an all-equal runoff is resolved, not undefined. The number the cascade
lands on (Almond by lot) is reproducible by anyone with the published lot order. `NaN` is a
display bug, not the math.
