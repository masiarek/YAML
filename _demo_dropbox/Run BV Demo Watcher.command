#!/bin/bash
# Double-click this to start the BV demo watcher.
# It uses the repo's .venv if present, otherwise system python3.
DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$DIR/.." && pwd)"
PY="$REPO/.venv/bin/python"
[ -x "$PY" ] || PY="python3"
echo "Using: $PY"
exec "$PY" "$DIR/watch_bv.py"
