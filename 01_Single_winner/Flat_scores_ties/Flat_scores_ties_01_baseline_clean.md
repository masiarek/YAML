# Flat scores 01 — clean top two (the works-fine baseline)

**Level 101 · the control.** Before any tie, show the ordinary case: distinct totals
leave an **unambiguous top two** and a **decisive runoff**, so **no tie-break fires
anywhere.** BetterVoting and the LH engine agree trivially. This is the contrast every
later case is measured against. Cast: three fruits.

→ the cascade that the tie cases trigger: [STAR Tie-Breaking](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· concept: [The Automatic Runoff Round](../../00_start_here/STAR_Voting/STAR_Automatic_Runoff.md)
· the set: [`README`](README_Flat_scores_ties.md).

---

## The ballots (2 voters)

```
Apple, Banana, Cherry
5, 3, 1
5, 3, 1
```

Source: [`Flat_scores_ties_01_baseline_clean.yaml`](Flat_scores_ties_01_baseline_clean.yaml).

## Why nothing ties

Totals are **Apple 10, Banana 6, Cherry 2** — all different. The top two (Apple, Banana)
are unambiguous, and in the runoff every voter scored Apple above Banana, so Apple wins
outright. No head-to-head step, no "most 5s" step, no lot number. **Flat-*looking* high
scores are not the problem; an exact *tie* is.** (Note: `5,5,5,0` would **not** be clean —
that totals to a 3-way tie, which is [case 05](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md).)

## View 1 — BetterVoting

Nothing to flag: BV reports Apple the winner with the same scores and runoff. No tie-break,
so nothing to mis-report.

> 📷 _Paste the BetterVoting result screenshot here (⌘V) once built; append `_<bvid>` to
> the filenames._

## View 2 — the LH engine

```
Scoring Round
   Apple         -- 10 -- First place
   Banana        --  6 -- Second place
   Cherry        --  2
 Apple and Banana advance.

Automatic Runoff Round
   Apple         -- 2 -- First place
   Banana        -- 0
   Equal Support -- 0
 Apple wins.
```

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_01_baseline_clean_tabulated.txt).

## The takeaway

When scores are distinct, tie-breaking never runs and every tabulator agrees. Keep this
picture in mind — every case from here on changes exactly one thing (make the top scores
*equal*) and watches what each system does.
