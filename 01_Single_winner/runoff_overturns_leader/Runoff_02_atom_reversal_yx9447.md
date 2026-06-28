# Runoff 02 — the atom (smallest runoff reversal)

**Level 101 · the smallest reversal there is.** Three voters. Everyone *likes* Austin
(scores 5, 4, 4 — the most stars), but two of the three *prefer* Boston, so the
Automatic Runoff hands it to **Boston**. The Scoring-Round leader **loses** — and that's
the runoff doing its job. (Boston is also the Condorcet winner — no startling case.)

The contrast: in [Runoff 01](./Runoff_01_confirms_leader_r2pvc9.md) the same machinery
*confirmed* the leader. The runoff only changes the answer when raw stars and majority
preference point at different candidates.

Two views of the **same election** (BV id [`yx9447`](https://bettervoting.com/yx9447/results)).
→ teaching guide: [`teaching_runoff_reversal.md`](./teaching_runoff_reversal.md)
· concept: [The Automatic Runoff Round](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md)
· [`Runoff Reversal`](../../00_start_here/GLOSSARY.md).

---

## The ballots (3 voters)

```
Austin, Boston, Cairo
5, 1, 2
4, 5, 0
4, 5, 0
```

Source: [`Runoff_02_atom_reversal_yx9447.yaml`](./Runoff_02_atom_reversal_yx9447.yaml)
· frozen export: [`Runoff_02_atom_reversal_yx9447_bv_export.json`](./Runoff_02_atom_reversal_yx9447_bv_export.json).

## View 1 — BetterVoting

Austin leads the Scoring Round (13) but **loses** the Automatic Runoff 1–2; BetterVoting
flags this with its "why is the top scorer different from the winner?" note.
Source: <https://bettervoting.com/yx9447/results>.

**Result — Scoring Round + Automatic Runoff:**
![BetterVoting result for yx9447: Boston wins; Scoring Round bars (Boston 11, Austin 13, Cairo 2); Automatic Runoff Boston 67% vs Austin 33%; with BetterVoting's "why is the top scoring candidate different from the winner?" popover](yx9447_result_popover.png)

**A clearer answer for this result.** BetterVoting's popover (in the screenshot above)
is vague. Here's the concrete reason Austin lost, from these three ballots: everyone
scored Austin high — a 5 and two 4s, **13 stars** in all — but two of the three voters
scored **Boston a 5 and Austin a 4**. They like Austin; they *prefer* Boston. The
scoring round can't tell a first choice from a strong second choice — a 4 looks the
same either way — so Austin's lead is built partly from two "Austin is my solid #2"
ballots. The runoff asks each voter to pick between the two finalists, and **2 of 3
pick Boston**, so Boston wins the head-to-head 2-1. Stars measure *how much* you like
each candidate; the runoff measures *who you actually prefer.*

**Automatic Runoff — raw votes:**
![Automatic Runoff bar view (raw votes): Boston 2 vs Austin 1, with the majority-threshold line Boston clears](yx9447_runoff_counts.png)

**Race Details — Scores Table + Runoff Table:**
![Race Details: Scores Table (Boston 11, Austin 13, Cairo 2) and Runoff Table (Boston 2 / 67% / 67%, Austin 1 / 33% / 33%, Equal Support 0, Total 3)](yx9447_race_details.png)


## View 2 — the LH engine

Same ballots, the full text report (the saved
[`_tabulated`](../runoff_overturns_leader_tabulated/Runoff_02_atom_reversal_yx9447_tabulated.txt)
mirror adds the funnel):

```
--- Runoff (Preference) Matrix ---
Legend: For - Equal Support - Against        * indicates Top 2 Finalist
               |  * Austin  | * Boston  |
    * Austin > |    ---     |1 - 0 - 2  |
    * Boston > | 2 - 0 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Boston — matches the STAR winner

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Austin)
 - Runoff Round Winner   = (Boston)
  Austin earned the highest total score, but Boston won the automatic
  runoff by being the head-to-head majority favorite.

Scoring Round
   Austin        -- 13 -- First place
   Boston        -- 11 -- Second place
   Cairo         --  2
 Austin and Boston advance.

Automatic Runoff Round
   Boston        -- 2 -- First place
   Austin        -- 1
   Equal Support -- 0
 Boston wins.
   Voters with a preference: 3 of 3 (no Equal Support).
   Boston 2 (67%) vs Austin 1 (33%); majority = 2.
```

> **BV ↔ LH wording.** The line `Boston 2 (67%) vs Austin 1 (33%)` is BetterVoting's
> *Runoff Votes* (2 / 1) and *% Between Finalists* (67% / 33%) folded into one line —
> LH names its denominator (`Voters with a preference`) instead of using table columns.
> [Why the words differ →](../../00_start_here/concepts/STAR_reporting/reporting_diff_BV_LH.md#same-numbers-different-words)

## The takeaway

Stars choose the two **finalists**; the runoff chooses the **winner** as the finalist
more voters prefer. Nothing was rigged — the runoff just asked the majority question
that raw totals can't, and BetterVoting and the LH engine agree on every number. In
[Runoff 01](./Runoff_01_confirms_leader_r2pvc9.md) the same machinery *confirmed* the
leader; the only difference is whether intensity and majority preference point at the
same candidate.
