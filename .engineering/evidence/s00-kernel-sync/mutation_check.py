"""WO-S00 — mutation harness proving the kernel tests are falsifiable.

A green suite is weak evidence on its own: tests that assert nothing, or assert the wrong thing, also pass.
This harness replaces each safety-critical kernel function with a deliberately wrong implementation, then
re-imports the test module and runs the test that is supposed to catch it. A mutant that is NOT caught means
the corresponding test is vacuous.

Run from the repository root:
    C:/Users/csn19/.ugas/venvs/ugas-v2-py314/Scripts/python.exe -B \
        .engineering/evidence/s00-kernel-sync/mutation_check.py

Exit code 0 means every mutation was caught.
"""
from __future__ import annotations

import hashlib
import importlib
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "packages" / "py"))

import ugas.kernel.adapter_qualification as aq  # noqa: E402
import ugas.kernel.evidence_graph as eg  # noqa: E402
import ugas.kernel.legacy_evidence_bridge as lb  # noqa: E402
import ugas.kernel.observability as ob  # noqa: E402
from ugas.kernel.evidence_graph import EvidenceGraph, EvidenceNode, ProofState  # noqa: E402


def _reload_tests():
    for name in ("ugas.kernel.tests.test_kernel_readiness", "ugas.kernel.tests.test_legacy_evidence_bridge"):
        sys.modules.pop(name, None)
    return (
        importlib.import_module("ugas.kernel.tests.test_kernel_readiness"),
        importlib.import_module("ugas.kernel.tests.test_legacy_evidence_bridge"),
    )


def _expect_failure(module, test_name: str) -> bool:
    try:
        getattr(module, test_name)()
    except AssertionError:
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"    (raised {type(exc).__name__}: {exc})")
        return True
    return False


original_carry_forward = eg.carry_forward
original_assert_usable = aq.assert_usable


def m_carry_forward_open(graph, current_fingerprints):
    """Mutant: carry-forward stops being fail-closed and promotes every proven node."""
    return EvidenceGraph(graph.project_id, tuple(
        EvidenceNode(n.id, n.project_id, n.subject_fingerprint, n.dimension, ProofState.CARRY_FORWARD,
                     n.producer_ref, n.dependency_refs, n.evidence_ref, n.dependency_fingerprints)
        if n.state in {ProofState.PROVEN, ProofState.CARRY_FORWARD} else n for n in graph.nodes))


def m_no_cycles(graph):
    """Mutant: cycle detection always reports a clean DAG."""
    return ()


def m_order_dependent_fingerprint(graph):
    """Mutant: fingerprint depends on the order nodes were supplied in."""
    payload = [{"id": n.id, "subject": n.subject_fingerprint, "state": str(n.state),
                "deps": list(n.dependency_refs)} for n in graph.nodes]
    return hashlib.sha256(json.dumps({"p": graph.project_id, "n": payload}).encode()).hexdigest()


def m_everything_retryable(kind):
    """Mutant: retry classification permits even hard rejections."""
    return True


def m_ignore_version(q, required_capabilities, *, requested_version=None):
    """Mutant: the version binding is silently ignored."""
    return original_assert_usable(q, required_capabilities)


def m_coerce_unknown_state(state):
    """Mutant: an unknown legacy state is coerced into canonical proof instead of raising."""
    return ProofState.PROVEN


MUTATIONS = [
    ("M1 carry_forward not fail-closed", eg, "carry_forward", m_carry_forward_open,
     "test_kernel_readiness", "test_carry_forward_fails_closed_when_own_fingerprint_is_unverifiable"),
    ("M2 cycles never detected", eg, "detect_cycles", m_no_cycles,
     "test_kernel_readiness", "test_cycle_is_detected_and_rejected"),
    ("M2b self-cycle never detected", eg, "detect_cycles", m_no_cycles,
     "test_kernel_readiness", "test_self_dependency_is_a_cycle"),
    ("M3 fingerprint order-dependent", eg, "graph_fingerprint", m_order_dependent_fingerprint,
     "test_kernel_readiness", "test_graph_fingerprint_is_order_independent_and_content_sensitive"),
    ("M4 hard rejections marked retryable", ob, "is_retryable", m_everything_retryable,
     "test_kernel_readiness", "test_retry_classification_never_retries_hard_rejections"),
    ("M5 adapter version mismatch ignored", aq, "assert_usable", m_ignore_version,
     "test_kernel_readiness", "test_adapter_version_mismatch_fails_closed"),
    ("M6 unknown legacy state coerced to PROVEN", lb, "canonical_proof_state", m_coerce_unknown_state,
     "test_legacy_evidence_bridge", "test_unknown_legacy_state_fails_closed"),
]

print("KERNEL TEST MUTATION HARNESS")
print("=" * 72)
results: list[tuple[str, bool]] = []
for label, module, attr, mutant, test_module_name, test_name in MUTATIONS:
    backup = getattr(module, attr)
    setattr(module, attr, mutant)
    readiness, bridge = _reload_tests()
    target = readiness if test_module_name == "test_kernel_readiness" else bridge
    caught = _expect_failure(target, test_name)
    setattr(module, attr, backup)
    results.append((label, caught))
    print(f"{'CAUGHT ' if caught else 'MISSED '} {label}  -> {test_name}")

_reload_tests()
print("=" * 72)
missed = [r for r in results if not r[1]]
print(f"MUTATIONS={len(results)} CAUGHT={len(results) - len(missed)} MISSED={len(missed)}")
print(f"MUTATION_SCORE={len(results) - len(missed)}/{len(results)}")
sys.exit(1 if missed else 0)
