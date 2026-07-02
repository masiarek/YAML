# Scale granularity can flip the winner (a 301 case)

*A score ballot's **resolution** — how many rungs the scale has — is a modeling
choice, not a neutral detail. Compressing a 0–9 ballot down to STAR's 0–5 can
change **who becomes a finalist**, and through that, **who wins**. This page
works one real example where it does exactly that.*

→ Companions: [the fidelity ladder](fidelity_ladder.md) · [scores vs. ranks](scores_vs_ranks.md) ·
Black Curtain lesson #5 (the 0–9 → 0–5 problem) in
[`README_black_curtain.md`](../../01_Single_winner/black_curtain/README_black_curtain.md) ·
Curriculum: [301.1 (RRV/proportional)](../CURRICULUM.md) and
[301.6 (when Score/Runoff/Condorcet disagree)](../CURRICULUM.md)

Files: [`rrv_sample_c15_b13_three-parties.yaml`](../../01_Single_winner/_main/rrv_sample_c15_b13_three-parties.yaml) ·
full report [`…_tabulated.txt`](../../01_Single_winner/_main/_main_tabulated/rrv_sample_c15_b13_three-parties_tabulated.txt)

---

## The one idea

The **fidelity ladder** is about converting *between* scores and ranks. This is a
subtler cousin: staying entirely within **scores**, but changing the scale's
**granularity** — 0–9 down to 0–5. Rescaling is monotone (it never reorders one
voter's own preferences), so you'd expect the winner to be safe. It usually is.
But STAR picks its two finalists by **summed score**, and when several candidates
are bunched in a near-tie for that second seat, quantization can nudge a different
one into the runoff — and a different finalist can win.

## The case

The example is BetterVoting.org's **Reweighted Range Voting sample election** —
three "parties" (Purple, Orange, Yellow), five candidates each, 13 voters mostly
loyal to a party (3 Purple, 6 Orange, 4 Yellow), grading on **0–9**. RRV is a
*proportional multi-winner* method; here we instead run the same ballots through
**single-winner STAR** to ask who *one* seat would go to. Orange has the most
loyal voters (6 of 13), so — no surprise — an Orange candidate wins. The
surprise is *which* one.

## On STAR's native 0–5 scale → **Orange5**

Mapping the source 0–9 scores to 0–5 with `round(x·5/9)`, the LH engine reports:

```
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Orange1       -- 31 -- First place
   Orange5       -- 30 -- Second place
   Orange3       -- 29
   Orange4       -- 29
   Orange2       -- 25
   ... (Yellow and Purple candidates trail)
 Orange1 and Orange5 advance.

Automatic Runoff Round
   Orange5       -- 4 -- First place
   Orange1       -- 3
   Equal Support -- 6
 Orange5 wins.
   Voters with a preference: 7 of 13 (6 Equal Support).
   Orange5 4 (57%) vs Orange1 3 (43%); majority = 4.
```

Note how tight the score round is: **Orange1 31, Orange5 30, Orange3 29,
Orange4 29** — four co-partisans inside a two-point band. Orange5 edges into the
second finalist slot, then wins the runoff 4–3.

## On the original 0–9 scale → **Orange1**

Summing the raw 0–9 ballots instead (the engine only accepts 0–5, so this is
counted directly from the source scores):

| Orange candidate | 0–9 total |
|---|---:|
| Orange1 | 54 |
| **Orange3** | **53** |
| **Orange5** | **53** |
| Orange4 | 52 |
| Orange2 | 45 |

Now Orange3 and Orange5 are **exactly tied at 53** for the second seat, and the
tie-break sends **Orange3** to the runoff — where **Orange1 beats Orange3, 4–3**.
So on the source scale the winner is **Orange1**, not Orange5.

## Why the winner moved

Nothing about any voter's *order* changed — rescaling is monotone. What changed is
who came **second in the score round**:

- On **0–9**, Orange3 and Orange5 tie at 53; the second finalist is decided by a
  **tiebreak** (→ Orange3).
- On **0–5**, the `round(x·5/9)` compression separates them — Orange5 lands at 30,
  Orange3 at 29 — so Orange5 takes the slot **outright**.

And the two candidates behave differently in the runoff: **Orange5 beats Orange1,
but Orange3 loses to Orange1.** Swap the finalist and you swap the champion. The
runoff round is *not* where the divergence is born — it's the **finalist
selection** upstream, made fragile by a cluster of near-tied co-partisans.

## The lesson (and the honest caveats)

- **Resolution is a design decision.** How many rungs your ballot offers (0–5,
  0–9, 0–10…) is part of the method. When the top contenders are bunched, that
  choice can pick the winner. This is the concrete, winner-flipping version of
  Black Curtain **lesson #5**, where a finer scale merely preserved a *pure-Score*
  near-tie; here it moves the **STAR** result.
- **It lives on a knife's edge — say so.** The 0–9 outcome rests on a **2nd-place
  tie** (53–53) resolved by tiebreak; the 0–5 outcome rests on a **one-point** gap.
  This is a *fragile* divergence, not a robust law — exactly the kind of case where
  you should report the assumptions, never just the winner (the methodological
  habit of [301.6](../CURRICULUM.md)).
- **It's mapping-dependent.** A different 0–9 → 0–5 rule (floor, ceiling, a custom
  table) could land differently. The fragility *is* the point: when a race is this
  close, small modeling choices are decisive.
- **Both winners are Orange.** The majority party still wins either way — STAR
  faithfully hands the seat to the 6-voter bloc. What's unstable is *which
  co-partisan*, which is precisely the internal choice a **proportional** method
  like the source RRV would instead resolve by seating several of them.

## Takeaway

When you port a real election onto a coarser score scale to teach or tabulate it,
check whether the finalists are bunched. If they are, treat the winner as
**scale-sensitive** and present both counts — as we do here — rather than quoting
one number as if the scale were free.

---

*Terminology: the source method is **RRV** (Reweighted Range Voting), a
proportional multi-winner method; this page runs its ballots through
**single-winner STAR** purely to expose the scale effect. See
[GLOSSARY.md](../GLOSSARY.md).*

# file: scale_granularity_flips_the_winner.md
