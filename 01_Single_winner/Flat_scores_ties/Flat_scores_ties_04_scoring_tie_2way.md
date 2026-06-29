# Flat scores 04 — scoring-round tie for the 2nd finalist slot (2-way)

**Level 201 · the first scoring-round tie.** A leads outright; **B and C tie for the
second finalist slot.** Now the cascade runs in the *scoring* round to decide *who
advances*: head-to-head (tied) → most 5s (tied) → **lot number** → B advances. A then wins
the runoff cleanly.

→ [STAR Tie-Breaking](../../00_start_here/concepts/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· concept: [The Automatic Runoff Round](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md)
· BV bugs: wrong finalists under ties [#1379](https://github.com/Equal-Vote/bettervoting/issues/1379),
lot rule [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063),
JSON sequence [#1371](https://github.com/Equal-Vote/bettervoting/issues/1371) · [`README`](./README.md).

---

## The ballots (3 voters)

```
A, B, C
5, 4, 4
5, 4, 4
5, 0, 0
```

Source: [`Flat_scores_ties_04_scoring_tie_2way.yaml`](./Flat_scores_ties_04_scoring_tie_2way.yaml).

## What LH does

Totals: **A 15, B 8, C 8.** A is first outright; B and C are tied for the **second**
finalist slot — and *which one advances can change the winner*, so the tie must be broken.
Cascade: **head-to-head** (B vs C is 0–0, three Equal Support → tied), **most 5s** (0 = 0,
tied), then **lot** → **B** advances. A beats B 3–0 in the runoff. The whole point: the
engine *shows* that B only edged out C by lot number, so the choice is auditable.

## View 1 — BetterVoting (bug pending)

This is the family of #1379: when a tie decides *which* candidate becomes a finalist, BV
can advance a different one than the reference engine and won't say how it chose.

> 📷 _Paste the BetterVoting result screenshot here — note which candidate BV advances as
> the 2nd finalist — and append `_<bvid>` to the filenames._

## View 2 — the LH engine

```
Scoring Round
   A             -- 15 -- First place
   B             --  8 -- Tied for second place
   C             --  8 -- Tied for second place
 A advances, but there's a two-way tie for second.

 First tiebreaker (head-to-head):  B 0 = C 0  (Equal Support 3)  → still tied
 Second tiebreaker (most 5s):      B 0 = C 0                     → still tied
 [Lot Number Priority] Tie among ['B','C'] → Resolved ['B'].

Automatic Runoff Round
   A -- 3 -- First place   B -- 0   Equal Support -- 0
 A wins.
```

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_04_scoring_tie_2way_tabulated.txt).

## The takeaway

A scoring-round tie isn't always about the winner — here it decides the *runner-up's
seat*. LH resolves it by published lot and prints the step; an auditor can replay it. The
next case is the one where this exact mechanism changes the **winner** — and where BV gets
it wrong.
