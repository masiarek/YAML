# Small case — reproduce the abstention mislabel on BetterVoting (TODO: Adam)

**Goal:** capture a *real* BetterVoting result for the smallest election that shows
the bug, so we have a frozen BV artifact (not just the synthetic LH file). Pairs
with the 461-ballot pet race as the "small + large" evidence set.

The synthetic LH version already exists and shows the **correct** behavior:
[`abstention_reconciliation_min_c2_b6.yaml`](./abstention_reconciliation_min_c2_b6.yaml).
This file is the recipe to get BetterVoting's (incorrect) version next to it.

## Steps

1. **Create a STAR election on BetterVoting** — 2 candidates, e.g. `A` and `B`
   (or `Dog`/`Cat` to match the big case).
2. **Cast these ballots** (scores 0–5):

   | Ballot | A | B | what it is |
   |---|--:|--:|---|
   | 1 | 5 | 0 | prefers A |
   | 2 | 4 | 0 | prefers A |
   | 3 | 0 | 5 | prefers B |
   | 4 | **5** | **5** | **Equal Support — the key ballot** |
   | 5 | 0 | 0 | all-zero (cast, supports neither) |
   | 6 | — | — | blank (leave both unscored) — a true abstention |

3. **Read BetterVoting's result** and note `nAbstentions` / `nTallyVotes` (Race
   Details / export). **Hypothesis:** BV reports **3 abstentions** (the 5,5 + 0,0 +
   blank), i.e. it flags the engaged `5,5` voter as abstaining, and tallies 3.
4. **Export the JSON**, drop it in this folder as
   `small_abstention_c2_b6_bv_export.json`, and **convert it to YAML**:

   ```
   python YAML_library/1_positive/01_convert_json_yaml.py <exported.json>
   ```

5. **Tabulate the YAML with the LH engine** and confirm the *correct* reading
   (6 cast, 1 abstention, 3 Equal Support, A wins 2–1) — i.e. it matches the
   synthetic file above. The contrast between the two reports is the lesson.
6. **Freeze + document:** add the BV numbers to a snapshot (like
   [`BV_result_snapshot.md`](./BV_result_snapshot.md)) and cross-link from the
   lessons. Update the GitHub issue with the real small-case screenshot.

## Expected contrast (the teaching point)

| | BetterVoting (predicted) | LH engine (correct) |
|---|---:|---:|
| Ballots tallied | 3 | 6 |
| Abstentions | 3 (5,5 + 0,0 + blank) | 1 (blank only) |
| `5,5` ballot | counted as abstention ❌ | Equal Support, stars counted ✓ |
| Winner | A | A |

*Remove or update this file once the real BV export is captured.*
