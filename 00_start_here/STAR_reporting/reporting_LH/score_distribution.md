# The Score Distribution table

**One line:** the **Score Distribution** is the LH engine's breakdown of *how many
ballots gave each score* to each candidate — the raw shape behind the score totals.
It's where you can see at a glance whether a candidate is broadly liked, polarizing,
or unknown — and it keeps an honest line between an explicit **0** and a **blank**.

→ Hub: [STAR Reporting](../README_STAR_reporting.md) · the full report: [How the LH engine reports](README_reporting_LH.md) · what counts as a blank: [`GLOSSARY`](../../GLOSSARY.md).

Turn it on with `options: { show_score_counts: true }` (the saved `_tabulated.txt`
always includes it).

---

## A worked example

From the flat-scores teaching election (Apple / Banana / Cherry, 8 ballots):

```
[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  Abs  | Total   Avg
Apple   2  1  2  0  0  2    1  |    20   2.9
Banana  4  1  1  0  0  1    1  |    27   3.9
Cherry  0  0  1  1  2  3    1  |     7   1.0
```

## How to read each part

- **The `5 4 3 2 1 0` columns** count *how many ballots* gave that score. Each row
  adds up to the number of ballots: Apple = `2+1+2+0+0+2 (+1 Abs) = 8`.
- **`Abs`** = ballots that left this candidate **blank** (no score recorded). An
  explicit **`0`** is different — it's a *cast* "I rate you zero," so it sits in the
  `0` column, not in `Abs`. (Here the only blank is the one fully-blank ballot, so
  every row shows `Abs 1`.) This is the same **0-vs-blank** distinction that drives
  the [abstention discussion](../../../01_STAR/pet_real_bv_election/small_case_abstention_lesson.md).
- **`Total`** = the sum of stars = the Scoring Round number: Apple = `5·2 + 4·1 + 3·2 = 20`.
- **`Avg`** = `Total ÷ (ballots − Abs)` — the mean score among voters **who actually
  scored** this candidate (blanks excluded, explicit zeros **included**). Apple =
  `20 ÷ 7 = 2.9`. That's why the two zeros pull Apple's average down but the blank
  does not.

## What the shape tells you

- **Banana** (4 fives, total 27, avg 3.9) — broad, strong support → the winner.
- **Apple** (2 fives but also 2 zeros, avg 2.9) — liked by many, dismissed by some
  (more polarizing than Banana).
- **Cherry** (no 4s or 5s, mostly 1s and 0s, avg 1.0) — little support; finishes last.

The distribution is the **why** behind the Scoring Round totals: same totals can come
from very different ballot shapes, and this table shows which. (BetterVoting reports
the *totals* in its Scores Table; this per-score breakdown is the LH engine's.)
