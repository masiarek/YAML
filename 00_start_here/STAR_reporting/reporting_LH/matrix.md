# The Preference Matrix (head-to-head) and the Condorcet check

**One line:** the **Preference Matrix** shows every candidate against every other,
one pair at a time — how many voters **prefer** each, and how many rated them
**equal**. It's how you check whether STAR's winner is also the **Condorcet winner**
(the candidate who beats everyone head-to-head).

→ Hub: [STAR Reporting](../README.md) · the full report: [How the LH engine reports](README.md) · the no-preference bucket: [Runoff percentages](../../STAR_Voting/runoff_percentages.md) · [`GLOSSARY`](../../GLOSSARY.md).

---

## Reading a cell — `For – Equal Support – Against`

Each cell reads in the direction of its **row**. For "`Banana > Apple | 3 - 4 - 1`":
**3** voters prefer Banana (*For*), **4** rate the two equally (*Equal Support*), **1**
prefers Apple (*Against*). The reverse cell mirrors it (`Apple > Banana | 1 - 4 - 3`).
The diagonal is `---`, and `*` marks the two **finalists**. The Equal Support count is
the same idea as in the runoff — ballots that scored the pair the same.

## Two candidates — the matrix is trivial

With only two candidates the matrix just **restates the runoff**, so house style sets
`show_matrix: false` for two-candidate files. For reference, it looks like:

```
               |    * A     |   * B     |
         * A > |    ---     |2 - 2 - 1  |
         * B > | 1 - 2 - 2  |   ---     |
```

`A > B | 2 - 2 - 1`: 2 prefer A, 2 Equal Support, 1 prefers B — the same 2 vs 1 that
decides the runoff (`Voters with a preference: 3 of 5 (2 Equal Support)`). Nothing new,
hence hidden by default. (→ [Runoff percentages](../../STAR_Voting/runoff_percentages.md).)

## Full N×N — every pair, and the Condorcet check

With three or more candidates the full grid earns its place — it shows match-ups the
runoff never stages (the losers against each other):

```
               |  * Apple   | * Banana  |   Cherry  |
     * Apple > |    ---     |1 - 4 - 3  |4 - 3 - 1  |
    * Banana > | 3 - 4 - 1  |   ---     |5 - 3 - 0  |
      Cherry > | 1 - 3 - 4  |0 - 3 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Banana — matches the STAR winner
```

Read down Banana's row: it beats Apple (3 vs 1) **and** Cherry (5 vs 0), so Banana
wins **every** head-to-head — the **Condorcet winner**. Here it matches the STAR
winner, which is the most uncontroversial outcome there is. When the score leader, the
runoff winner, and the Condorcet winner are the same candidate, no reasonable method
disagrees.

## The options

- **`show_matrix`** — print the matrix at all. Default `true` for single-winner
  (except two-candidate files); `false` for multi-winner (a "Top 2 Finalist" matrix is
  a single-winner idea).
- **`matrix_finalists_only`** — `true` prints only the two finalists' row/column (a
  compact check that the runoff matches the pairwise result); `false` prints the full
  N×N grid. The saved `_tabulated.txt` always forces the **full** grid.
- **`show_condorcet`** — `true` prints the `[Condorcet Winner]` line and whether it
  **matches the STAR winner**; `false` hides it (house default on screen, to keep the
  echo lean). The `_tabulated.txt` copy always includes it.

When the Condorcet winner and the STAR winner **differ**, that's the interesting case —
see [three notions of "winner"](../../STAR_Voting/STAR_three_winner_notions.md).
