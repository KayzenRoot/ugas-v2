"""WO-S00 Kernel Sync — reproducible A0/A1/A2 verification.

Run from the repository root with the isolated UGAS V2 interpreter:
    C:/Users/csn19/.ugas/venvs/ugas-v2-py314/Scripts/python.exe -B \
        .engineering/evidence/s00-kernel-sync/verify_kernel_sync.py

Exit codes: 0 = all gates green, 1 = a gate failed, 2 = wrong interpreter / ugas resolves outside this checkout.

Read-only with respect to the repository: -B keeps bytecode out of the worktree, and pytest is invoked with
-p no:cacheprovider so no .pytest_cache appears.
"""
from __future__ import annotations

import ast
import hashlib
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
KERNEL = REPO / "packages" / "py" / "ugas" / "kernel"

# Immutable historical baseline for WO-S00. Pinned deliberately: deriving this from a branch ref such as
# origin/planning/m01-replan would let the "before" fingerprint drift whenever the canonical branch advances,
# which would silently invalidate every historical before/after comparison recorded in the evidence bundle.
PINNED_BASE_SHA = "f0d3eadbd822b4a59966a38a4f2df3ad92c3d3d1"
EXPECTED_BEFORE_FINGERPRINT = "99899c814e933c3cc29343fda5dc54ef3c06efa9ed05083b3c506a2b7a07c4a9"

failures: list[str] = []


def gate(label: str, ok: bool, detail: str) -> None:
    print(f"{'PASS' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        failures.append(f"{label}: {detail}")


# ---- interpreter / source identity (review precondition) -----------------
print(f"PYTHON_VERSION={sys.version.split()[0]}")
print(f"PYTHON_EXECUTABLE={sys.executable}")
sys.path.insert(0, str(REPO / "packages" / "py"))
import ugas  # noqa: E402

resolved = sorted({str(pathlib.Path(p).resolve()) for p in (getattr(ugas, "__path__", []) or [])})
print(f"UGAS_RESOLVED_TO={resolved}")
if not resolved or not all(REPO in pathlib.Path(p).parents or pathlib.Path(p) == REPO for p in resolved):
    print("FATAL: 'ugas' does not resolve inside this checkout; refusing to produce evidence.")
    sys.exit(2)

# ---- A0: syntax ----------------------------------------------------------
py_files = sorted(KERNEL.rglob("*.py"))
syntax_ok = 0
for path in py_files:
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        syntax_ok += 1
    except SyntaxError as exc:
        failures.append(f"SYNTAX {path.relative_to(REPO).as_posix()}: {exc}")
gate("A0_KERNEL_SYNTAX", syntax_ok == len(py_files), f"{syntax_ok}/{len(py_files)} files parse")

# ---- A1 + A2: focused kernel suites -------------------------------------
tests_dir = KERNEL / "tests"
proc = subprocess.run(
    [sys.executable, "-B", "-m", "pytest", str(tests_dir), "-q", "-p", "no:cacheprovider"],
    cwd=REPO,
    capture_output=True,
    text=True,
)
tail = [ln for ln in proc.stdout.strip().splitlines() if ln.strip()][-1:] or [""]
print(f"A1_A2_PYTEST_EXIT={proc.returncode}  {tail[-1]}")
if proc.returncode != 0:
    failures.append(f"A1/A2 pytest failed (exit {proc.returncode})")
    print(proc.stdout[-2000:])

# ---- kernel contract fingerprint (blob-based, platform-stable) -----------
def fingerprint(rels: list[str], rev: str | None = None) -> str:
    """sha256 over sorted 'path:sha256' lines joined by LF, no trailing newline.

    Content is read from the given revision's blobs, or from the working tree when rev is None, and CRLF is
    normalised to LF before hashing. This repository runs core.autocrlf=true with no .gitattributes, so the
    working tree is CRLF on Windows while committed blobs are LF; normalising makes the value identical either
    way and reproducible from any clone on any platform.
    """
    lines = []
    for rel in sorted(rels):
        if rev is None:
            raw = (REPO / rel).read_bytes()
        else:
            raw = subprocess.run(["git", "cat-file", "blob", f"{rev}:{rel}"], cwd=REPO, capture_output=True).stdout
        lines.append(f"{rel}:{hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()}")
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def kernel_paths(rev: str | None) -> list[str]:
    if rev is None:
        return [p.relative_to(REPO).as_posix() for p in sorted(KERNEL.rglob("*.py"))]
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", rev, "packages/py/ugas/kernel"],
        cwd=REPO, capture_output=True, text=True,
    ).stdout.split()
    return [p for p in out if p.endswith(".py")]


current = kernel_paths(None)
after = fingerprint(current)
print(f"KERNEL_FINGERPRINT_AFTER={after}  (files={len(current)})")

# Historical baseline comes from the pinned SHA only. Fail loudly if that object is not present locally,
# rather than silently substituting a branch ref or skipping the comparison.
probe = subprocess.run(["git", "cat-file", "-e", f"{PINNED_BASE_SHA}^{{commit}}"], cwd=REPO, capture_output=True)
if probe.returncode != 0:
    print(f"FATAL: pinned base commit {PINNED_BASE_SHA} is unavailable in this repository.")
    print("       Fetch it explicitly, or restore the pinned object, before trusting any historical comparison.")
    sys.exit(2)
print(f"PINNED_BASE_SHA={PINNED_BASE_SHA}")
base_paths = kernel_paths(PINNED_BASE_SHA)
before = fingerprint(base_paths, rev=PINNED_BASE_SHA)
print(f"KERNEL_FINGERPRINT_BEFORE={before}  (files={len(base_paths)})")
gate("PINNED_BASE_RESOLVES", True, f"{PINNED_BASE_SHA} is a commit in this repository")
gate("BEFORE_FINGERPRINT_MATCHES_PINNED", before == EXPECTED_BEFORE_FINGERPRINT,
     f"expected {EXPECTED_BEFORE_FINGERPRINT}")

# ---- verdict -------------------------------------------------------------
if failures:
    print(f"KERNEL_SYNC=FAIL failures={len(failures)}")
    for item in failures:
        print(f"  - {item}")
    sys.exit(1)
print("KERNEL_SYNC=PASS")
