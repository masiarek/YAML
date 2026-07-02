# Runoff 06 — the runoff confirms the leader at scale (control)

**Level 101 · the closing control.** After four reversals, the reassurance: here the
Scoring-Round leader **Wren** is *also* the candidate most voters prefer, so the
Automatic Runoff **confirms** the leader, 4–1. *How much* and *how many* point at the
same candidate — no reversal. (Wren is the Condorcet winner.)

This is the bookend to [Runoff 01](Runoff_01_confirms_leader_r2pvc9.md): most of the
time the runoff just agrees with the score round. The reversals (02–05) are the
exception — the safeguard catching the cases where intensity and majority preference
diverge.

→ teaching guide: [`teaching_runoff_reversal.md`](teaching_runoff_reversal.md)
· concept: [The Automatic Runoff Round](../../00_start_here/STAR_Voting/STAR_Automatic_Runoff.md).

---

## The ballots (5 voters)

```
Wren, Yarrow, Zinnia
5, 2, 0      prefers Wren
5, 3, 1      prefers Wren
5, 2, 0      prefers Wren
4, 5, 0      prefers Yarrow
2, 1, 5      prefers Wren (over Yarrow)
```

Source: [`Runoff_06_confirms_at_scale_d664xw.yaml`](Runoff_06_confirms_at_scale_d664xw.yaml)
· frozen export: [`Runoff_06_confirms_at_scale_d664xw_bv_export.json`](Runoff_06_confirms_at_scale_d664xw_bv_export.json).

## View 1 — BetterVoting

Wren leads the Scoring Round (21) **and** wins the Automatic Runoff 4–1.
Source: <https://bettervoting.com/d664xw/results>.

**Result — Scoring Round + Automatic Runoff:**

![BetterVoting result for d664xw: Wren wins; Scoring Round bars (Wren 21, Yarrow 13, Zinnia 6); Automatic Runoff Wren 80% vs Yarrow 20% — the leader confirmed](img/d664xw_result_bars.png)

**Why there's no reversal.** Wren has the most stars (21) *and* is the head-to-head
favorite: four of the five voters score Wren above Yarrow. So *how much* and *how many*
agree, and the runoff confirms the leader. The runoff didn't change the answer — but it
asked the question, which is the safeguard. A reversal only happens when those two
point at **different** candidates; here they don't.

**The same runoff, other views (raw votes, and pie):**

![Automatic Runoff bar view (raw votes): Wren 4 vs Yarrow 1](img/d664xw_runoff_counts.png)

![Automatic Runoff pie (percentages): Wren 80% vs Yarrow 20%](img/d664xw_runoff_pie.png)

![Automatic Runoff pie (raw votes): Wren 4 vs Yarrow 1](img/d664xw_runoff_pie_counts.png)

**Race Details — Scores Table + Runoff Table:**

> 📷 _Paste the BetterVoting Race Details screenshot here (⌘V)._

## View 2 — the LH engine

Same ballots, the full text report (the saved
[`_tabulated`](runoff_overturns_leader_tabulated/Runoff_06_confirms_at_scale_d664xw_tabulated.txt)
mirror adds the funnel):

```
[Condorcet Winner]
  Condorcet Winner: Wren — matches the STAR winner

Scoring Round
   Wren          -- 21 -- First place
   Yarrow        -- 13 -- Second place
   Zinnia        --  6
 Wren and Yarrow advance.

Automatic Runoff Round
   Wren          -- 4 -- First place
   Yarrow        -- 1
   Equal Support -- 0
 Wren wins.
   Voters with a preference: 5 of 5 (no Equal Support).
   Wren 4 (80%) vs Yarrow 1 (20%); majority = 3.
```

(No "Majority Preference Enforcement" line here — that block only prints when the score
winner and the runoff winner *differ*. They agree, so it stays silent.)

> **BV ↔ LH wording.** The line `Wren 4 (80%) vs Yarrow 1 (20%)` is BetterVoting's
> *Runoff Votes* (4 / 1) and *% Between Finalists* (80% / 20%) folded into one line —
> LH names its denominator (`Voters with a preference`) instead of using table columns.
> [Why the words differ →](../../00_start_here/STAR_reporting/reporting_diff_BV_LH.md#same-numbers-different-words)

## The takeaway — and the whole set

The runoff is not biased against the leader; it *checks* the leader, and usually
confirms them. The point of the second step is the times it doesn't (Runoff_02–05),
where a passionate or broadly-liked leader on *stars* loses to the candidate more
voters actually *prefer*. Confirm or reverse, BetterVoting and the LH engine agree on
every number — and the rule is always the same: **stars find the finalists; the runoff
counts who the majority prefers.**
