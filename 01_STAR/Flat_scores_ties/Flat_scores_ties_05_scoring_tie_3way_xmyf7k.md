# Flat scores 05 — scoring-round 3-way tie (BV555 / #1379)

> ⚠️ **The documented divergence — work in progress until BetterVoting is fixed.** This is
> the one case in the set where BV and LH **pick a different winner.** Same ballots: the LH
> engine advances **A, B** and elects **A**; BetterVoting (`xmyf7k`) advances **C, A** and
> declares **C** — and exports **no explanation** of how it broke the tie. Tracked as
> **[BV555 / #1379](https://github.com/Equal-Vote/bettervoting/issues/1379)**.

**Level 201/301.** Three candidates tie at the top of the scoring round; **every
score-based tiebreaker stays tied**; only the **lot number** can separate them. This is the
cleanest possible test of "does your tabulator break ties deterministically *and* show its
work?" — and the reference answer is A.

→ the cascade: [STAR Tie-Breaking](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· why a published lot order matters: [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063)
· export of the tie-break sequence — **added by BV, now closed**: [#1371](https://github.com/Equal-Vote/bettervoting/issues/1371)
· [reporting true ties](../../00_start_here/STAR_reporting/reporting_ties.md) · [`README`](README_Flat_scores_ties.md).

---

## The ballots (2 voters)

```
A, B, C, D, E
5, 5, 5, 4, 4
5, 5, 5, 4, 4
```

Source: [`Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml`](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml)
· BV: <https://bettervoting.com/xmyf7k/results>.

## Where the two engines diverge (the whole point)

| | LH engine (reference) | BetterVoting (`xmyf7k`) |
|---|---|---|
| Scoring-round tie | A, B, C tied at 10 | A, B, C tied at 10 |
| Tie-break shown? | **yes — every step printed** | **no explanation in JSON** |
| Finalists advanced | **A, B** (lot order) | **C, A** |
| Runoff | A vs B → tie → lot → **A** | C vs A → **C** |
| **Winner** | **A** | **C** ❌ |

Both engines see the same three-way tie. LH applies the published lot order (A, B, C, …),
advances **A** and **B**, breaks the resulting runoff tie by lot again, and elects **A** —
printing each step. The screenshot in #1379 showed BV advancing **C** and **A** and
electing **C**. BV has **added the tie-break priority sequence to its JSON export**
([#1371](https://github.com/Equal-Vote/bettervoting/issues/1371), now **closed**), so the result is now
**reproducible** — a second engine can import BV's exported order and replay it (the LH
engine already accepts an imported lot order for exactly this). What's still open is the
substance of #1379: BV using a *different* order than the reference and not showing the
tie-break in its human-readable report, plus the request for a **pre-published** lot number
rather than a post-hoc random shuffle ([#1063](https://github.com/Equal-Vote/bettervoting/issues/1063)).
**Re-verify `xmyf7k` against a fresh BV run** — the displayed winner may have changed since
the export fix.

## View 1 — BetterVoting (incorrect — bug pending)

BV elects **C**, the wrong finalist set, with no tie-break explanation.

> 📷 _Paste the BetterVoting `xmyf7k` result screenshot here (the one in #1379 showing C as
> winner). Keep the filename suffix `_xmyf7k`._

## View 2 — the LH engine (reference)

```
Scoring Round
   A             -- 10 -- Tied for first place
   B             -- 10 -- Tied for first place
   C             -- 10 -- Tied for first place
   D             --  8
   E             --  8
 There's a three-way tie for first.

 First tiebreaker (head-to-head):  A 0 = B 0 = C 0  (Equal Support 2)  → still tied
 Second tiebreaker (most 5s):      A 2 = B 2 = C 2                     → still tied
 [Lot Number Priority] Tie among ['A','B','C'] → Resolved ['A','B'].

Automatic Runoff Round
   A             -- 0 -- Tied for first place
   B             -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

 First tiebreaker (highest score):  A 10 = B 10  → still tied
 Second tiebreaker (most 5s):       A  2 = B  2  → still tied
 [Lot Number Priority] Tie among ['A','B'] → Resolved ['A'].

Winner: A
```

Full audit copy: [`_tabulated`](Flat_scores_ties_tabulated/Flat_scores_ties_05_scoring_tie_3way_xmyf7k_tabulated.txt).

## The takeaway

When every score-based tiebreaker ties, the only thing that lets two independent systems
agree is a **shared tie-break order**. LH publishes its lot order and prints every step;
BV **now exports** its tie-break sequence too ([#1371](https://github.com/Equal-Vote/bettervoting/issues/1371),
recently added), so the result can be reproduced by importing that order. What keeps this
case flagged is the rest of [#1379](https://github.com/Equal-Vote/bettervoting/issues/1379):
BV choosing different finalists than the reference here and not showing the tie-break in
its human-readable report — and the open ask for a **pre-published** lot number rather than
a random shuffle ([#1063](https://github.com/Equal-Vote/bettervoting/issues/1063)). Confirm
the current `xmyf7k` result before treating the winner divergence as live.
