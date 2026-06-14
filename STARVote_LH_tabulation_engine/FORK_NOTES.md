# Fork Notes — starvote (vendored fork)

This directory contains a **vendored fork** of Larry Hastings' STAR Voting
engine, [`larryhastings/starvote`](https://github.com/larryhastings/starvote).
We do not submit pull requests upstream; we edit the engine directly here and
keep it as part of this project (the `masiarek/YAML` repo).

## What is what

| Path | Origin | Edit it when… |
|------|--------|---------------|
| `starvote/` (`__init__.py`, `__main__.py`, `reference.py`) | **Upstream engine** (Larry Hastings) | You're changing how the *voting algorithm itself* works — scoring, tabulation, tiebreak mechanics, CLI/option parsing of the engine. |
| `starvote_larry_hastings.py` | **Our code** | Anything about how *we* run, feed, or present an election — our `LotNumberTiebreaker`, matrix visualization, colored output, file loading. This `import starvote`; it should never duplicate engine logic. |
| `tools_adam/` | **Our code** | Helper/automation scripts (conversion, simulation, BetterVoting automation, etc.). |
| `tests/`, `test_elections/` | Mixed | Upstream tests plus ours. |

**Rule of thumb:** "Would Larry want this in the engine for everyone?" → it goes
in `starvote/`. "Is this about *my* analysis, display, or workflow?" → it goes
in our script/tools.

## Upstream baseline

The pristine upstream version is **starvote 2.1.6**, verified byte-identical to
the PyPI release. It is recorded as the git tag:

```
starvote-upstream-2.1.6   ->  commit daa6bbd
```

### See exactly what we've changed in the engine, any time

```bash
# full diff of our engine edits vs pristine upstream
git diff starvote-upstream-2.1.6 -- STARVote_LH_tabulation_engine/starvote/

# just a summary
git diff --stat starvote-upstream-2.1.6 -- STARVote_LH_tabulation_engine/starvote/
```

## Current divergence from upstream 2.1.6

As of this note, the only engine change is in `starvote/__init__.py`
(roughly +64 / −2 lines), adding two optional output toggles and one label fix:

- **`print_averages`** option (default `False`) + CLI flag `-a` / `--print-averages`
  and config key `print averages = <bool>`. Suppresses the averages line unless asked.
- **`print_maximum_score`** option (default `False`) + CLI flag `-M` / `--print-maximum-score`
  and config key `print maximum score = <bool>`. Suppresses the "Maximum score is …" line unless asked.
- Relabeled the score bucket **`No Preference` → `Equal Preference`**.
- Both options are forwarded to method functions only when they differ from the
  default, so older/reference method implementations don't break.

These changes make all 105 tests pass.

## How to pull a future upstream update (if ever wanted)

1. Download the new pristine version (e.g. `pip download starvote==X.Y.Z --no-deps --no-binary :all:`).
2. Tag it: copy the new `starvote/` over a clean checkout, commit, `git tag starvote-upstream-X.Y.Z`.
3. Re-apply our diff: `git diff starvote-upstream-2.1.6 starvote-upstream-X.Y.Z` shows what
   upstream changed; resolve against our edits listed above.

Because our edits are small and localized, re-applying them by hand is the
simplest path.
