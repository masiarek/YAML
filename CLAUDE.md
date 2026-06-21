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
  (matrix legend *and* runoff). Note "(aka Equal Preference, No Preference)". Do
  **not** reintroduce "Equal Preference" as the lead term.
- **Favorite Betrayal Criterion ≠ Later-No-Harm** — keep distinct. Neither STAR
  nor IRV is FBC-compliant; RCV-IRV fails it structurally (center squeeze), STAR
  only in rare constructions. See `interviews_conversations/favorite_betrayal_voting_301.md`.
- Spelling: **Bucklin** (not "Buckling"). **Hare ≈ IRV** single-winner, **STV**
  multi-winner. Borda & Bucklin are ranked but **not** Condorcet.

---

## Repo conventions (so output stays consistent)
- **YAML `options:` booleans → `true` / `false`** (parser also accepts t/f/y/n/etc.,
  but house style is the long form).
- **`show_description`**: `false` = clean demo (description stays in the file and
  the `_tabulated` copy, hidden on screen); `true` = study/reference. Files with a
  `video_script` default to `false`; description-only files default to `true`.
- **Voter counts:** weighted `Count` values must be **≥ 6** (avoid collision with
  0–5 scores), or use individual ballots. Scaling all weights ×N preserves
  STAR/proportional winners and percentages. See `TIPS_choosing_voter_counts.md`.
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

## When unsure
Consistency matters more than cleverness here. If a terminology or convention
question isn't covered by the `00_start_here/` docs, ask rather than guess.
