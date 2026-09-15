"""WO-S01 reproducible A0/A1/A2 verification.

Run from the repository root with the isolated UGAS V2 interpreter:
    <venv>/Scripts/python.exe -B .engineering/evidence/s01-foundation/verify_s01.py

Exit codes: 0 = all gates green, 1 = a gate failed, 2 = wrong interpreter / unavailable pinned object.
Read-only with respect to the repository: -B keeps bytecode out, and pytest runs with -p no:cacheprovider.
"""
from __future__ import annotations

import ast
import hashlib
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]

# Immutable historical baseline. Pinned deliberately: deriving it from a branch ref such as
# origin/planning/m01-replan would let the historical comparison drift as the governed branch advances.
PINNED_BASE_SHA = "a1d71a545aad45e4ccef3a8b9404b360332031f5"
# S00 predecessor merge, and the kernel contract fingerprint that S01 carries forward unchanged.
S00_MERGE_SHA = "71f0f5b95f5b5fe6fb3a1281fcbe97416232828f"
S00_KERNEL_FINGERPRINT = "a66daa1b059bcb87158b69fbb8117e75c315c9ae0ddc233e1c90a1a7a38c3611"

SCOPED_PACKAGES = [
    "packages/py/ugas/foundation",
    "packages/py/ugas/modules/m01_product_production_os",
    "packages/py/ugas/modules/m02_hardware_intelligence",
    "packages/py/ugas/modules/m03_model_intelligence",
    "packages/py/ugas/modules/m04_multimodal_ir",
    "packages/py/ugas/modules/m05_asset_dna",
]
BANNED_IMPORT_ROOTS = {
    "torch", "tensorflow", "openai", "anthropic", "bpy", "comfyui", "requests",
    "httpx", "aiohttp", "boto3", "transformers", "diffusers",
}

failures: list[str] = []


def gate(label: str, ok: bool, detail: str) -> None:
    print(f"{'PASS' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        failures.append(f"{label}: {detail}")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True).stdout.strip()


def fingerprint(rels: list[str], rev: str | None = None) -> str:
    """sha256 over sorted 'path:sha256' lines, CRLF normalised to LF, LF-joined, no trailing newline.

    CRLF normalisation is required because this repository runs core.autocrlf=true with no .gitattributes, so
    the working tree is CRLF on Windows while committed blobs are LF. Normalising makes the value identical
    from either source and reproducible on any platform.
    """
    lines = []
    for rel in sorted(rels):
        if rev is None:
            raw = (REPO / rel).read_bytes()
        else:
            raw = subprocess.run(["git", "cat-file", "blob", f"{rev}:{rel}"], cwd=REPO, capture_output=True).stdout
        lines.append(f"{rel}:{hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()}")
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def scoped_files() -> list[str]:
    return sorted(
        p.relative_to(REPO).as_posix()
        for root in SCOPED_PACKAGES
        for p in (REPO / root).rglob("*.py")
    )


# ---- source identity ---------------------------------------------------------------------------------
print(f"PYTHON_VERSION={sys.version.split()[0]}")
print(f"PYTHON_EXECUTABLE={sys.executable}")
sys.path.insert(0, str(REPO / "packages" / "py"))
import ugas  # noqa: E402

resolved = sorted({str(pathlib.Path(p).resolve()) for p in (getattr(ugas, "__path__", []) or [])})
print(f"UGAS_RESOLVED_TO={resolved}")
if not resolved or not all(REPO in pathlib.Path(p).parents or pathlib.Path(p) == REPO for p in resolved):
    print("FATAL: 'ugas' does not resolve inside this checkout; refusing to produce evidence.")
    sys.exit(2)

# ---- pinned baseline ---------------------------------------------------------------------------------
if subprocess.run(["git", "cat-file", "-e", f"{PINNED_BASE_SHA}^{{commit}}"], cwd=REPO, capture_output=True).returncode != 0:
    print(f"FATAL: pinned base commit {PINNED_BASE_SHA} is unavailable in this repository.")
    sys.exit(2)
print(f"PINNED_BASE_SHA={PINNED_BASE_SHA}")
print(f"CODE_HEAD_UNDER_ATTESTATION={git('log', '-1', '--format=%H', '--', *SCOPED_PACKAGES)}")
print(f"PR_HEAD_AT_GENERATION={git('rev-parse', 'HEAD')}")

# ---- S00 carry-forward -------------------------------------------------------------------------------
kernel_files = [p for p in git("ls-tree", "-r", "--name-only", PINNED_BASE_SHA, "packages/py/ugas/kernel").split() if p.endswith(".py")]
carried = fingerprint(kernel_files, rev=PINNED_BASE_SHA)
print(f"S00_KERNEL_FINGERPRINT_CARRIED={carried}")
gate("S00_KERNEL_FINGERPRINT_MATCHES", carried == S00_KERNEL_FINGERPRINT,
     "kernel contract carried forward unchanged from the S00 attestation")
gate("KERNEL_UNMODIFIED_BY_S01", len(git("diff", "--name-only", PINNED_BASE_SHA, "--", "packages/py/ugas/kernel").split()) == 0,
     "kernel package has no diff against the approved base")

# ---- A0: syntax + architecture -----------------------------------------------------------------------
files = scoped_files()
syntax_fail = []
leaks = []
for path in files:
    source = (REPO / path).read_text(encoding="utf-8")
    try:
        tree = ast.parse(source, filename=path)
    except SyntaxError as exc:
        syntax_fail.append(f"{path}: {exc}")
        continue
    for node in ast.walk(tree):
        names: list[str] = []
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module:
            names = [node.module]
        for name in names:
            if name.split(".")[0] in BANNED_IMPORT_ROOTS:
                leaks.append(f"{path}: {name}")
gate("A0_SYNTAX", not syntax_fail, f"{len(files) - len(syntax_fail)}/{len(files)} files parse")
gate("A0_NO_PROVIDER_SDK_IMPORT", not leaks, f"{len(leaks)} provider SDK imports in S01 scope")
for item in (syntax_fail + leaks)[:10]:
    print(f"  - {item}")

# ---- A1 + A2: focused suites -------------------------------------------------------------------------
proc = subprocess.run(
    [sys.executable, "-B", "-m", "pytest", *SCOPED_PACKAGES, "--import-mode=importlib", "-q", "-p", "no:cacheprovider"],
    cwd=REPO, capture_output=True, text=True,
)
summary = [ln for ln in proc.stdout.strip().splitlines() if ln.strip()][-1:] or [""]
print(f"A1_A2_PYTEST_EXIT={proc.returncode}  {summary[-1]}")
if proc.returncode != 0:
    failures.append(f"A1/A2 pytest failed (exit {proc.returncode})")
    print(proc.stdout[-2000:])

# ---- mutation / negative controls --------------------------------------------------------------------
mut = subprocess.run(
    [sys.executable, "-B", ".engineering/evidence/s01-foundation/mutation_check.py"],
    cwd=REPO, capture_output=True, text=True,
)
score = [ln for ln in mut.stdout.strip().splitlines() if ln.startswith("MUTATION_SCORE")]
print(f"MUTATION_EXIT={mut.returncode}  {score[-1] if score else 'no score reported'}")
gate("SAFETY_STRENGTH_CONTROLS", mut.returncode == 0, score[-1] if score else "mutation harness failed")

# ---- fingerprints ------------------------------------------------------------------------------------
print(f"FOUNDATION_CONTRACT_FINGERPRINT={fingerprint(files)}  (files={len(files)})")

# ---- verdict -----------------------------------------------------------------------------------------
if failures:
    print(f"S01_VERIFY=FAIL failures={len(failures)}")
    for item in failures:
        print(f"  - {item}")
    sys.exit(1)
print("S01_VERIFY=PASS")
