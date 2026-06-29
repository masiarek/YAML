# Runoff 04 — the reversal holds at scale (67/33)

**Level 101 · the atom, blown up to a crowd.** Same shape as
[Runoff 02](./Runoff_02_atom_reversal_yx9447.md), now with nine voters: three love
**Maple** (5s) and push Maple's total to the top of the Scoring Round (39), but six
prefer **Olive**, who wins the Automatic Runoff **6–3** — a clean **2-to-1 majority**
(67 / 33). Proof a reversal isn't a small-numbers fluke. (Olive is the Condorcet winner.)

→ teaching guide: [`teaching_runoff_reversal.md`](./teaching_runoff_reversal.md)
· concept: [The Automatic Runoff Round](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md)
· [`Runoff Reversal`](../../00_start_here/GLOSSARY.md).

---

## The ballots (9 voters, two kinds)

```
Maple, Olive, Pine
6 ×  4, 5, 0     # like Maple (4), prefer Olive (5)
3 ×  5, 1, 2     # the Maple enthusiasts
```

Source: [`Runoff_04_reversal_at_scale_bfjqmg.yaml`](./Runoff_04_reversal_at_scale_bfjqmg.yaml)
· frozen export: [`Runoff_04_reversal_at_scale_bfjqmg_bv_export.json`](./Runoff_04_reversal_at_scale_bfjqmg_bv_export.json).

## View 1 — BetterVoting

Maple leads the Scoring Round (39) but **loses** the Automatic Runoff 3–6.
Source: <https://bettervoting.com/bfjqmg/results>.

**Result — Scoring Round + Automatic Runoff (with BetterVoting's popover):**

![BetterVoting result for bfjqmg: Olive wins; Scoring Round bars (Maple 39, Olive 33, Pine 6); Automatic Runoff Olive 67% vs Maple 33%; with BetterVoting's "why is the top scoring candidate different from the winner?" popover](img/bfjqmg_result_popover.png)

**Why it scales.** With three voters the reversal was a 2–1 nudge; with nine it's a
**6–3 landslide** — the same *how much vs how many* split, just louder. The three Maple
fans pile up stars (their 5s lift Maple to 39), but only three people prefer Maple. Six
prefer Olive, so the runoff goes 6–3. Adding voters in the same proportions doesn't
rescue the score leader — it makes the majority's verdict clearer.

**The same runoff, other views (percentage bars, and pie):**

![Automatic Runoff as percentage bars: Olive 67% vs Maple 33%](img/bfjqmg_runoff_pct.png)

![Automatic Runoff pie (percentages): Olive 67% vs Maple 33%; 0% expressed no preference](img/bfjqmg_runoff_pie.png)

![Automatic Runoff pie (raw votes): Olive 6 vs Maple 3](img/bfjqmg_runoff_pie_counts.png)

**Race Details — Scores Table + Runoff Table:**

![Race Details: Scores Table (Maple 39, Olive 33, Pine 6) and Runoff Table (Olive 6 / 67% / 67%, Maple 3 / 33% / 33%, Equal Support 0, Total 9)](img/bfjqmg_race_details.png)

## View 2 — the LH engine

Same ballots (collapsed as `count × scores`), the full text report (the saved
[`_tabulated`](../runoff_overturns_leader_tabulated/Runoff_04_reversal_at_scale_bfjqmg_tabulated.txt)
mirror adds the funnel):

```
[Condorcet Winner]
  Condorcet Winner: Olive — matches the STAR winner

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Maple)
 - Runoff Round Winner   = (Olive)
  Maple earned the highest total score, but Olive won the automatic
  runoff by being the head-to-head majority favorite.

Count × Maple,Olive,Pine
    6 ×     4,    5,   0
    3 ×     5,    1,   2

Scoring Round
   Maple         -- 39 -- First place
   Olive         -- 33 -- Second place
   Pine          --  6
 Maple and Olive advance.

Automatic Runoff Round
   Olive         -- 6 -- First place
   Maple         -- 3
   Equal Support -- 0
 Olive wins.
   Voters with a preference: 9 of 9 (no Equal Support).
   Olive 6 (67%) vs Maple 3 (33%); majority = 5.
```

> **BV ↔ LH wording.** The line `Olive 6 (67%) vs Maple 3 (33%)` is BetterVoting's
> *Runoff Votes* (6 / 3) and *% Between Finalists* (67% / 33%) folded into one line —
> LH names its denominator (`Voters with a preference`) instead of using table columns.
> [Why the words differ →](../../00_start_here/concepts/STAR_reporting/reporting_diff_BV_LH.md#same-numbers-different-words)

## The takeaway

The reversal isn't a quirk of tiny examples. Scale the same electorate up and the
score leader still loses — by *more*, because *how many* is a headcount and headcounts
grow with the crowd while a few enthusiasts' extra stars don't. BetterVoting and the LH
engine agree on every number.
