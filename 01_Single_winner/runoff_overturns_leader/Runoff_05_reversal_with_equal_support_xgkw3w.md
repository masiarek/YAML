# Runoff 05 — reversal with Equal Support

**Level 201 · the first reversal where some voters have no preference.** Rosa leads
the Scoring Round (21), but two voters scored **Rosa and Sage equally** — *Equal
Support* — so they sit out the runoff. Of the **three** who did pick between the
finalists, two prefer **Sage**, so Sage wins. The runoff is decided by **3 of 5**
voters, not all five — the bridge to the two-denominator idea.

→ what an Equal Support ballot is: [`GLOSSARY`](../../00_start_here/GLOSSARY.md)
· the two denominators: [Runoff percentages](../../00_start_here/STAR_Voting/runoff_percentages.md)
· concept: [The Automatic Runoff Round](../../00_start_here/STAR_Voting/STAR_Automatic_Runoff.md)
· teaching guide: [`teaching_runoff_reversal.md`](teaching_runoff_reversal.md).

---

## The ballots (5 voters)

```
Rosa, Sage, Tulip
5, 1, 0      prefers Rosa
4, 5, 0      prefers Sage
4, 5, 0      prefers Sage
3, 3, 1      Equal Support (Rosa = Sage)
5, 5, 2      Equal Support (Rosa = Sage)
```

Source: [`Runoff_05_reversal_with_equal_support_xgkw3w.yaml`](Runoff_05_reversal_with_equal_support_xgkw3w.yaml)
· frozen export: [`Runoff_05_reversal_with_equal_support_xgkw3w_bv_export.json`](Runoff_05_reversal_with_equal_support_xgkw3w_bv_export.json).

## View 1 — BetterVoting


Rosa leads the Scoring Round (21) but **loses** the Automatic Runoff 1–2, with **2
Equal Support**. Source: <https://bettervoting.com/xgkw3w/results>.

**Result — Scoring Round + Automatic Runoff (with BetterVoting's popover):**

![BetterVoting result for xgkw3w: Sage wins; Scoring Round bars (Rosa 21, Sage 19, Tulip 3); Automatic Runoff percentage view (Sage 40%, Rosa 20%, Equal Support 40% — out of all five voters); with BetterVoting's "why is the top scoring candidate different from the winner?" popover](img/xgkw3w_result_popover.png)

**Why the denominator isn't five.** Two voters scored Rosa and Sage the **same** (3-3
and 5-5): they like both finalists equally, so they have *no preference* in this
head-to-head and are set aside as **Equal Support**. That leaves **3 voters** deciding
the runoff. Rosa still has the most stars (21) — those equal-support ballots counted
fully in the Scoring Round — but among the three who *picked*, two prefer Sage, so Sage
wins 2–1. The summary line says it exactly: **`3 of 5 (2 Equal Support)`** — a majority
of the **decided** voters, not of everyone. (Because both equal-support voters rated
Tulip, they're cast votes, not abstentions — so BetterVoting and LH agree.)

**The same runoff, other views (raw votes, and pie):**

![Automatic Runoff bar view (raw votes): Sage 2, Rosa 1, Equal Support 2](img/xgkw3w_runoff_counts.png)

![Automatic Runoff pie, % between finalists: Sage 67% vs Rosa 33%; footnote "40.0% expressed no preference between the two finalists"](img/xgkw3w_runoff_pie_pct.png)

![Automatic Runoff pie, raw votes: Sage 2 vs Rosa 1; 40% expressed no preference](img/xgkw3w_runoff_pie_counts.png)

**Race Details — Scores Table + Runoff Table:**

![Race Details: Scores Table (Rosa 21, Sage 19, Tulip 3) and Runoff Table with both denominators — Sage 2 / 40% Runoff Votes / 67% Between Finalists, Rosa 1 / 20% / 33%, Equal Support 2 / 40%, Total 5](img/xgkw3w_race_details.png)

Watch the Runoff Table here: **% Between Finalists** is out of 3 (67% / 33%), but **%
Runoff Votes** is out of all 5 — the two denominators side by side. ([Runoff
percentages](../../00_start_here/STAR_Voting/runoff_percentages.md).)

## View 2 — the LH engine

Same ballots, the full text report (the saved
[`_tabulated`](../runoff_overturns_leader_tabulated/Runoff_05_reversal_with_equal_support_xgkw3w_tabulated.txt)
mirror adds the funnel):

```
[Condorcet Winner]
  Condorcet Winner: Sage — matches the STAR winner

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Rosa)
 - Runoff Round Winner   = (Sage)
  Rosa earned the highest total score, but Sage won the automatic
  runoff by being the head-to-head majority favorite.

Scoring Round
   Rosa          -- 21 -- First place
   Sage          -- 19 -- Second place
   Tulip         --  3
 Rosa and Sage advance.

Automatic Runoff Round
   Sage          -- 2 -- First place
   Rosa          -- 1
   Equal Support -- 2
 Sage wins.
   Voters with a preference: 3 of 5 (2 Equal Support).
   Sage 2 (67%) vs Rosa 1 (33%); majority = 2.
```

> **BV ↔ LH wording.** `3 of 5 (2 Equal Support). Sage 2 (67%) vs Rosa 1 (33%)` packs
> BetterVoting's *Runoff Votes* (2 / 1), *% Between Finalists* (67% / 33%), and the
> Equal-Support count (2) into one line that names its denominator.
> [Why the words differ →](../../00_start_here/STAR_reporting/reporting_diff_BV_LH.md#same-numbers-different-words)

## The takeaway

A reversal and a real Equal-Support split in one election: the runoff sets aside the
voters with no preference between the finalists and asks the rest *how many* prefer
each. Rosa's bigger total can't override the majority of the **decided** voters, who
chose Sage. Both reports agree on every number — and now you can read the
`N of TOTAL (E Equal Support)` line for what it is.
