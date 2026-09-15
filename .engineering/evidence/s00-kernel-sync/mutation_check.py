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

import dataclasses
import hashlib
import importlib
import json
import pathlib
import sys
from collections.abc import Mapping

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


def m_stale_state_retryable(kind):
    """Mutant (CR-001 RETRY-01): reverts to a deny-list so STALE_STATE becomes a retry candidate."""
    return kind not in {
        ob.ErrorKind.POLICY_REJECTION, ob.ErrorKind.QUALITY_REJECTION,
        ob.ErrorKind.CAPABILITY_DENIED, ob.ErrorKind.INTEGRITY_FAILURE,
    }


def m_top_level_only_secret_walk(node, path, found):
    """Mutant (CR-001 SECRET-01): boundary stops at the top level, so nested secrets survive."""
    if isinstance(node, Mapping):
        found.extend(str(k) for k in node if ob._is_secret_key(k))


def m_top_level_only_redaction(payload):
    """Mutant (CR-001 SECRET-01): redaction stops at the top level, so nested secrets survive."""
    if isinstance(payload, Mapping):
        return {str(k): (ob.REDACTED if ob._is_secret_key(k) else v) for k, v in payload.items()}
    return payload


def m_drop_unresolved_lineage(bundle, *, producer_ref):
    """Mutant (CR-001 LINEAGE-01): silently drops unresolvable causal refs instead of failing closed."""
    project_id = bundle.project_id
    node_ids_by_proof: dict[str, list[str]] = {}
    per_proof = []
    for proof in bundle.proofs:
        nodes = lb.evidence_nodes_from_legacy_proof(proof, project_id=project_id, producer_ref=producer_ref)
        per_proof.append((proof, nodes))
        node_ids_by_proof.setdefault(proof.proof_id, []).extend(n.id for n in nodes)
    linked = []
    for proof, nodes in per_proof:
        resolvable = tuple(sorted({nid for c in (getattr(proof, "causal_refs", ()) or ()) for nid in node_ids_by_proof.get(c, ())}))
        linked.extend(dataclasses.replace(n, dependency_refs=resolvable) for n in nodes)
    return lb.EvidenceGraph(project_id, tuple(linked))


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
    ("M7 STALE_STATE made retryable (CR-001 RETRY-01)", ob, "is_retryable", m_stale_state_retryable,
     "test_kernel_readiness", "test_stale_state_is_not_generically_retryable"),
    ("M7b retry allow-list narrowed wrongly (CR-001 RETRY-01)", ob, "is_retryable", m_stale_state_retryable,
     "test_kernel_readiness", "test_retry_allowlist_is_exhaustive_over_error_kinds"),
    ("M8 nested secret walk non-recursive (CR-001 SECRET-01)", ob, "_walk_secret_paths", m_top_level_only_secret_walk,
     "test_kernel_readiness", "test_nested_secret_keys_are_rejected_and_redacted"),
    ("M8b nested secret in sequence survives (CR-001 SECRET-01)", ob, "_walk_secret_paths", m_top_level_only_secret_walk,
     "test_kernel_readiness", "test_secret_in_sequence_of_mappings_is_rejected_and_redacted"),
    ("M8c redaction non-recursive (CR-001 SECRET-01)", ob, "redact_secrets", m_top_level_only_redaction,
     "test_kernel_readiness", "test_nested_secret_keys_are_rejected_and_redacted"),
    ("M9 unresolved lineage silently dropped (CR-001 LINEAGE-01)", lb, "evidence_graph_from_legacy_bundle", m_drop_unresolved_lineage,
     "test_legacy_evidence_bridge", "test_unresolvable_causal_refs_fail_closed"),
    ("M9b partial lineage loss silently dropped (CR-001 LINEAGE-01)", lb, "evidence_graph_from_legacy_bundle", m_drop_unresolved_lineage,
     "test_legacy_evidence_bridge", "test_partially_unresolvable_causal_refs_fail_closed"),
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
