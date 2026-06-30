# LH reporting options — what each `options:` flag shows

**One line:** the `options:` block in a YAML election controls **what the on-screen
report shows** — it changes the *display*, never the result. (The saved
`_tabulated.txt` ignores these and always renders everything; house default on
screen is "less is more.")

→ Up: [How the LH engine reports](README_reporting_LH.md) · hub: [STAR Reporting](../README_STAR_reporting.md) · house defaults: [`CLAUDE.md`](../../../CLAUDE.md).

---

## The block, option by option

This is the block from the 3-candidate demo
([`flat_scores_abstention_c3_b8.yaml`](../../../01_Single_winner/pet_real_bv_election/flat_scores_abstention_c3_b8.yaml)):

```yaml
options:
  show_matrix: true            # print the head-to-head Preference Matrix
  matrix_finalists_only: true  # just the top-2 finalists (not the full N×N grid)
  show_condorcet: false        # hide the [Condorcet Winner] line
  show_score_counts: false     # hide the [Score Distribution] table
  show_irv: false              # hide the [Divergence from STAR] RCV-IRV comparison
  brief: true                  # collapse the repetitive "[STAR Voting: …]" headers
  collapse_ballots: false      # one row per voter (don't group identical ballots)
  show_runoff_percent: true    # print the self-reconciling runoff line
```

| Option | What it adds/removes from the report | Deep dive |
|---|---|---|
| `show_matrix` | the **Preference Matrix** (`For – Equal Support – Against`) | [matrix](matrix.md) |
| `matrix_finalists_only` | `true` = only the two finalists' row/col; `false` = full N×N grid | [matrix](matrix.md) |
| `show_condorcet` | the `[Condorcet Winner]` line and whether it matches the STAR winner | [matrix](matrix.md) |
| `show_score_counts` | the `[Score Distribution]` table (per-score counts, Total, Avg) | [score distribution](score_distribution.md) |
| `show_irv` | the `[Divergence from STAR]` block comparing the RCV-IRV result | — |
| `brief` | `true` collapses repeated section headers so the report is shorter | — |
| `collapse_ballots` | `false` lists every ballot; `true` groups identical ones as `count × scores` | — |
| `show_runoff_percent` | the `Voters with a preference: N of TOTAL …` line | [runoff percentages](../../STAR_Voting/runoff_percentages.md) |

## What this block produces

With the values above, the on-screen report shows: the **finalists-only matrix**, the
ballots **one per row**, both rounds (headers collapsed by `brief`), and the
**runoff-percentage line** — but **no** Score Distribution, **no** Condorcet line, and
**no** IRV divergence. Turning `show_score_counts` and `show_condorcet` on (as the
demo file now does) adds those two sections back; that's the only difference between a
lean teaching echo and a fuller study render.

## Two things that never change with options

1. **The winner and all the numbers** — options only hide or show sections, never alter
   the tabulation.
2. **The `_tabulated.txt` mirror** — it always forces every analysis on (full matrix,
   Condorcet, score counts, IRV, the runoff funnel), so the saved audit copy is
   complete regardless of what the on-screen echo chose to show.

The recommended minimal block and the per-option house defaults live in
[`CLAUDE.md`](../../../CLAUDE.md); the full report section-by-section is
[Reading a STAR report](../../tabulation_engines/LH_starvote/reading_a_star_report.md).
