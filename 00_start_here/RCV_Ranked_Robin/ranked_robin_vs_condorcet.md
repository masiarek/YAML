# Ranked Robin vs. "the Condorcet winner" — same animal, until there's a cycle

*A question that trips up almost everyone: aren't **Ranked Robin (RCV-RR)** and **Condorcet**
the same thing? Almost — and the gap between them is the whole lesson.*

→ Topic hub: [Condorcet efficiency](../topics/condorcet/README_condorcet.md) · cycles in depth:
[`cycle_resolution.md`](cycle_resolution.md) · the method: [`ranked_robin.md`](ranked_robin.md)

---

## The one-line answer

- A **Condorcet winner** is a candidate who beats **every** other candidate one-on-one.
  Sometimes **nobody** does (a *cycle*), so the Condorcet winner is **undefined — blank**.
- **Ranked Robin (RCV-RR / Copeland)** counts each candidate's head-to-head **wins** and
  elects whoever has the **most** (ties broken by total margin, then lot). It **always**
  produces a winner.

> **Ranked Robin = Condorcet + a built-in tiebreaker for cycles.** When a Condorcet winner
> exists, Ranked Robin elects exactly that candidate — *same animal.* When none exists,
> Condorcet is blank but Ranked Robin still names someone.

The cleanest way to see it is the **same three candidates, two different electorates.**

## Case 1 — a Condorcet winner exists → they agree

Five voters, candidates Ada / Ben / Cara
([`01_condorcet_winner.yaml`](../../01_Single_winner/condorcet_vs_ranked_robin/01_condorcet_winner.yaml)):

```
3 × Ada > Ben > Cara
2 × Ben > Ada > Cara
```

Ada beats Ben (3–2) **and** beats Cara (5–0) — Ada beats everyone, so **Ada is the
Condorcet winner**. Ranked Robin agrees, because Ada also has the most wins:

```
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–0–0         2      +6  Ben, Cara
    2  Ben        1–1–0         1      +4  Cara
    3  Cara       0–2–0         0     -10  —

Winner — Ranked Robin (RCV-RR): Ada
   beats every opponent head-to-head — the Condorcet winner.
```

**Ranked Robin = Condorcet = Ada.** No daylight between them.

## Case 2 — a cycle (rock-paper-scissors) → they part ways

Now seven voters, same three candidates
([`02_cycle_no_condorcet.yaml`](../../01_Single_winner/condorcet_vs_ranked_robin/02_cycle_no_condorcet.yaml)):

```
3 × Ada > Ben > Cara
2 × Ben > Cara > Ada
2 × Cara > Ada > Ben
```

Now the head-to-heads chase each other in a circle — exactly like rock-paper-scissors:

- **Ada beats Ben** 5–2
- **Ben beats Cara** 5–2
- **Cara beats Ada** 4–3

**Nobody beats both others, so there is NO Condorcet winner** — the Condorcet answer is
*blank*. But Ranked Robin still resolves it: everyone is 1–1, so it breaks the tie by
**total margin**, and Ada (the strongest margins) wins:

```
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–1–0         1      +2  Ben
    2  Ben        1–1–0         1      +0  Cara
    3  Cara       1–1–0         1      -2  Ada

Winner — Ranked Robin (RCV-RR): Ada
   *** 3 candidates tie on wins — a Condorcet cycle. Resolved by total margin, then lot order.
```

This is the whole distinction in one election: **Condorcet = (blank), Ranked Robin = Ada.**
(*How a cycle gets resolved is itself a design choice — Minimax, Ranked Pairs, and Schulze
each break it differently. See [`cycle_resolution.md`](cycle_resolution.md).*)

## In the wild — record 0 from the random sweep

This isn't just a contrived 3-candidate trick. It's why the **Condorcet column was blank**
in the random STAR sweep you ran (`tools_adam/random_star_divergence.py`). Take its very
first divergent election — **record 0**, 6 candidates, 5 voters
([`03_real_record0_c6_b5.yaml`](../../01_Single_winner/condorcet_vs_ranked_robin/03_real_record0_c6_b5.yaml)):

```
     A  B  C  D  E  F
#1:  3  3  0  2  4  3
#2:  3  2  3  2  4  1
#3:  4  1  2  1  0  4
#4:  2  4  5  4  1  2
#5:  0  5  0  5  2  3
```

A full 6×6 pairwise grid is hard to read, so look at the **win–loss record** instead — it
tells the story at a glance:

```
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          3–1–1       3.5      +3  D, E, F
    2  A          2–1–2         3      +1  C, D
    3  C          2–3–0         2      -1  B, D
    4  D          2–3–0         2      -1  E, F
    5  E          2–3–0         2      -1  A, C
    6  F          2–2–1       2.5      -1  C, E

Winner — Ranked Robin (RCV-RR): B  (the most head-to-head wins, 3)
```

Read the top row: **B went 3–1–1 — not 5–0.** B beats D, E, F, *ties* A, and *loses* to C.
So **no candidate beats all five rivals → there is no Condorcet winner → the column is
blank.** Ranked Robin doesn't care: B has the **most wins (3)**, so **Ranked Robin elects
B** — which also happens to be the STAR winner here.

That's the takeaway from the sweep: with only 5 ballots and 6 candidates, an undisputed
head-to-head champion rarely exists, so **Condorcet is usually blank** — but **Ranked Robin
always answers**, because "best record" always has a top.

*(The full 6×6 matrix is in the file's `_tabulated` mirror if you want it.)*

## So which should I say?

| You mean… | Say… |
|-----------|------|
| Is there an *undisputed* head-to-head champion? (may be **none**) | **Condorcet winner** |
| Who has the *best* head-to-head record? (**always** someone) | **Ranked Robin (RCV-RR)** |
| Both, when a Condorcet winner exists | they're the **same candidate** |

## Related

- [Condorcet efficiency — topic hub](../topics/condorcet/README_condorcet.md)
- [Ranked Robin (the method)](ranked_robin.md) · [Cycle resolution](cycle_resolution.md)
- [Which RCV-IRV?](../RCV_IRV/RCV_IRV_variants.md) — the BTR/Baldwin/Nanson variants are also Condorcet methods
- Generator: `STARVote_LH_tabulation_engine/tools_adam/random_star_divergence.py`

Glossary: [`Condorcet`](../GLOSSARY.md).
