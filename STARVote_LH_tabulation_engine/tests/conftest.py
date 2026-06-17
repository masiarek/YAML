"""
pytest configuration for the engine's test suite.

Larry Hastings' upstream `test_all.py` calls `preload_local_starvote()` at
import time, which walks up the directory tree starting from `sys.argv[0]`
looking for `starvote/__init__.py`. When run as a script that's the test file,
so it works. Under pytest, `sys.argv[0]` is the pytest launcher, so the search
never finds the package and the `while True` loop spins forever (collection
hangs).

We don't want to edit the upstream test, so we fix the input instead: point
`sys.argv[0]` at a path inside the engine directory (which contains
`starvote/__init__.py`) before any test module is imported. conftest.py is
loaded before collection, so this runs first.
"""

import os
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent

# Larry's test_all.py uses paths relative to the engine directory (e.g.
# "test_elections/foo.starvote"), assuming it is run from there. pytest may be
# invoked from anywhere, so anchor the working directory to the engine dir.
os.chdir(ENGINE_DIR)

# Parent of this anchor is ENGINE_DIR, which holds starvote/__init__.py, so the
# upstream preload search terminates immediately. The file need not exist.
sys.argv[0] = str(ENGINE_DIR / "_pytest_engine_anchor.py")

# Make the engine importable regardless of where pytest is invoked from.
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))
