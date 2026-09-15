"""Issue #53 reproducibility script — kernel integrity check for the S00 entry gate.

Verifies that:
  1. `ugas` resolves to THIS repository (V2), not a shadowing UGAS V1 install;
  2. the kernel modules required by the S00 Context Pack import cleanly;
  3. the kernel A1 test module imports and exposes its test surface;
  4. observability and the kernel test consume the canonical ErrorKind object from
     packages/py/ugas/kernel/primitives.py (identity, not a copy or a redefinition).

Run from the repository root:
    py -3.14 -B .engineering/evidence/issue-53/kernel_integrity_check.py
"""
from __future__ import annotations

import importlib
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "packages" / "py"))

KERNEL_MODULES = [
    "primitives",
    "envelopes",
    "evidence_graph",
    "adapter_qualification",
    "observability",
]

ok = True

import ugas  # noqa: E402

resolved = list(getattr(ugas, "__path__", []) or [])
print(f"UGAS_RESOLVED_TO={resolved}")
if not any("ugas-v2" in p for p in resolved):
    print("FATAL: 'ugas' does not resolve to the UGAS V2 checkout; see ENV-01 in the evidence bundle.")
    sys.exit(2)

for name in KERNEL_MODULES:
    importlib.import_module(f"ugas.kernel.{name}")
print(f"KERNEL_MODULES_IMPORTED={len(KERNEL_MODULES)}/{len(KERNEL_MODULES)}")

test_module = importlib.import_module("ugas.kernel.tests.test_kernel_readiness")
functions = sorted(n for n in dir(test_module) if n.startswith("test_"))
print(f"KERNEL_TEST_FUNCTIONS={functions}")

primitives = importlib.import_module("ugas.kernel.primitives")
observability = importlib.import_module("ugas.kernel.observability")

canonical = primitives.ErrorKind
test_error_kind = getattr(test_module, "ErrorKind", None)
observability_is_canonical = observability.ErrorKind is canonical
test_is_canonical = test_error_kind is canonical

print(f"ERRORKIND_CANONICAL={canonical.__module__}.{canonical.__name__}")
print(f"OBSERVABILITY_ERRORKIND_IS_CANONICAL={observability_is_canonical}")
print(f"TEST_ERRORKIND_IS_CANONICAL={test_is_canonical}")
print(f"ERRORKIND_MEMBER_COUNT={len(list(canonical))}")
print(f"ERRORKIND_MEMBERS={[k.name for k in canonical]}")

if not (observability_is_canonical and test_is_canonical):
    ok = False
    print("FAIL: kernel does not consume the canonical ErrorKind taxonomy")
if len(list(canonical)) != 8:
    ok = False
    print("FAIL: unexpected ErrorKind member count")

print("KERNEL_INTEGRITY=PASS" if ok else "KERNEL_INTEGRITY=FAIL")
sys.exit(0 if ok else 1)
