# Condorcet vs. Ranked Robin — worked examples

*Three runnable Ranked Robin (RCV-RR / Copeland) elections showing the one distinction that
trips everyone up: **Ranked Robin and "the Condorcet winner" are the same answer — until
there's a cycle.** Same three candidates, two electorates, plus a real 6-candidate case.*

→ **Full lesson (the teaching write-up):**
[ranked_robin_vs_condorcet.md](../../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_condorcet.md) ·
deeper math: [the math behind Condorcet](../../00_start_here/RCV_Ranked_Robin/the_math_behind_condorcet.md)

| File | What it shows | Condorcet winner | Ranked Robin |
|------|---------------|:---:|:---:|
| [`01_condorcet_winner.yaml`](01_condorcet_winner.yaml) | a Condorcet winner exists → they **agree** | Ada | **Ada** |
| [`02_cycle_no_condorcet.yaml`](02_cycle_no_condorcet.yaml) | a rock-paper-scissors **cycle** → they part ways | *(none)* | **Ada** |
| [`03_real_record0_c6_b5.yaml`](03_real_record0_c6_b5.yaml) | real 6-cand sweep case — no Condorcet winner | *(none)* | **B** |

---

## 1. Condorcet winner exists → Ranked Robin elects it

Ada beats both rivals head-to-head, so Ada is the Condorcet winner *and* the Ranked Robin
winner. No daylight between them.

```text
Ballots:
     3 × Ada > Ben > Cara
     2 × Ben > Ada > Cara

Win–loss record (most wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–0–0         2      +6  Ben, Cara
    2  Ben        1–1–0         1      +4  Cara
    3  Cara       0–2–0         0     -10  —

Winner — Ranked Robin (RCV-RR): Ada   (beats every opponent — the Condorcet winner)
```

Full report: [`…_tabulated/01_condorcet_winner_tabulated.txt`](../condorcet_vs_ranked_robin_tabulated/01_condorcet_winner_tabulated.txt)

## 2. A cycle → no Condorcet winner, but Ranked Robin still picks one

Ada beats Ben (5–2), Ben beats Cara (5–2), Cara beats Ada (4–3) — a circle. **No candidate
beats both others, so there is no Condorcet winner.** Everyone is 1–1; Ranked Robin breaks
the tie by total margin and elects Ada.

```text
Ballots:
     3 × Ada > Ben > Cara
     2 × Ben > Cara > Ada
     2 × Cara > Ada > Ben

Win–loss record:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–1–0         1      +2  Ben
    2  Ben        1–1–0         1      +0  Cara
    3  Cara       1–1–0         1      -2  Ada

Winner — Ranked Robin (RCV-RR): Ada
   *** 3 candidates tie on wins — a Condorcet cycle. Resolved by total margin, then lot order.
```

Full report: [`…_tabulated/02_cycle_no_condorcet_tabulated.txt`](../condorcet_vs_ranked_robin_tabulated/02_cycle_no_condorcet_tabulated.txt)

## 3. The real one — record 0 from the random sweep (6 candidates)

The first divergent election from `tools_adam/random_star_divergence.py`. STAR elects **B**;
so does Ranked Robin. But these are **score** ballots, so Ranked Robin first reads them as a
ranking (equal scores stay tied, `=`). **No candidate beats all five rivals**, so the
Condorcet winner is blank — yet B has the best record (3 wins), so Ranked Robin elects B.

```text
Ballots:
   columns = A, B, C, D, E, F   (scores  →  the ranking Ranked Robin reads;  "=" = tied)
     1 × 3, 3, 0, 2, 4, 3   →   E > A=B=F > D > C
     1 × 3, 2, 3, 2, 4, 1   →   E > A=C > B=D > F
     1 × 4, 1, 2, 1, 0, 4   →   A=F > C > B=D > E
     1 × 2, 4, 5, 4, 1, 2   →   C > B=D > A=F > E
     1 × 0, 5, 0, 5, 2, 3   →   B=D > F > E > A=C

Win–loss record (top rows):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          3–1–1       3.5      +3  D, E, F      <- best record, NOT 5-0
    2  A          2–1–2         3      +1  C, D

Winner — Ranked Robin (RCV-RR): B   (the most head-to-head wins, 3)
```

B went **3–1–1, not 5–0** (it loses to C, ties A), so no one beats everyone → Condorcet is
blank. The full 6×6 pairwise grid is in the mirror:
[`…_tabulated/03_real_record0_c6_b5_tabulated.txt`](../condorcet_vs_ranked_robin_tabulated/03_real_record0_c6_b5_tabulated.txt)

---

*Regenerate any report by re-running the `.yaml` through the LH engine; the
`…_tabulated.txt` mirrors are generated siblings. Full teaching write-up:
[ranked_robin_vs_condorcet.md](../../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_condorcet.md).*
