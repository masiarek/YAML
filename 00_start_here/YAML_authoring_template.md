# YAML Test Case — Authoring Template

*A fill-in guide for contributing an election test case to this library. One
YAML file = one complete, reproducible test: the ballots, how to count them,
and the winner(s) the engine must produce.*

---

## The 30-second version

Only **three keys are required**. Copy, fill in, done:

```yaml
voting_method: STAR     # STAR | Approval | RankedRobin | RCV_IRV | bloc | sss | rrv | allocated
num_winners: 1          # how many seats to fill (1 = single-winner)
ballots: |-             # header row of candidate names, then one row per voter
  Ann,Bob,Cal
  5,4,0
  3,5,2
  0,3,5
expected_winners:       # not required to tabulate — but REQUIRED for a test case:
  - Bob                 # the pytest suite discovers this key and checks it
```

Run it:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py your_file.yaml
```

The engine prints the annotated count to the screen and writes a full-detail
`_tabulated.txt` sibling. If your `expected_winners` matches what the engine
elects, the file is a valid test case.

---

## The full template (copy & fill in)

Everything below `ballots:` in the minimal version still applies; this adds
the optional context and display fields, each with its meaning in a comment.
Delete any optional block you don't need.

```yaml
election_title: "Short human title — what this case shows"

scenario_description: |-
  2–6 lines of plain language: what the election demonstrates, what to look
  for in the result. Printable (shown when show_description: true, and always
  included in the _tabulated copy).

# Presenter notes (ignored by the engine; never shown to the audience).
video_script: |-
  SAY / HOW / WHY / POINT OUT / TRANSITION notes for whoever presents this.

# Output options — what the SHORT on-screen echo shows. House default below
# ("less is more"). The saved _tabulated copy always shows maximum detail
# regardless of these flags, so only turn on the section your case teaches.
options:
  show_description: false     # print scenario_description in the echo
  show_matrix: true           # the Runoff (Preference) Matrix
  matrix_finalists_only: true # true = finalists only; false = full N×N grid
  show_condorcet: false       # the [Condorcet Winner] line
  show_score_counts: false    # per-candidate score-distribution table
  show_irv: false             # the [Divergence from STAR] RCV-IRV comparison
  show_runoff_percent: true   # compact 2-line runoff summary (percentages)
  brief: true                 # collapse repetitive section headers
  collapse_ballots: true      # group identical ballots ("N × scores");
                              #   use false when each ballot is a teaching case
  count_separator: "×"        # glyph between count and ballot: × : x X

voting_method: STAR           # see the method table below
num_winners: 1

ballots: |-
  Ann,Bob,Cal
  5,4,0
  3,5,2
  0,3,5

# --- optional -------------------------------------------------------------

lot_numbers: [Cal, Ann, Bob]  # official tie-break order (highest priority
                              # first). Only consulted when the deterministic
                              # tiebreakers can't separate candidates. Omit it
                              # and the engine uses ballot column order.

eligible_voters: 100          # registered electorate (for turnout reporting)
quorum: 25                    # minimum ballots for a valid election

blocs:                        # candidate groupings for the vote-splitting check
  Allies: [Ann, Cal]

# --- the answer key (required for a test case) -----------------------------

expected_winners:
  - Bob                       # must list exactly num_winners names

# file: <your_file_name>.yaml
```

---

## Field reference

| Key | Required? | What it is |
|---|---|---|
| `voting_method` | recommended (defaults to STAR with a NOTE) | How to count — see table below. |
| `num_winners` | recommended (defaults to 1 with a NOTE) | Seats to fill. Multi-winner needs a multi-winner method. |
| `ballots` | **yes** | The ballot grid (see rules below). Must be a literal block: write `ballots: \|-` and indent every row. |
| `expected_winners` | **yes, for a test case** | Top-level list of winner name(s). This is the key the automated test suite discovers and asserts. |
| `election_title` | optional | One-line human title, printed as the report header. |
| `scenario_description` | optional | Printable context (echoed only if `show_description: true`; always in `_tabulated`). |
| `video_script` | optional | Presenter notes. Never echoed. |
| `options` | optional | On-screen display flags (see template comments). The `_tabulated` copy ignores them and always shows everything. |
| `lot_numbers` | optional | Official tie-break (lot) order, highest priority first. |
| `eligible_voters`, `quorum` | optional | Turnout / minimum-participation reporting. |
| `blocs` | optional | Named candidate groups for the vote-splitting analysis. |

## `voting_method` values

| Value | Ballot | Counts as |
|---|---|---|
| `STAR` | scores 0–5 | Score Then Automatic Runoff (single-winner default) |
| `Approval` | `0`/`1` only | Most approvals wins |
| `RankedRobin` (aka `RCV_RR`, `Copeland`, `Consensus`) | scores 0–5 (read as an order) | Head-to-head round robin; best win–loss record wins |
| `RCV_IRV` | ranked, `A>C>B` | Instant runoff (elimination rounds) |
| `bloc` | scores 0–5 | Bloc STAR (multi-winner, majoritarian) |
| `sss` | scores 0–5 | Sequentially Spent Score (proportional) |
| `rrv` | scores 0–5 | Reweighted Range Voting (proportional) |
| `allocated` | scores 0–5 | Allocated Score (proportional) |

A file whose ballots contain ranked `A>C>B` lines routes to RCV-IRV
automatically. (Rank notes inside `# comments` are ignored.)

## Ballot grid rules

- **Row 1 = candidate names**, comma-separated. Every voter row must have the
  same number of columns.
- **Scores are `0`–`5`** (Approval: `0`/`1` only).
- **Markers** — all tabulate as 0 but are reported honestly:

  | Marker | Meaning |
  |---|---|
  | `-` | blank / left unmarked |
  | `~` | race-level abstention (skipped the whole race) |
  | `&` | candidate-level abstention |
  | `?` | spoiled ballot |
  | `%` | spoiled **and** re-issued |

- **Weighted (grouped) rows**: prefix a count — `42 × 0,3,5` (separators `×`,
  `:`, `x`, `X`). House rule: weights must be **≥ 6** so a count is never
  mistaken for a 0–5 score.
- **`# comments`** are allowed at the end of any ballot row — use them to say
  what each ballot demonstrates.

## House style (so your case fits the library)

- **Keep it small.** The fewest ballots that make the point — a handful of
  individual voters beats 100 weighted ones. Scale up only if percentages or
  proportional seats genuinely need it. See
  [TIPS_choosing_voter_counts.md](TIPS_choosing_voter_counts.md).
- **Candidate names:** common, easy to say, **distinct initials in
  A, B, C… order** (Ann, Bob, Cal…), phonetically distinct, themed if you
  like. Use a fresh cast per scenario; keep the same cast across a matched
  pair of files.
- **File name:** `NN<letter>_c<candidates>_b<ballots>_short-description.yaml`
  — e.g. `03c_c6_b8_style-gallery.yaml` (6 candidates, 8 ballots).
- **Booleans** in `options:` are written `true` / `false` (long form).
- **Only feature the section your case teaches** — start from the options
  block in the template and flip on just one heavier section
  (`show_score_counts`, `show_irv`, full matrix…) if the case is *about* it.

## What happens when you get it wrong (that's fine)

The engine is the validator — it fails with a plain-language message, never a
traceback: bad YAML, missing `ballots:`, uneven column counts, out-of-range
scores, invalid characters, ranked ballots under a score method, method/seat
mismatches. Fix and re-run. (`expected_winners` itself is checked by the
pytest suite, not the engine — a wrong answer key shows up as a test failure.)

## Submitting

1. Run the file through the engine; confirm the printed winner(s).
2. Fill `expected_winners` with exactly what the engine elected.
3. Re-run — the `_tabulated.txt` sibling regenerates.
4. From `STARVote_LH_tabulation_engine/`, run
   `pytest tests/test_single_winner_positive.py` — your file is discovered
   automatically (single-winner STAR cases with `expected_winners`).

Live examples to crib from: [`01_Single_winner/`](../01_Single_winner/) —
start with `01a_c2_b1_two-candidates.yaml` (simplest) and
`03c_c6_b8_style-gallery.yaml` (every optional field in use).
