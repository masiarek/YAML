# Flat scores 07 — fully flat ballots (the maximal tie + the abstention trap)

**Level 301 · the capstone.** Every voter scores **every** mountain 5. It's the maximal
tie — tied in **both** rounds, resolved entirely by lot — and it sits on top of a second
BV bug: a fully-flat ballot gets **mis-filed as an abstention** and dropped.

> ⚠️ **Two BV bugs meet here (pending).**
> 1. **Equal Support ≠ abstention.** A ballot that rates every candidate 5 is a *cast vote
>    with no preference* (**Equal Support**), but BetterVoting drops it as an **abstention** —
>    **[#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)** (see the worked
>    case in [`Runoff_07`](../runoff_overturns_leader/Runoff_07_flat_ballot_bv_bug_tf73v9.md)
>    and [`small_case_abstention_lesson`](../pet_real_bv_election/small_case_abstention_lesson.md)).
> 2. **NaN on equal ties** — **[BV200 / #1035](https://github.com/Equal-Vote/bettervoting/issues/1035)**.

→ [STAR Tie-Breaking](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· [`GLOSSARY` (Equal Support vs abstention)](../../00_start_here/GLOSSARY.md)
· [reporting true ties](../../00_start_here/STAR_reporting/reporting_ties.md) · [`README`](README.md).

---

## The ballots (2 voters)

```
Ararat, Blanc, Cook
5, 5, 5
5, 5, 5
```

Source: [`Flat_scores_ties_07_fully_flat.yaml`](Flat_scores_ties_07_fully_flat.yaml).

## What LH does

All three peaks total 10 — a three-way tie. Head-to-head: all 0 (every pair is Equal
Support). Most 5s: all 2. The **lot** advances **Ararat, Blanc**; the runoff is 0–0 → lot →
**Ararat**. Crucially, the two ballots are **counted** the whole way — they're Equal
Support, not abstentions, so they sit in the score totals and the runoff's Equal-Support
bucket. Nothing is dropped.

## View 1 — BetterVoting (bug pending)

The tell for #1407: BV's voter/ballot count comes up **short** (the fully-flat ballots
filed as abstentions) and the runoff may show **NaN** (#1035).

> 📷 _Paste the BetterVoting result screenshot here — capture the ballot count and any NaN —
> and append `_<bvid>` to the filenames._

## View 2 — the LH engine

```
Scoring Round
   Ararat -- 10 -- Tied   Blanc -- 10 -- Tied   Cook -- 10 -- Tied
 There's a three-way tie for first.
 First tiebreaker (head-to-head):  Ararat=Blanc=Cook 0  (Equal Support 2)  → still tied
 Second tiebreaker (most 5s):      Ararat=Blanc=Cook 2                     → still tied
 [Lot Number Priority] Tie among ['Ararat','Blanc','Cook'] → Resolved ['Ararat','Blanc'].

Automatic Runoff Round
   Ararat -- 0 -- Tied   Blanc -- 0 -- Tied   Equal Support -- 2
 There's a two-way tie for first.
 First tiebreaker (highest score):  Ararat 10 = Blanc 10  → still tied
 Second tiebreaker (most 5s):       Ararat  2 = Blanc  2  → still tied
 [Lot Number Priority] Tie among ['Ararat','Blanc'] → Resolved ['Ararat'].

Winner: Ararat
```

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_07_fully_flat_tabulated.txt).

## The takeaway

The maximal tie is still deterministic — lot order decides, every step shown. But it also
exposes the deeper modeling error behind several BV tickets: **treating "no preference" as
"no vote."** A fully-flat ballot is Equal Support, counts in full, and belongs in the tie —
not in the abstention pile. Fix that, and the count, the percentages, and the tie-break all
reconcile.
