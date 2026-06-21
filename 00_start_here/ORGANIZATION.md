# Organizing the YAML files (conventions)

Where things live, what goes in the YAML vs a Markdown file, and how to get a
clean demo without losing your documentation.

## The core principle: storage ≠ display

Most of the second-guessing ("if I document the scenario in the YAML it clutters
my recording") comes from treating *where the text lives* and *what shows on
screen* as the same decision. They aren't.

- **Keep the scenario text in the YAML** — one source of truth, travels with the
  ballots, can't drift out of sync.
- **Control what prints with an option** — `show_description: false` hides the
  long description on screen for a clean demo, *without removing it from the
  file*. The saved `_tabulated` file always keeps the full text.

So: store rich, display clean. You never have to choose.

## What goes where

| Content | Lives in | Prints on screen? |
|---------|----------|-------------------|
| `election_title` | YAML | yes (one-line banner) |
| `scenario_description` — short, audience-facing "what" | YAML | yes, unless `show_description: false` |
| `video_script` — presenter notes, cues, "how to present" | YAML | **no** (never echoed) |
| Cross-file teaching (lessons, sequences, comparisons, "why") | **Markdown** (`00_start_here/`, folder READMEs) | n/a |

Rule of thumb: **per-file context → in the YAML; cross-file teaching → Markdown.**
If a paragraph is about *this one election*, it belongs in the file. If it's
about how several examples fit together, it belongs in an `.md`.

## Don't: a separate `.md` per YAML, or a folder per scenario

Tempting, but it creates exactly the sync problem you already dislike with the
Google Docs:

- **Per-YAML `.md`** doubles maintenance and drifts out of sync. The YAML already
  has two slots — `scenario_description` (printable) and `video_script` (notes) —
  which cover everything a single file needs.
- **A folder per scenario** (`yaml` + `md` + `_tabulated` together) fragments
  navigation: you can no longer skim a folder of examples, and the lesson order
  gets buried. Heavy for no benefit.

## Recommended folder structure (keep what you have)

Group by **teaching role**, not by file type:

```
00_start_here/        lessons, glossary, curriculum, tips, conventions (Markdown)
01_Single_winner/     single-winner example YAMLs
01_Single_winner_tabulated/   generated _tabulated.txt (sibling, mirrors source)
02_Multi_winner/      multi-winner / proportional YAMLs
02_Multi_winner_tabulated/
split_voting/         spoiler / vote-splitting example set
interviews_conversations/   Larry↔Adam scripts + LINKS registry (Markdown)
STARVote_LH_tabulation_engine/   the engine + tools
RCV_IRV_tabulation_engine/       the RCV-IRV engine
```

- **`_tabulated` output stays in a sibling `*_tabulated/` folder** — generated,
  regenerable, separate from source, but easy to diff against the YAML it came
  from. (They're committed by choice; they could be gitignored instead.)
- **Markdown teaching docs cluster in `00_start_here/`** and in each folder's
  `README.md`, so the prose has a home that isn't tangled with the data.

## The clean-demo / recording recipe

For a file you'll show on camera:

```yaml
options:
  show_description: false   # hide the long write-up
  show_matrix: false
  show_condorcet: false
  show_score_counts: false
  brief: true
  show_irv: false
```

That leaves just the title banner, the ballots, and the tabulation. The full
context is still in the file (and in its `_tabulated` copy) for anyone studying
it later. Flip the flags back to `true` for a workshop or self-study.

> Tip: keep `scenario_description` to 1–3 short paragraphs (the audience-facing
> "what"), and put longer staging notes in `video_script` — it never prints, so
> it can be as detailed as you like without ever cluttering a demo.

See also: [TIPS_choosing_voter_counts.md](./TIPS_choosing_voter_counts.md) ·
[CURRICULUM.md](./CURRICULUM.md).
