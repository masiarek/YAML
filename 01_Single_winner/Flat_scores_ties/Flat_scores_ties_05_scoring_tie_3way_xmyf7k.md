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

→ the cascade: [STAR Tie-Breaking](../../00_start_here/concepts/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· why a published lot order matters: [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063),
[#1371](https://github.com/Equal-Vote/bettervoting/issues/1371)
· [reporting true ties](../../00_start_here/concepts/STAR_reporting/reporting_ties.md) · [`README`](./README.md).

---

## The ballots (2 voters)

```
A, B, C, D, E
5, 5, 5, 4, 4
5, 5, 5, 4, 4
```

Source: [`Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml`](./Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml)
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
printing each step. BV advances **C** and **A** and elects **C**, with nothing in the
export to show *why*. With no published lot rule and no exported tie-break sequence, the
result is **not reproducible** and **not auditable** — that is the bug, even more than the
specific letter.

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

Full audit copy: [`_tabulated`](../Flat_scores_ties_tabulated/Flat_scores_ties_05_scoring_tie_3way_xmyf7k_tabulated.txt).

## The takeaway

When every score-based tiebreaker ties, only a **published lot order** can produce a
result two independent systems agree on. LH has that rule and prints every step; BV
currently has neither, so it lands on a different winner and can't show its work. Until
[#1379](https://github.com/Equal-Vote/bettervoting/issues/1379) /
[#1063](https://github.com/Equal-Vote/bettervoting/issues/1063) /
[#1371](https://github.com/Equal-Vote/bettervoting/issues/1371) land, this case stays
flagged as a known divergence.
