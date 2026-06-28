# How to Read a STAR Result Report (201)

**One line:** the engine prints a full **audit report** — matrix, divergence check,
plain-English summary, both rounds, winner. A 101 voter only needs the last three
lines; this page walks through the *whole* thing, section by section, so you can read
(and trust) any STAR result.

→ The phenomenon this example shows: [Runoff Reversal](../../../../01_Single_winner/runoff_overturns_leader/README.md).
Curriculum: [201.1 — Reading the results](../../../CURRICULUM.md). This text report is the
engine's half of a pair — the other is BetterVoting's visual display of the same race:
[BetterVoting and the LH engine](../bettervoting_and_the_engine.md). The engine upstream:
[`larryhastings/starvote` on GitHub](https://github.com/larryhastings/starvote) ·
[`starvote` on PyPI](https://pypi.org/project/starvote/).

---

## Start with the ballots (the input)

Always read the **input first**. This is `05_c3_b5_low-scores-bv1265.yaml` — a real
BetterVoting election, 5 voters, 3 candidates (A, B, C), scored 0–5:

```
A, B, C
0, 0, 4
2, 0, 0
0, 2, 3
2, 0, 0
2, 2, 0
```

Everything below is *computed from these five rows* — nothing else goes in.

## The full report

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |   * C     |
-----------------------------------------
         * A > |    ---     |3 - 0 - 2  |
         * C > | 2 - 0 - 3  |   ---     |

[Divergence from STAR]
  STAR     = A
  Approval = C   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (C)
  - Runoff Round Winner = (A)
  Candidate C earned the highest total score,
  but Candidate A won the automatic runoff by being the head-to-head majority favorite.

Scoring Round
 The two highest-scoring candidates advance to the next round.
   C             -- 7 -- First place
   A             -- 6 -- Second place
   B             -- 4
 C and A advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   C             -- 2
   Equal Support -- 0
 A wins.

Winner — STAR Voting Method (single winner)
 A
```

## Reading it, section by section

**1. Runoff (Preference) Matrix.** The head-to-head table — the summable, auditable
heart of the count (see [STAR is summable](../../STAR_Voting/STAR_summability.md)). Each cell reads
**For – Equal Support – Against** for the *row* candidate vs the *column* candidate.
So `A > … | 3 - 0 - 2` means: in A-vs-C, **3** ballots scored A over C, **0** scored
them equal, **2** scored C over A. The `*` marks the two **Finalists** (A and C). Read
the winner's row: A beats C 3–2, so A wins their head-to-head.

**2. [Divergence from STAR].** A quick cross-check against other methods. `STAR = A`
but `Approval = C` — i.e., a pure *score/approval* count (most total stars) would pick
**C**. When this line shows a difference, you're looking at a case where the scoring
total and the STAR winner disagree — the signal of a **Runoff Reversal**.

**3. Majority Preference Enforcement Principle.** The plain-English summary, and the
one sentence to quote: *"C earned the highest total score, but A won the automatic
runoff by being the head-to-head majority favorite."* This is the whole lesson in two
lines — score leader ≠ winner, because the runoff applies a majority check.

**4. Scoring Round.** Add every candidate's stars: **C 7, A 6, B 4**. The two highest
— **C and A** — become the Finalists; **B is out**. (This is one of the only three
lines a first-time voter needs.)

**5. Automatic Runoff Round.** Now compare *only* the two finalists. Each ballot is one
full vote for whichever of C/A it scored higher: **A 3, C 2**, and **Equal Support 0**
(no ballot scored A and C the same). **A wins.** Note the engine uses *Equal Support* —
the house term for a genuine no-preference ballot, **not** "equal" in the loose sense.
With `options: { show_runoff_percent: true }` (always on in the `_tabulated` copy), the
engine also prints the winner's share of the **decided** voters — the percentage that
actually settles the runoff. What that number means, and why its denominator excludes
Equal Support, is the [runoff percentages](../../STAR_Voting/runoff_percentages.md) page.

**6. Winner.** **A** — the finalist more voters preferred, even though C led on score.

## When to show which part

| Audience | Show |
|----------|------|
| **101** — first-time voter | Scoring Round + Automatic Runoff Round + Winner (3 blocks) |
| **201** — official / auditor | + the Preference Matrix and the Majority Preference summary |
| **301** — debater / theorist | + [Divergence from STAR], Condorcet checks, score distribution, tiebreakers |

That's the point of the minimal on-screen echo plus the always-full `_tabulated.txt`:
the report scales to the reader. The full report for *any* example lives in its
`_tabulated.txt` sibling; step-by-step method comparison is in
[STAR vs RCV-IRV, step by step](../../tabulation_star_vs_irv.md).
