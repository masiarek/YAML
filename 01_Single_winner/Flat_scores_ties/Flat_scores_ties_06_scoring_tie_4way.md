# Flat scores 06 — scoring-round 4-way tie (ties at every step)

**Level 301 · the full cascade, both rounds.** Four people — Ava, Ben, Cara, Dan — tie at
10; the ties persist through **every** score-based tiebreaker; the lot picks two finalists;
and then the **runoff also ties** → lot again. A stress test that exercises the entire
tie-break ladder in both rounds and still lands deterministically on **Ava**.

> ⚠️ **BV reporting bug (pending).** When ties hit every step, BetterVoting has shown the
> wrong message **"no ballots have been cast"** even though ballots exist — tracked as
> **[BV126 / #1052](https://github.com/Equal-Vote/bettervoting/issues/1052)**. Same
> underlying gap as case 05: wrong finalists / no human-readable tie-break explanation
> [#1379](https://github.com/Equal-Vote/bettervoting/issues/1379). (The tie-break sequence
> is now in BV's JSON export — [#1371](https://github.com/Equal-Vote/bettervoting/issues/1371),
> closed.)

→ [STAR Tie-Breaking](../../00_start_here/concepts/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· [reporting true ties](../../00_start_here/concepts/STAR_reporting/reporting_ties.md) · [`README`](./README.md).

---

## The ballots (2 voters)

```
Ava, Ben, Cara, Dan, Eve
5, 5, 5, 5, 1
5, 5, 5, 5, 1
```

Source: [`Flat_scores_ties_06_scoring_tie_4way.yaml`](./Flat_scores_ties_06_scoring_tie_4way.yaml).

## What LH does

Ava, Ben, Cara, Dan all total 10 — a **four-way tie** for two finalist slots. Head-to-head:
all 0 (everyone Equal Support). Most 5s: all 2. The **lot** picks **Ava, Ben**. The runoff
Ava vs Ben is then 0–0 → highest score tied → most 5s tied → **lot** → **Ava**. Every one
of those steps is printed, so even a maximally tied election is fully auditable.

## View 1 — BetterVoting (bug pending)

Watch for the spurious **"no ballots have been cast"** message (#1052) and check which two
finalists BV advances.

> 📷 _Paste the BetterVoting result screenshot here — capture the "no ballots cast"
> message if it appears — and append `_<bvid>` to the filenames._

## View 2 — the LH engine

```
Scoring Round
   Ava -- 10 -- Tied   Ben -- 10 -- Tied   Cara -- 10 -- Tied   Dan -- 10 -- Tied   Eve -- 2
 There's a four-way tie for first.

 First tiebreaker (head-to-head):  Ava=Ben=Cara=Dan 0  (Equal Support 2)  → still tied
 Second tiebreaker (most 5s):      Ava=Ben=Cara=Dan 2                     → still tied
 [Lot Number Priority] Tie among ['Ava','Ben','Cara','Dan'] → Resolved ['Ava','Ben'].

Automatic Runoff Round
   Ava -- 0 -- Tied   Ben -- 0 -- Tied   Equal Support -- 2
 There's a two-way tie for first.
 First tiebreaker (highest score):  Ava 10 = Ben 10  → still tied
 Second tiebreaker (most 5s):       Ava  2 = Ben  2  → still tied
 [Lot Number Priority] Tie among ['Ava','Ben'] → Resolved ['Ava'].

Winner: Ava
```

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_06_scoring_tie_4way_tabulated.txt).

## The takeaway

No matter how many candidates tie or how many steps stay tied, a published lot order
terminates the cascade with a reproducible winner — and a correct report says how, not
"no ballots have been cast."
