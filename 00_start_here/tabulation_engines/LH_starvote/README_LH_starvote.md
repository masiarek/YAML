# The LH starvote engine — what it is, and what we added

*The repo's primary tabulator. It's Larry Hastings' STAR engine plus a thick
**presentation + analysis layer** of our own — the part that turns a correct
winner into a **readable, auditable report**. This page is the map; the
section-by-section walkthrough is [Reading a STAR report](reading_a_star_report.md).*

→ Cross-checks: [pref_voting (independent referee)](../cross_checking_with_pref_voting.md) ·
[BetterVoting and the engine](../bettervoting_and_the_engine.md).
Source: [`larryhastings/starvote`](https://github.com/larryhastings/starvote) ·
[PyPI](https://pypi.org/project/starvote/). Curriculum: [201.1](../../CURRICULUM.md).

---

## Credit — `starvote` is Larry Hastings' engine

The tabulation core is **[`starvote`](https://github.com/larryhastings/starvote)**,
written and maintained by **Larry Hastings**
([PyPI](https://pypi.org/project/starvote/), MIT-licensed). It's a mature,
well-tested Python implementation of **STAR Voting** *and* the whole family of
related score methods — single-winner STAR, multi-winner **Bloc STAR**, and three
proportional methods (**Allocated Score**, **Sequentially Spent Score**,
**Reweighted Range Voting**) — with a pluggable tiebreaker system, a CLI, and its
own `.starvote`/CSV file format. All the *correctness* of our results rests on
Larry's engine; everything this repo adds sits **on top of** it, never replacing
its math. When this page says "the LH engine," it means *Larry Hastings' starvote*
with our presentation layer wrapped around it — full credit for the tabulation
belongs upstream.

We use it as a **vendored fork** (a copy committed into this repo) only so the
teaching examples are reproducible against a known version; we don't patch the
algorithm. See [`FORK_NOTES.md`](../../../STARVote_LH_tabulation_engine/FORK_NOTES.md)
for the exact upstream baseline (tag `starvote-upstream-2.1.6`) and how to re-pull a
future release.

## Two layers (so you know what's "ours")

The engine is a **vendored fork** of upstream `starvote 2.1.6`, and almost
everything we describe as "our improvement" lives in the **wrapper**, not the
algorithm:

| Layer | File | What it owns |
|-------|------|--------------|
| **Upstream engine** | `starvote/` | The voting algorithm — scoring, runoff, tiebreak mechanics. We touch it almost never. |
| **Our wrapper** | `starvote_larry_hastings.py` | How elections are **loaded, run, displayed, and saved** — the reporting, the matrix, the colors, multi-method dispatch, error handling. |

So when we say the LH engine "reports better than upstream," we almost always mean
the **wrapper** ([`README_larry_hastings.md`](../../../STARVote_LH_tabulation_engine/README_larry_hastings.md)) —
not edits to Larry's code.

### Exactly what we changed in the vendored engine

The vendored `starvote/` package is kept **as close to pristine as possible.**
Compared to upstream `starvote 2.1.6` (`git diff` against tag
`starvote-upstream-2.1.6`):

- **Algorithm: unchanged.** Same `__version__` (`2.1.6`), no functions added or
  removed except one small helper, and the two files are **~97 % character-identical**
  once whitespace is ignored. The large raw line count in `git diff --stat` is almost
  all **line-reflow** (long signatures/calls re-wrapped), not logic.
- **Two new optional output toggles** (the only functional edits):
  - `print_averages` — default `False`; CLI `-a` / `--print-averages`; config key
    `print averages`. Suppresses the per-candidate averages line unless asked.
  - `print_maximum_score` — default `False`; CLI `-M` / `--print-maximum-score`;
    config key `print maximum score`. Suppresses the "Maximum score is …" line.
  - a `bool_converter` helper to parse those two config keys. Both options are only
    forwarded to method functions when they differ from the default, so reference
    method implementations don't break.

**What is *not* an engine edit** (a common misconception — these are all in the
wrapper): the `No Preference → Equal Support` relabel, the Runoff (Preference)
Matrix, `[Divergence from STAR]`, the Majority Preference Enforcement summary, and
`show_runoff_percent`. The vendored package still prints "No Preference" internally;
our wrapper renders "Equal Support" on screen. Keeping the engine pristine-but-for-the-
two-toggles is deliberate — re-pulling a future upstream release stays trivial.

To reproduce this list precisely at any time:

```bash
git diff --stat starvote-upstream-2.1.6 -- STARVote_LH_tabulation_engine/starvote/
git diff       starvote-upstream-2.1.6 -- STARVote_LH_tabulation_engine/starvote/
```

## The headline design: **echo** vs **`_tabulated`**

The single most important improvement is that every run produces **two** outputs,
tuned for two different readers:

**1. The on-screen *echo* — minimal by design.** What prints to the terminal
honors the file's own `options:`, and our house default is *less is more*: show
the rounds, the winner, and the one or two sections the example is teaching.
Clean enough to put on a slide without overwhelming a first-time voter.

**2. The saved `_tabulated.txt` mirror — always maximal.** Every run *also* writes
a plain-text copy into a sibling `<folder>_tabulated/` mirror, and that copy is
**always rendered with every analysis on** — full N×N matrix, Condorcet line,
score distribution, tiebreaker detail, the runoff funnel — *regardless of the
file's options*. It also stamps the source name, the source's last-modified time,
and when tabulation ran, so a stale record is obvious at a glance.

The payoff: **the on-screen demo stays clean while the saved record stays
complete.** You never have to choose between a readable echo and a full audit
trail — you get the right one in each place. (This is why house YAML files carry
a deliberately *minimal* `options:` block: the mirror forces full detail anyway,
so hand-maxing the echo just adds noise.)

## What the report adds on top of "the winner is X"

Beyond the raw result, the wrapper renders the parts that make a STAR result
*trustworthy and teachable*:

- **Runoff (Preference) Matrix** — the head-to-head / pairwise grid, the summable
  heart of the count (`For – Equal Support – Against` per cell). See
  [STAR is summable](../../STAR_Voting/STAR_summability.md).
- **Majority Preference Enforcement Principle** — a plain-English sentence naming
  *why* the runoff winner beat the score leader when they differ. The whole
  Runoff-Reversal lesson in two lines.
- **`[Divergence from STAR]`** — a quick cross-check that flags when Approval / a
  pure score count, or RCV-IRV, would pick someone else; it prints whenever
  methods disagree, so comparative demos keep their punch even with the minimal echo.
- **Self-reconciling runoff line** (`show_runoff_percent`) — a compact two-line
  summary of the winner's share of the **decided** voters, stated against the
  total ballots with the Equal Support gap named inline so the denominator never
  has to be inferred; the `_tabulated` copy expands it into a "Runoff math" funnel.
  Details: [runoff percentages](../../STAR_Voting/runoff_percentages.md).
- **Score distribution, Condorcet line, tiebreaker rounds** — on demand on screen,
  always in the mirror. The **lot-number tiebreak cascade** (head-to-head → most
  5s → lot order) is shown step by step so a tie's resolution is auditable.
- **Color palette + round separators** — distinct colors per phase (scoring,
  runoff, winner), mirroring the matrix legend; auto-off when piped to a file or
  under `NO_COLOR`, so the saved text stays clean.

## One engine, many methods (auto-dispatch)

The wrapper reads `voting_method` and routes to the right tabulator, so the *same*
command and the *same* `_tabulated` discipline cover the whole family:

- **STAR** (single), **Bloc STAR**, and proportional **Allocated / SSS / RRV** (multi).
- **RCV-IRV (Hare)** — ranked ballots (`A>B>C`) route to the vendored RCV-IRV engine.
- **Approval** — single or explicit multi-winner.
- **Ranked Robin (RCV-RR / Copeland)** — *first-class*: `voting_method: RankedRobin`
  (aliases `RCV_RR` / `Copeland` / `Consensus`) prints the round-robin report
  (ballots + pairwise table + win-loss record), flags a Condorcet cycle, and writes
  its own `_tabulated` mirror — it does **not** fall through to the IRV rounds.
  See [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md).

It also runs an extra **`blocs:` vote-splitting check** and supports **quorum** /
eligible-voter accounting on STAR races.

## Input ergonomics & clear errors

- Tolerant loader: flat files, a single `election:` wrapper, or a `races:` list;
  weighted ballots (`42 × 5,4,3,2`), and zero-scoring **markers** (`-` blank,
  `~` race abstention, `&` candidate abstention, `?` spoiled, `%` reissued).
- It **errors clearly — no tracebacks** — for the common mistakes: bad YAML, a
  missing `ballots:` block (it prints the template), wrong column counts,
  out-of-range scores, ranked ballots under a score method, and method/seats
  mismatches. A missing `voting_method` / `num_winners` is a non-fatal NOTE.

## Trust, but verify

Correct *and* readable isn't the same as *self-certified*. The repo's third
engine wraps Eric Pacuit's `pref_voting` as an **independent referee** and
confirms the LH engine's Condorcet / IRV / Plurality / Copeland picks across the
whole library (currently **0 mismatches**):
[cross-checking with pref_voting](../cross_checking_with_pref_voting.md).

## Related pages

- [Reading a STAR report](reading_a_star_report.md) — the section-by-section walkthrough.
- [BetterVoting and the LH engine](../bettervoting_and_the_engine.md) — the visual half of the same race.
- [Runoff Reversal](../../../01_Single_winner/runoff_overturns_leader/README_runoff_overturns_leader.md) — the phenomenon the report is built to expose.
- [`README_larry_hastings.md`](../../../STARVote_LH_tabulation_engine/README_larry_hastings.md) · [`FORK_NOTES.md`](../../../STARVote_LH_tabulation_engine/FORK_NOTES.md) — the engine docs themselves.
