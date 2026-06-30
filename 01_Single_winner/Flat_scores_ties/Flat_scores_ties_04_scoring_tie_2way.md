# Flat scores 04 — scoring-round tie for the 2nd finalist slot (2-way)

**Level 201 · the first scoring-round tie.** Aral leads outright; **Baikal and Crater tie
for the second finalist slot.** Now the cascade runs in the *scoring* round to decide *who
advances*: head-to-head (tied) → most 5s (tied) → **lot number** → Baikal advances. Aral
then wins the runoff cleanly. Cast: three lakes.

→ [STAR Tie-Breaking](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· concept: [The Automatic Runoff Round](../../00_start_here/STAR_Voting/STAR_Automatic_Runoff.md)
· BV: wrong finalists under ties [#1379](https://github.com/Equal-Vote/bettervoting/issues/1379),
pre-published lot rule [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063),
tie-break export [#1371](https://github.com/Equal-Vote/bettervoting/issues/1371) (closed) · [`README`](README_Flat_scores_ties.md).

---

## The ballots (3 voters)

```
Aral, Baikal, Crater
5, 4, 4
5, 4, 4
5, 0, 0
```

Source: [`Flat_scores_ties_04_scoring_tie_2way.yaml`](Flat_scores_ties_04_scoring_tie_2way.yaml).

## What LH does

Totals: **Aral 15, Baikal 8, Crater 8.** Aral is first outright; Baikal and Crater are tied
for the **second** finalist slot — and *which one advances can change the winner*, so the
tie must be broken. Cascade: **head-to-head** (Baikal vs Crater is 0–0, three Equal Support
→ tied), **most 5s** (0 = 0, tied), then **lot** → **Baikal** advances. Aral beats Baikal
3–0 in the runoff. The whole point: the engine *shows* that Baikal only edged out Crater by
lot number, so the choice is auditable.

## View 1 — BetterVoting (bug pending)

This is the family of #1379: when a tie decides *which* candidate becomes a finalist, BV
can advance a different one than the reference engine and won't say how it chose.

> 📷 _Paste the BetterVoting result screenshot here — note which candidate BV advances as
> the 2nd finalist — and append `_<bvid>` to the filenames._

## View 2 — the LH engine

```
Scoring Round
   Aral          -- 15 -- First place
   Baikal        --  8 -- Tied for second place
   Crater        --  8 -- Tied for second place
 Aral advances, but there's a two-way tie for second.

 First tiebreaker (head-to-head):  Baikal 0 = Crater 0  (Equal Support 3)  → still tied
 Second tiebreaker (most 5s):      Baikal 0 = Crater 0                     → still tied
 [Lot Number Priority] Tie among ['Baikal','Crater'] → Resolved ['Baikal'].

Automatic Runoff Round
   Aral -- 3 -- First place   Baikal -- 0   Equal Support -- 0
 Aral wins.
```

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_04_scoring_tie_2way_tabulated.txt).

## The takeaway

A scoring-round tie isn't always about the winner — here it decides the *runner-up's
seat*. LH resolves it by published lot and prints the step; an auditor can replay it. The
next case is the one where this exact mechanism changes the **winner** — and where BV gets
it wrong.
