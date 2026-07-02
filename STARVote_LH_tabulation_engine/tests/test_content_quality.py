"""
test_content_quality.py
=======================
Blocking gates for the two content-quality scans in
scripts/check_repo_hygiene.py (the pre-commit run of that script is
warn-only; these tests make the standards enforceable):

1. DESCRIPTIONS — every teaching YAML must carry a real
   scenario_description (no placeholders, no one-liners). It is the
   educational prose on that file's generated page; a bare data file is
   not a lesson.

2. TERMINOLOGY — the house canon (CLAUDE.md) is machine-checked:
   'Bucklin' spelling, 'Equal Support' as the lead term, and no bare
   'RCV' credited with IRV-specific pathologies. Deliberate exceptions
   carry an inline 'terminology-ok' marker; canon/discussion files are
   skipped inside the checker itself.
"""
import importlib.util
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
HYGIENE = REPO_ROOT / "scripts" / "check_repo_hygiene.py"


def _load():
    spec = importlib.util.spec_from_file_location("check_repo_hygiene", HYGIENE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_repo_hygiene"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_every_teaching_yaml_has_a_real_description():
    weak = _load().check_descriptions()
    assert not weak, (
        f"{len(weak)} teaching YAML(s) with weak/missing descriptions:\n" +
        "\n".join(f"  {f}: {msg}" for f, msg in weak) +
        "\n(scenario_description is the lesson on the generated page — "
        "say what the case shows and what to look for.)"
    )


def test_house_terminology_canon():
    hits = _load().check_terminology()
    assert not hits, (
        f"{len(hits)} terminology violation(s):\n" +
        "\n".join(f"  {f}:{ln}  {msg}" for f, ln, msg in hits) +
        "\n(Fix the wording, or mark a deliberate usage with 'terminology-ok'.)"
    )


def test_gates_are_not_vacuous():
    mod = _load()
    assert len(list(mod._yaml_teaching_files())) >= 50, "description gate scans too few files"
    assert mod.TERM_RULES, "terminology rules list is empty"
