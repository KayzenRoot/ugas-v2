"""Issue #53 reproducibility script — A0/A1 preflight for the materialized M01-M36 surfaces.

Run from the repository root with the interpreter that resolves UGAS V2 correctly:
    py -3.14 -B .engineering/evidence/issue-53/preflight_materialized_surfaces.py

Read-only: parses/compiles sources and imports modules. Writes no repository files.
Note: use -B or PYTHONDONTWRITEBYTECODE=1 so no __pycache__ appears in the worktree.
"""
from __future__ import annotations

import ast
import asyncio
import hashlib
import importlib
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
SURFACE_ROOT = REPO / "packages" / "py" / "ugas" / "modules"

KERNEL_IMPORTS = [
    "ugas.kernel.primitives",
    "ugas.kernel.envelopes",
    "ugas.kernel.evidence_graph",
    "ugas.kernel.adapter_qualification",
    "ugas.kernel.observability",
]

MODULE_SURFACES = [
    "contracts", "ports", "errors", "domain", "service",
    "contracts_deep", "ports_deep", "errors_deep", "services_deep",
]

CANONICAL_GLOBS = [
    "packages/py/ugas/kernel/*",
    "packages/py/ugas/model_factory/*",
    "packages/py/ugas/extensions/*",
    "packages/py/ugas/distributed_fabric/*",
    "packages/py/ugas/runtime_experience/*",
]

failures: list[str] = []

# Revision whose committed blobs the fingerprints describe. HEAD is stable for these paths: the
# materialized surfaces and the canonical kernel/M37-M40 files are identical in every commit of the
# Issue #53 publication branch.
fingerprint_rev = "HEAD"


def fingerprint(rels: list[str], rev: str = "HEAD") -> str:
    """Pinned recipe: sha256 over sorted 'path:sha256' lines joined by LF, no trailing newline.

    Per-file digests are taken over the COMMITTED BLOB content (git cat-file), not the working-tree
    bytes, so the fingerprint is platform-stable: this repository runs with core.autocrlf=true and no
    .gitattributes, so working-tree files are CRLF on Windows while the blobs are LF. Hashing the blob
    makes the value reproducible from any clone on any platform. Do not add a trailing newline here.
    """
    lines = []
    for rel in sorted(rels):
        blob = subprocess.run(
            ["git", "cat-file", "blob", f"{rev}:{rel}"],
            cwd=REPO,
            capture_output=True,
            check=True,
        ).stdout
        lines.append(f"{rel}:{hashlib.sha256(blob).hexdigest()}")
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def tracked(pattern: str) -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", pattern], cwd=REPO, capture_output=True, text=True, check=True
    ).stdout.split()
    return [p for p in out if p]


# ---- A0: syntax parse of every materialized file ------------------------
new_files = sorted(SURFACE_ROOT.rglob("*.py"))
syntax_ok = 0
for path in new_files:
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        syntax_ok += 1
    except SyntaxError as exc:
        failures.append(f"SYNTAX {path.relative_to(REPO).as_posix()}: {exc}")
print(f"A0_SYNTAX_FILES={len(new_files)} OK={syntax_ok} FAIL={len(new_files) - syntax_ok}")

# ---- A1: kernel imports required by S00 ---------------------------------
sys.path.insert(0, str(REPO / "packages" / "py"))
kernel_ok = 0
for name in KERNEL_IMPORTS:
    try:
        importlib.import_module(name)
        kernel_ok += 1
    except Exception as exc:  # noqa: BLE001
        failures.append(f"IMPORT {name}: {type(exc).__name__}: {exc}")
print(f"A1_KERNEL_IMPORTS={kernel_ok}/{len(KERNEL_IMPORTS)}")

primitives = importlib.import_module("ugas.kernel.primitives")
print(f"ERRORKIND={primitives.ErrorKind.__name__} MEMBERS={len(list(primitives.ErrorKind))}")

# ---- A1: materialized module surfaces -----------------------------------
module_ok = module_fail = 0
for pkg_dir in sorted(p for p in SURFACE_ROOT.iterdir() if p.is_dir()):
    for surface in MODULE_SURFACES:
        target = f"ugas.modules.{pkg_dir.name}.{surface}"
        try:
            importlib.import_module(target)
            module_ok += 1
        except Exception as exc:  # noqa: BLE001
            module_fail += 1
            failures.append(f"IMPORT {target}: {type(exc).__name__}: {exc}")
print(f"A1_MODULE_SURFACE_IMPORTS OK={module_ok} FAIL={module_fail}")

# ---- A1: M01 orchestration smoke through a fake port --------------------
try:
    from ugas.modules.m01_product_production_os.contracts import Command, Result
    from ugas.modules.m01_product_production_os.service import Service

    class FakeCapability:
        async def execute(self, command):
            return Result(status="ok", evidence_refs=("ev-1",))

    result = asyncio.run(Service(FakeCapability()).execute(Command(operation="plan")))
    assert result.status == "ok", result
    print(f"M01_FAKE_PORT_SMOKE=PASS status={result.status} evidence={result.evidence_refs}")
except Exception as exc:  # noqa: BLE001
    failures.append(f"SMOKE m01 service: {type(exc).__name__}: {exc}")
    print("M01_FAKE_PORT_SMOKE=FAIL")

# ---- fingerprints -------------------------------------------------------
canonical_rels = sorted({p for g in CANONICAL_GLOBS for p in tracked(g)})
materialized_rels = sorted(p.relative_to(REPO).as_posix() for p in new_files)
print(f"FINGERPRINT_REV={fingerprint_rev} (blob content)")
print(f"PROJECT_FINGERPRINT={fingerprint(canonical_rels)}  (canonical files={len(canonical_rels)})")
print(f"MATERIALIZED_SURFACE_FINGERPRINT={fingerprint(materialized_rels)}  (files={len(materialized_rels)})")

# ---- verdict ------------------------------------------------------------
print(f"PYTHON_VERSION={sys.version.split()[0]}")
if failures:
    print(f"PREFLIGHT=FAIL failures={len(failures)}")
    for item in failures[:40]:
        print(f"  - {item}")
    sys.exit(1)
print("PREFLIGHT=PASS")
