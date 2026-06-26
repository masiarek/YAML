# CLAUDE.md — working guidance for this repo

Standing instructions for Claude when working in this project. Prefer the
canonical docs in `00_start_here/` over memory; this file is the index + the
non-obvious house rules.

## What this is
A **STAR Voting education** repo built on a fork of Larry Hastings' `starvote`
(single-winner STAR engine + extra reporting), plus a vendored RCV-IRV engine,
example YAML elections, teaching docs, and Larry↔Adam conversation scripts.
Audience: voters, presenters, and debaters learning/teaching STAR.

---

## File access (standing permission from Adam)

Adam grants Claude permission to **read, edit, and delete** files anywhere under
`/Volumes/T7/Voting/Larry Hastings/YAML` (this repo). No need to ask before
modifying or removing files here as part of a requested task. (Note: file
*deletion* is also gated by the app's permission layer, so a new session may
still prompt once to enable it — approve and proceed.)

---

## Terminology policy (important — keep it consistent & correct)

**Background:** "RCV" is widely used loosely to mean IRV (FairVote-era usage that
also trained most AIs to be sloppy). We meet people where they are, but we stay
precise. The key idea: **RCV names a BALLOT (ranked); IRV names one TABULATION of
it.** Other tabulations of the *same* ranked ballot: **Ranked Robin** (Condorcet
/ "consensus"), **STV** (proportional).

**House style:**
- **Default to `RCV-IRV`** in this repo's method comparisons, engine output, and
  debate/teaching docs. Unambiguous, and already the engine's term.
- **Use `IRV`** in technical/critical passages — center squeeze, exhausted
  ballots, non-monotonicity are **IRV-specific**, *not* properties of all ranked
  ballots (Ranked Robin isn't squeezed). Saying "RCV does X" there is imprecise
  and an easy target.
- **Reserve bare `RCV`** for "the ranked-ballot family," and say so when used that
  way.
- **Name `Ranked Robin` / `STV`** explicitly; never fold them into "RCV" = IRV.
- **Don't be a purist who derails.** When others use "RCV" loosely, keep their
  word, correct once, move on. Don't fight the wind.

**US-usage caveat (the nuance):** `RCV-IRV` is a deliberate *house* compound, **not
standard US usage** — appending "IRV" can look odd or confusing to a general
public audience, who only know "RCV." So:
- **Technical / debate / engine / docs → `RCV-IRV` (or `IRV`).** Precision wins.
- **Public-facing copy (slides, intro talk) → "RCV" is fine**, but clarify *once*
  on first mention: e.g. *"RCV — ranked ballots counted by instant runoff (IRV)."*
  Then use the familiar word.

Family tree, when-to-use table, and glossary are canonical — **do not restate the
taxonomy from memory:** see `00_start_here/TIPS_terminology.md` and `GLOSSARY.md`.

**Other voting-term canon:**
- **STAR** = Score Then Automatic Runoff (a *score* ballot + that tabulation; the
  same ballot can be Approval / Score / Proportional STAR).
- **Equal Support** is the canonical label for the no-preference runoff bucket
  (matrix legend *and* runoff) — printed **plain**, just "Equal Support". The aka
  (Equal Preference / No Preference) is documented once in `GLOSSARY.md`, **not**
  echoed on every runoff line. Do **not** reintroduce "Equal Preference" as the
  lead term.
- **Favorite Betrayal Criterion ≠ Later-No-Harm** — keep distinct. Neither STAR
  nor IRV is FBC-compliant; RCV-IRV fails it structurally (center squeeze), STAR
  only in rare constructions. See `interviews_conversations/favorite_betrayal_voting_301.md`.
- Spelling: **Bucklin** (not "Buckling"). **Hare ≈ IRV** single-winner, **STV**
  multi-winner. Borda & Bucklin are ranked but **not** Condorcet.

---

## Repo conventions (so output stays consistent)
- **YAML `options:` booleans → `true` / `false`** (parser also accepts t/f/y/n/etc.,
  but house style is the long form).
- **Echo-to-screen `options:` — house default is "less is more."** The on-screen
  echo should be minimal; the saved `_tabulated` copy already renders **maximum
  info automatically** (engine forces every analysis on, regardless of the file's
  options — don't hand-set that). Single-winner default block:

  ```
  options:
    show_description: false
    show_matrix: true
    matrix_finalists_only: true
    show_condorcet: false
    show_score_counts: false
    show_irv: false
    brief: true
    collapse_ballots: true
    count_separator: "×"
  ```

  **Multi-winner** uses the same block but with `show_matrix: false` and
  `matrix_finalists_only: false` (a "Top 2 Finalist" matrix is a single-winner
  concept and prints misleadingly for PR/Bloc). **Exceptions:** the options-demo
  files (`04b_…display-options-all`, `options_examples`) keep their illustrative
  all-on settings — they exist to showcase options; and **two-candidate intro
  files set `show_matrix: false`** — with only two candidates the finalists matrix
  is trivial (it just echoes the runoff). The `[Divergence from STAR]`
  block prints whenever methods differ regardless of these flags, so comparative
  demos keep their punch on screen even with the minimal block.
- **`show_description`**: per the block above, default `false` (clean demo —
  description stays in the file and the always-full `_tabulated` copy, hidden on
  screen). Flip to `true` only for a deliberate study/reference render.
- **Voter counts — keep examples SMALL.** Default to the *fewest ballots* that
  make the point; prefer **individual ballots** (one row per voter, a handful of
  them) over large weighted blocs. A 3-voter example that shows the effect beats a
  100-voter one. Only scale up when a larger electorate is genuinely essential
  (e.g., percentages or proportional seats). When you *do* weight, `Count` values
  must be **≥ 6** (avoid collision with 0–5 scores); scaling all weights ×N
  preserves STAR/proportional winners. See `TIPS_choosing_voter_counts.md`.
- **Candidate names — a fresh, easy cast per scenario; the same cast within one.**
  Prefer a *new* set of names for each scenario (memorable beats uniform — "the
  Ada/Ben/Cara split," "the Tennessee cities") over one fixed roster. Four rules:
  (1) **common and easy to say** — no obscure or confusable names (the "Cy" problem);
  (2) **distinct initials, in order** — A, B, C, D… so names line up with the ballot
  columns and reading order; (3) **phonetically distinct within a scenario** — avoid
  rhyming/blurring pairs (Dana/Hana, Ben/Glen) that don't carry when spoken aloud in a
  recording; (4) **use a theme when one fits** (Star Wars, cities, flavors) — that's
  the best kind of variety. **Variety _between_ scenarios, consistency _within_:** a
  matched pair or family (e.g. `05a`/`05b`) keeps the *same* cast — it's the same
  election with one thing changed, so new names would imply a different election. Use
  bare `A/B/C/D` only for purely abstract/academic illustrations where names are noise.
- **Markers (all tabulate as 0):** `-` blank · `~` race abstention · `&` candidate
  abstention · `?` spoiled · `%` spoiled+reissued. **No `^`** (removed). Approval
  ballots accept only `0`/`1` (+ blank/marker = not approved).
- **Levels (101/201/301)** live ONLY in `00_start_here/CURRICULUM.md`
  (authoritative). Don't tag every file. Example folders stay content-typed
  (`01_Single_winner/`, `02_Multi_winner/`, `split_voting/`).
- **Where text lives:** per-file context in the YAML (`scenario_description`
  printable, `video_script` = notes, never echoed); cross-file teaching in
  Markdown. No `.md` per YAML. See `ORGANIZATION.md`.
- **`_tabulated`** files are generated siblings in `*_tabulated/`; regenerate by
  re-running the YAMLs after engine changes. They always show full context.
- **Cross-reference slides by title** via `interviews_conversations/LINKS.md`
  short names — never page numbers or `#slide=id…` deep links.

## Engines
- `STARVote_LH_tabulation_engine/starvote_larry_hastings.py` — STAR + Bloc/
  proportional; reporting options; `blocs:` vote-splitting check; quorum;
  `[Divergence from STAR]` comparison. Auto-dispatches to RCV-IRV / Approval by
  `voting_method`, or to RCV-IRV when ballots contain ranked `>` (comments with
  `->` are ignored).
- `RCV_IRV_tabulation_engine/rcv_irv_tabulation.py` — vendored pyrankvote; reads
  ranked (`A>C>B`) or score ballots.
- Quick checks can use system `python3` (engines are vendored); the user runs via
  their `.venv` / `uv`.
- The engine errors *clearly* (no tracebacks) for the common mistakes: bad YAML,
  no `ballots:` block / old nested schema (prints the key-components template),
  wrong column counts, invalid chars / out-of-range scores, ranked ballots under a
  score method, and method/seats mismatches. Missing `voting_method` / `num_winners`
  is a non-fatal NOTE (defaults to STAR / 1). Generated `_tabulated.txt` files are
  refused as input.

## Tests
- `STARVote_LH_tabulation_engine/tests/test_single_winner_positive.py` — every
  single-winner STAR file with `expected_winners` (in `01_Single_winner/`,
  `split_voting/`, `YAML_library/1_positive/`) is run through the CLI (which also
  writes its `_tabulated` copy) and checked for exit 0 + correct winner.
- `…/tests/test_harness_selfcheck.py` — meta-tests proving the winner check isn't
  vacuous: deliberately-wrong answer keys (single- and multi-winner) in
  `tests/harness_cases/` must NOT match the engine's real result.
- `…/tests/test_json_to_yaml_conversion.py` — guards the BetterVoting-JSON →
  YAML pipeline (`YAML_library/1_positive/01_convert_json_yaml.py`): converts a
  real export in an isolated tmp dir and checks the produced YAML tabulates to the
  embedded winners (catches engine-signature drift like the `parse_ballots_from_string`
  arity bug).
- `…/tests/test_negative_validation.py` — malformed fixtures (in `tests/negative_cases/`
  **and** the migrated `YAML_library/2_negative/`) must exit 1 with the right
  message and no traceback; covers single messages and multiple-errors-in-one-file.
- Run: `pytest tests/test_single_winner_positive.py tests/test_negative_validation.py`
  from the engine dir. A repo pre-commit hook (`scripts/git-hooks/`, wired via
  `git config core.hooksPath scripts/git-hooks`) runs these on every commit.

## When unsure
Consistency matters more than cleverness here. If a terminology or convention
question isn't covered by the `00_start_here/` docs, ask rather than guess.
