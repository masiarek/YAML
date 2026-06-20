"""
md_to_presenter_html.py

Render a "Why STAR Voting"-style markdown deck into a styled presenter HTML page:
  * slide bullets are LARGER,
  * '> 🎬 Video script:' notes are SMALLER and muted,
  * the exact words to say (anything in "double quotes" inside a video-script
    note) are shown in a distinct teleprompter color,
  * '> Speaker note:' blocks get their own muted accent.

Markdown stays the source of truth; re-run this whenever it changes.

Usage:
    python md_to_presenter_html.py ../../00_start_here/Why_STAR_Voting.md
    python md_to_presenter_html.py input.md -o output.html
"""

import argparse
import html
import os
import re

CSS = """
:root { --ink:#1a2230; --muted:#5f6b7a; --say:#1565c0; --bullet:#0b3d2e; }
* { box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
       max-width: 860px; margin: 2.5rem auto; padding: 0 1.5rem; line-height: 1.5; color: var(--ink); }
h1 { font-size: 2rem; border-bottom: 2px solid #e3e8ef; padding-bottom: .3rem; }
h2 { font-size: 1.4rem; margin-top: 2rem; color:#33415c; }
h3.slide { font-size: 1.5rem; margin-top: 2.2rem; color:#1565c0;
           border-left: 5px solid #1565c0; padding-left: .6rem; }
ul.bullets { margin: .6rem 0 .9rem; }
ul.bullets li { font-size: 1.25rem; line-height: 1.45; margin: .45rem 0; color: var(--bullet); }
ul.bullets li strong { color:#062b1f; }
.note { font-size: 0.82rem; line-height: 1.5; border-radius: 6px; padding: .55rem .85rem;
        margin: .5rem 0 1rem; }
.videoscript { color: var(--muted); background:#f5f8fc; border-left: 4px solid #9fc0e8; }
.videoscript .label { font-weight: 800; letter-spacing:.02em; color:#1565c0; }
.speakernote { color:#7a5b16; background:#fdf8ec; border-left: 4px solid #e3c168; }
.speakernote .label { font-weight: 800; color:#9a7012; }
/* the exact words to say aloud */
.say { color: var(--say); font-weight: 600; }
.say::before { content:"\\201C"; }
.say::after  { content:"\\201D"; }
hr { border:none; border-top:1px solid #e3e8ef; margin:2rem 0; }
p { margin:.5rem 0; }
.tip { font-size:.8rem; color:#8a93a3; }
"""


def inline(text):
    """Escape, then apply **bold** -> <strong>."""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return text


def color_quotes(text):
    """Wrap "double-quoted" say-aloud phrases in a colored span (quotes added by CSS)."""
    return re.sub(r'"([^"]*)"', r'<span class="say">\1</span>', text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md_file")
    ap.add_argument("-o", "--out", default=None)
    args = ap.parse_args()
    out = args.out or os.path.splitext(args.md_file)[0] + ".html"

    with open(args.md_file, encoding="utf-8") as f:
        lines = f.readlines()

    body = []
    bullets = []          # pending bullet list
    quote_lines = []      # pending blockquote

    def flush_bullets():
        if bullets:
            body.append('<ul class="bullets">')
            body.extend(f"  <li>{inline(b)}</li>" for b in bullets)
            body.append("</ul>")
            bullets.clear()

    def flush_quote():
        if not quote_lines:
            return
        raw = " ".join(quote_lines).strip()
        quote_lines.clear()
        if "🎬" in raw:
            label = "🎬 Video script:"
            rest = raw.split("Video script:", 1)[-1].strip()
            inner = color_quotes(inline(rest))
            body.append(f'<div class="note videoscript">'
                        f'<span class="label">{label}</span> {inner}</div>')
        elif raw.lower().startswith("speaker note"):
            rest = raw.split(":", 1)[-1].strip()
            body.append(f'<div class="note speakernote">'
                        f'<span class="label">Speaker note:</span> {inline(rest)}</div>')
        else:
            body.append(f'<div class="note">{inline(raw)}</div>')

    for ln in lines:
        line = ln.rstrip("\n")
        if line.startswith(">"):
            flush_bullets()
            quote_lines.append(line.lstrip("> ").rstrip())
            continue
        flush_quote()
        if line.startswith("- "):
            bullets.append(line[2:].strip())
            continue
        flush_bullets()
        if line.startswith("### "):
            body.append(f'<h3 class="slide">{inline(line[4:].strip())}</h3>')
        elif line.startswith("## "):
            body.append(f"<h2>{inline(line[3:].strip())}</h2>")
        elif line.startswith("# "):
            body.append(f"<h1>{inline(line[2:].strip())}</h1>")
        elif line.strip() == "---":
            body.append("<hr>")
        elif line.strip() == "":
            pass
        else:
            body.append(f"<p>{color_quotes(inline(line.strip()))}</p>")
    flush_bullets()
    flush_quote()

    doc = (f"<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
           f"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
           f"<title>Why STAR Voting — presenter script</title>\n<style>{CSS}</style>\n"
           f"</head>\n<body>\n"
           f'<p class="tip">Presenter view — bullets are the slide; '
           f'<span class="say">colored text</span> is the exact words to say.</p>\n'
           + "\n".join(body) + "\n</body>\n</html>\n")
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
