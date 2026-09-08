---
name: site-build
description: How this repo builds and deploys as a MkDocs site — the plugin versus hook decision, the docs dependency group, NAV_ORDER and sidebar reading order, local preview, and the two kinds of site-only redirect. Load before editing mkdocs.yml, mkdocs_hooks.py, the docs workflow, or any redirect map entry.
---

# The website build

*Migrated out of `CLAUDE.md` on 2026-09-08 so it loads on demand instead of in every session. The rules below are unchanged.*

**The repo publishes as a searchable website** — <https://masiarek.github.io/star-voting-library/>,
built by root `mkdocs.yml` (MkDocs Material + `mkdocs-same-dir` + `mkdocs-redirects`)
straight from the
repo's own Markdown (no `docs/` copy; `.yaml` / `_tabulated` files carried through)
and deployed by `.github/workflows/docs.yml` on every push to master. Folder
`README.md`s become the site's section index pages (one more reason that naming rule
matters), and links keep GitHub's file-relative semantics (`use_directory_urls:
false` — don't flip it). Local preview: `uv run --group docs mkdocs serve` (the
docs toolchain is pinned in `pyproject.toml`'s `docs` dependency group + `uv.lock`;
`mkdocs-same-dir`/`mkdocs-redirects` are capped at the last releases free of the
MkDocs-impersonating `properdocs` package — investigate before raising those pins).
`site/` is generated output — never commit.
Details + known nits: `07_Concepts/about_this_repo/website_build.md`.
**Site-only redirects (`redirects.redirect_maps` in `mkdocs.yml`) — two kinds, only
one of them discretionary.** A redirect replaces the *built* page at a URL; if the
source `.md` is still on disk, GitHub keeps rendering it but **the site never shows
it**. The **relocation** kind is mandatory and permanent — the file really moved (the
`00_start_here/*` concept pages into their method folders is the big set) and the old
URL has to keep resolving forever, for the reason the reorganization bullet above
gives: a deleted redirect is an unfixable 404. As of 2026-08-09 every live entry in
the map is this kind. The **hide-a-live-page** kind — redirecting a page that still
exists, to push site visitors somewhere better — is the one to use sparingly, because
the reason for it can disappear out from under it. **Retired case, worth reading:**
`05_Ranked_Robin/README.md` → the Ranked Robin concept page, added back when the
concept pages sat in a separate `00_start_here` tree and the case folder was the only
top-level door for a visitor wanting "Ranked Robin"; the "one door per method"
reorganization moved the concepts *into* `05_Ranked_Robin`, so the folder's own README
became the method front door in the right place and the redirect only pushed readers
past it (retired 2026-08-04 — the story is kept as a comment where it used to sit in
`mkdocs.yml`). So: **re-check these after any reorganization**, and whenever you add
one, **move or mirror whatever the source said onto the destination** and leave a
maintainer note in the redirected README — otherwise edits there silently never ship.
Adding a plugin means updating **two** places: `mkdocs.yml` plugins and the `docs`
dependency group in `pyproject.toml` (then `uv lock`). CI and the local preview both
resolve from `uv.lock`, so there is no separate install command to keep in sync.
**Prefer a hook over a plugin** for small build-time fixes: `hooks:` in `mkdocs.yml`
loads a plain repo file (`mkdocs_hooks.py`) with no dependency and no lock churn.
It already carries the sidebar acronym casing (`rr_tiebreaks` → "RR tiebreaks"),
which is fixed at build time precisely *because* renaming the folder would move
permanent URLs.
**Sidebar reading order lives there too** — `NAV_ORDER` in `mkdocs_hooks.py`,
keyed by folder path, listing children by on-disk name. Auto-nav is
alphabetical, which for a *lesson* folder is actively wrong (`01_Learn` opened
on the ballot page, with "Welcome to STAR Voting" third). Set the order there,
**never by renaming files to `01_`, `02_`…**: that is a number in a permanent
URL, and inserting one lesson later moves a whole run of them. Unlisted pages
keep their alphabetical slot at the bottom, so adding a page needs no edit;
a folder's `README.md` is always pinned first (`navigation.indexes` needs the
index at `children[0]`). Entries before `SPINE_BREAK` get a visible `N. ` in
the sidebar — keep that run short and mostly *sections*, since numbering a
page also prefixes that page's `<title>`. `tests/test_nav_labels.py` fails if
a listed name no longer exists on disk.
