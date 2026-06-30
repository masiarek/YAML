# Flat scores 08 — every ballot flat (BetterVoting counts 0)

> ⚠️ **Bug pending.** Five real votes are cast, but **BetterVoting reports 0 ballots** —
> it mis-files *every* flat ballot as an **abstention**. Each voter rated all candidates
> (just equally), so each ballot is a cast vote with **no preference** (**Equal Support**),
> not an abstention. Tracked as **[#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)**
> (abstention mis-file), with the related reporting failures
> **[BV126 / #1052](https://github.com/Equal-Vote/bettervoting/issues/1052)** ("no ballots
> have been cast") and **[BV200 / #1035](https://github.com/Equal-Vote/bettervoting/issues/1035)** (NaN).

**Level 301 · the abstention trap at full strength.** Where [case 07](Flat_scores_ties_07_fully_flat.md)
had everyone score the *same* value (all 5s), here each voter is flat at a *different*
level (1s, then 2s, … then 5s). Still every ballot is flat, so BV drops them all — and the
counted total collapses to zero. LH counts all five, sees a clean three-way tie at 15, and
resolves it by lot to **Anchovy**. Cast: three pizza toppings.

→ Equal Support vs abstention: [`GLOSSARY`](../../00_start_here/GLOSSARY.md)
· the same bug worked end-to-end: [`Runoff_07`](../runoff_overturns_leader/Runoff_07_flat_ballot_bv_bug_tf73v9.md),
[`small_case_abstention_lesson`](../pet_real_bv_election/small_case_abstention_lesson.md)
· [STAR Tie-Breaking](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) · [`README`](README_Flat_scores_ties.md).

---

## The ballots (5 voters)

```
Anchovy, Basil, Caper
1, 1, 1
2, 2, 2
3, 3, 3
4, 4, 4
5, 5, 5
```

Every row is flat — each voter likes all three toppings equally, just at a different
intensity. Totals: **Anchovy 15, Basil 15, Caper 15** (a three-way tie). Source:
[`Flat_scores_ties_08_all_flat_zero_count.yaml`](Flat_scores_ties_08_all_flat_zero_count.yaml).

## View 1 — BetterVoting (incorrect — bug pending)

The tell: BetterVoting's header/ballot count reads **0** (all five filed as abstentions),
and the runoff may show **NaN** or "no ballots have been cast."

> 📷 _Paste the BetterVoting result screenshot here — capture the **0 ballots** count — and
> append `_<bvid>` to the filenames._

## View 2 — the LH engine (reference)

All five ballots counted; each is Equal Support, not an abstention:

```
[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  | Total   Avg
Anchovy 1  1  1  1  1  0  |    15   3.0
Basil   1  1  1  1  1  0  |    15   3.0
Caper   1  1  1  1  1  0  |    15   3.0

Scoring Round
   Anchovy -- 15 -- Tied   Basil -- 15 -- Tied   Caper -- 15 -- Tied
 There's a three-way tie for first.
 First tiebreaker (head-to-head):  Anchovy=Basil=Caper 0  (Equal Support 5)  → still tied
 Second tiebreaker (most 5s):      Anchovy=Basil=Caper 1                     → still tied
 [Lot Number Priority] Tie among ['Anchovy','Basil','Caper'] → Resolved ['Anchovy','Basil'].

Automatic Runoff Round
   Anchovy -- 0 -- Tied   Basil -- 0 -- Tied   Equal Support -- 5
 There's a two-way tie for first.
 First tiebreaker (highest score):  Anchovy 15 = Basil 15  → still tied
 Second tiebreaker (most 5s):       Anchovy  1 = Basil  1  → still tied
 [Lot Number Priority] Tie among ['Anchovy','Basil'] → Resolved ['Anchovy'].

Winner: Anchovy
```

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_08_all_flat_zero_count_tabulated.txt).

## The takeaway

"Flat" is not "blank." A ballot that scores every candidate — even all at 1, or all at 5 —
is a **cast vote with no preference**, and it belongs in the count, the score totals, and
the tie. Treating "no preference" as "no vote" is what turns five real voters into a
reported zero. LH counts them and breaks the resulting tie by published lot; BV drops them
and reports nothing was cast.
