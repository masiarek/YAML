# 03_STAR_PR — proportional STAR (multi-winner)

The same 0–5 score ballot, counted so that seats reflect the electorate's
*proportions* instead of handing every seat to the largest bloc. Three
tabulations are represented here, all runnable on the same ballot files by
switching `voting_method:`:

| `voting_method` | Counts as |
|---|---|
| `sss` | Sequentially Spent Score — each voter has a budget of "stars" that elected candidates spend |
| `allocated` | Allocated Score — each winner "uses up" a quota of their strongest supporters |
| `rrv` | Reweighted Range Voting — ballots that already elected someone are down-weighted |

Cases live in [`_main/`](_main/) (the `02a/02b/02c` trio counts the SAME
63-ballot election three ways). Majoritarian multi-winner:
[`../02_STAR_Bloc/`](../02_STAR_Bloc/). STV, the proportional method for
*ranked* ballots, lives in [`../other_methods/`](../other_methods/).
Concept docs:
[`../00_start_here/proportional_representation/`](../00_start_here/proportional_representation/).

# file: README_03_STAR_PR.md
