# 05_Ranked_Robin — Ranked Robin (RCV-RR / Copeland)

Equal Vote's method for **ranked** ballots: compare every pair of candidates
head-to-head; the candidate who wins the most matchups wins (a round robin,
like a sports league). It reads the *whole* ballot — no eliminations, no
center squeeze — and elects the Condorcet winner whenever one exists.

| Where | What |
|---|---|
| [`_main/`](_main/) | `ranked_robin_consensus_center.yaml` — the worked intro: RR elects the consensus candidate IRV eliminates |
| [`condorcet_vs_ranked_robin/`](condorcet_vs_ranked_robin/) | a clean Condorcet winner, a genuine cycle (rock/paper/scissors) and how RR resolves it, and a real 0-wins record |

Same ballot, different count: RCV-IRV (elimination rounds) lives in
[`../other_methods/`](../other_methods/) and inside the comparison sets.
Concept docs: [`../00_start_here/RCV_Ranked_Robin/`](../00_start_here/RCV_Ranked_Robin/).

# file: README_05_Ranked_Robin.md
