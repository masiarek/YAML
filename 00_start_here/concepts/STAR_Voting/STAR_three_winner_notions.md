# Three Notions of "Winner" — Condorcet, Score, and Runoff

**One line:** the word *winner* isn't one thing. In a single election, three
reasonable definitions can point at **three different candidates** — and STAR's job
is to choose among them on purpose, not by accident.

→ Related: the simpler two-way case, [Runoff Reversal](../../../01_Single_winner/runoff_overturns_leader/README.md)
(score leader ≠ STAR winner). Glossary: [`Condorcet winner`](../../GLOSSARY.md).

---

## The three notions

- **Condorcet winner** — the candidate who **beats every other candidate
  one-on-one**. The "no one would rather have someone else, head-to-head" winner.
- **Score (utility) winner** — the candidate with the **most total stars**. The
  "highest overall enthusiasm" winner.
- **Runoff winner (= the STAR winner)** — the candidate the **majority prefers
  between the two finalists**. STAR uses the Scoring Round to pick the two finalists,
  then the Automatic Runoff to choose between them.

When these three agree — which is common — STAR, score, and Condorcet all name the
same person and there's nothing to discuss. The lesson is what happens when they
**don't**.

## One election, three winners

→ [`three_winners_cw_score_runoff.yaml`](../../../01_Single_winner/three_winners_cw_score_runoff.yaml)
— five voters, three candidates:

```
  Ann  Bob  Carl
   5    4    3      ×3   (love Ann, like Bob, ok Carl)
   0    3    5      ×2   (love Carl, ok Bob, reject Ann)

  Total stars:  Ann 15   Bob 18   Carl 19
```

- **Score winner — Carl (19 stars).** His two devotees max him out; he edges Bob and
  Ann on raw totals.
- **Condorcet winner — Ann.** Head-to-head she beats Bob **3–2** *and* beats Carl
  **3–2**. More voters prefer Ann than any rival, one-on-one.
- **STAR winner — Bob.** The Scoring Round sends the top two — **Carl (19)** and
  **Bob (18)** — to the Automatic Runoff. There, **3 of 5 prefer Bob to Carl**, so
  **Bob wins 3–2.** Bob is the broad compromise the majority actually lands on once
  the field is narrowed to two.

(All three are confirmed by the engine, which prints `Condorcet = Ann (differs from
STAR)` and `Carl earned the highest total score, but Bob won the automatic runoff`.)

## Why isn't this a bug?

Each method optimizes a different, defensible goal, so disagreement is information,
not error:

- **Score** rewards *intensity* — but intensity alone can let a candidate adored by a
  minority outrank a candidate liked by everyone.
- **Condorcet** rewards *pairwise dominance* — but a Condorcet winner can be almost
  nobody's favorite, and the criterion ignores *how much* voters prefer one to
  another.
- **STAR** splits the difference on purpose: **scores find the finalists, a majority
  runoff picks the winner.** It captures strength of support *and* applies a majority
  check — at the deliberate cost of not always electing the Condorcet winner.

Here Ann (Condorcet) is shut out only because she's nudged into *third by total score*
and never reaches the runoff. That's the design tradeoff in one picture: **STAR is not
a Condorcet method**, and it doesn't pretend to be — it's a *score-then-majority*
method, and Bob is exactly who that procedure is meant to elect.

## The takeaway for a debate

When someone says "but STAR didn't pick the Condorcet winner!", the honest answer
isn't a dodge — it's: *correct, and on purpose.* STAR trades guaranteed Condorcet
compliance for expressiveness plus a majority runoff. This little five-voter election
is the cleanest way to show all three notions of "winner" at once, and to be precise
about which one STAR targets.

Sources: [Condorcet criterion (Wikipedia)](https://en.wikipedia.org/wiki/Condorcet_winner_criterion),
[Utilitarian vs. majoritarian social choice (Wikipedia)](https://en.wikipedia.org/wiki/Social_welfare_function).
