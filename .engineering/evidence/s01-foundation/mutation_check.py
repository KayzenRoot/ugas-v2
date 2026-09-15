"""S01 safety-strength mutation harness.

Each mutation replaces a safety-critical S01 function with a deliberately wrong implementation, then re-imports
the test modules and runs the test that is supposed to catch it. A mutant that is NOT caught means the
corresponding guard is vacuous - a green suite alone would not have told us that.

Every consumer module is patched, not just the defining one: `from x import f` binds f at import time, so
patching only the definition would leave an already-bound reference pointing at the correct function and the
harness would report a false MISS.

Run from the repository root:
    <venv>/Scripts/python.exe -B .engineering/evidence/s01-foundation/mutation_check.py

Exit code 0 means every mutation was caught.
"""
from __future__ import annotations

import importlib
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "packages" / "py"))

import ugas.foundation.contracts as _contracts  # noqa: E402
import ugas.foundation.fingerprinting as _fingerprinting  # noqa: E402
import ugas.foundation.idempotency as _idempotency  # noqa: E402
import ugas.foundation.invalidation as _invalidation  # noqa: E402
import ugas.foundation.invariants as _invariants  # noqa: E402
import ugas.foundation.routing as _routing  # noqa: E402
import ugas.modules.m01_product_production_os.domain as _m01_domain  # noqa: E402
import ugas.modules.m02_hardware_intelligence.domain as _m02_domain  # noqa: E402
import ugas.modules.m03_model_intelligence.domain as _m03_domain  # noqa: E402
import ugas.modules.m03_model_intelligence.services_deep as _m03_services  # noqa: E402
import ugas.modules.m04_multimodal_ir.domain as _m04_domain  # noqa: E402
import ugas.modules.m04_multimodal_ir.services_deep as _m04_services  # noqa: E402
import ugas.modules.m05_asset_dna.domain as _m05_domain  # noqa: E402
import ugas.modules.m05_asset_dna.services_deep as _m05_services  # noqa: E402

TEST_MODULES = [
    "ugas.foundation.tests.test_foundation_canonical",
    "ugas.foundation.tests.test_foundation_lifecycle",
    "ugas.foundation.tests.test_foundation_idempotency",
    "ugas.foundation.tests.test_foundation_routing",
    "ugas.foundation.tests.test_s01_golden_path",
    "ugas.modules.m01_product_production_os.tests.test_m01_lifecycle",
    "ugas.modules.m02_hardware_intelligence.tests.test_m02_hardware",
    "ugas.modules.m03_model_intelligence.tests.test_m03_routing",
    "ugas.modules.m04_multimodal_ir.tests.test_m04_ir",
    "ugas.modules.m05_asset_dna.tests.test_m05_dna",
]


def _reload_tests():
    loaded = {}
    for name in TEST_MODULES:
        sys.modules.pop(name, None)
    for name in TEST_MODULES:
        loaded[name.rsplit(".", 1)[-1]] = importlib.import_module(name)
    return loaded


def _expect_failure(module, test_name):
    try:
        getattr(module, test_name)()
    except BaseException:  # noqa: BLE001
        # BaseException, not Exception: pytest's own assertion failure type derives from BaseException rather
        # than Exception, so catching Exception alone would let a correctly-caught mutant escape the harness.
        return True
    return False


# ---- mutants ---------------------------------------------------------------------------------------

def _always_legal(before, after):
    """Mutant: any state transition is accepted."""


def _never_cyclic(node_ids, edges):
    """Mutant: cycles are never detected."""


def _locks_never_checked(before, after):
    """Mutant: migration may change locked values."""


def _dna_derivative_unchecked(canonical, derivative):
    """Mutant: a derivative may change identity and locked traits."""


def _invalidate_everything(graph, changed_node_ids):
    """Mutant: invalidation is global rather than limited to the causal cone."""
    return tuple(sorted(node.id for node in graph.nodes))


def _zero_for_missing(missing):
    """Mutant: absent telemetry is coerced to a measured zero instead of staying unknown."""


def _route_any_order(models, requirements, hardware):
    """Mutant: ranking follows input order instead of a deterministic tie-break."""
    return tuple(r for m in models if (r := _routing.score_model(m, requirements, hardware)) is not None)


def _everything_routable(model):
    """Mutant: unqualified models are treated as routable."""
    return None


def _fingerprint_includes_declared_field(value):
    """Mutant: the declared fingerprint is folded into its own content digest."""
    return _fingerprinting.fingerprint(_fingerprinting.canonical_value(value))


def _replay_reexecutes(store, record):
    """Mutant helper: a committed record is ignored so the mutation runs again."""
    return _idempotency.IdempotencyState.STARTED


# ---- mutation registry -----------------------------------------------------------------------------
# (label, [(module, attr, mutant)], test_module_key, test_name)
MUTATIONS = [
    ("M1 illegal transition accepted",
     [(_invariants, "assert_legal_transition", _always_legal), (_m01_domain, "assert_legal_transition", _always_legal)],
     "test_foundation_lifecycle", "test_illegal_transition_is_rejected"),

    ("M2 graph cycle accepted",
     [(_invariants, "assert_acyclic", _never_cyclic)],
     "test_foundation_lifecycle", "test_cycle_is_rejected"),

    ("M3 locked IR path mutated",
     [(_m04_domain, "assert_locks_preserved", _locks_never_checked),
      (_m04_services, "assert_locks_preserved", _locks_never_checked)],
     "test_m04_ir", "test_locked_path_mutation_is_rejected"),

    ("M4 locked IR path accepted by the compiler",
     [(_m04_domain, "assert_locks_resolvable", _locks_never_checked),
      (_m04_services, "assert_locks_resolvable", _locks_never_checked)],
     "test_m04_ir", "test_compiler_rejects_lock_path_that_does_not_resolve"),

    ("M4b DNA derivative identity/lock guard removed",
     [(_invariants, "assert_dna_derivative", _dna_derivative_unchecked),
      (_m05_services, "assert_dna_derivative", _dna_derivative_unchecked),
      (_m05_domain, "assert_dna_derivative", _dna_derivative_unchecked)],
     "test_m05_dna", "test_identity_consistency_service_rejects_a_foreign_derivative"),

    ("M5 unrelated proofs invalidated",
     [(_invalidation, "downstream_invalidation", _invalidate_everything)],
     "test_foundation_lifecycle", "test_sibling_is_not_invalidated"),

    ("M6 UNKNOWN hardware coerced to measured zero",
     [(_m02_domain, "normalize_probe", lambda raw, **kw: _m02_domain.normalize_probe(
         {k: (0 if v is None else v) for k, v in {**raw, "knowledge": None}.items()}, **kw))],
     "test_m02_hardware", "test_absent_telemetry_is_unknown_not_zero"),

    ("M7 unqualified model routed",
     [(_m03_domain, "assert_routable", _everything_routable)],
     "test_m03_routing", "test_only_qualified_or_promoted_models_are_routable"),

    ("M8 non-deterministic tie-break",
     [(_routing, "rank_routes", _route_any_order),
      (_m03_services, "rank_routes", _route_any_order),
      (_m03_domain, "ROUTABLE_QUALIFICATIONS", frozenset())],
     "test_foundation_routing", "test_input_order_cannot_change_the_winner"),

    ("M9 declared fingerprint folded into its own digest",
     [(_contracts, "content_fingerprint_of", _fingerprint_includes_declared_field)],
     "test_foundation_canonical", "test_declared_fingerprint_field_is_excluded_from_content_digest"),

    ("M10 committed replay re-executes the mutation",
     [(_idempotency, "IdempotencyState",
       type("S", (), {"STARTED": "started", "COMMITTED": "started", "FAILED": "failed"}))],
     "test_foundation_idempotency", "test_committed_replay_does_not_execute_the_mutation_twice"),
]


def main() -> int:
    print("S01 SAFETY-STRENGTH MUTATION HARNESS")
    print("=" * 78)
    results = []
    for label, patches, test_module_key, test_name in MUTATIONS:
        backups = [(module, attr, getattr(module, attr)) for module, attr, _ in patches]
        for module, attr, mutant in patches:
            setattr(module, attr, mutant)
        tests = _reload_tests()
        caught = _expect_failure(tests[test_module_key], test_name)
        for module, attr, original in backups:
            setattr(module, attr, original)
        results.append((label, caught, test_name))
        print(f"{'CAUGHT ' if caught else 'MISSED '} {label}  -> {test_name}")

    _reload_tests()
    print("=" * 78)
    missed = [r for r in results if not r[1]]
    print(f"MUTATIONS={len(results)} CAUGHT={len(results) - len(missed)} MISSED={len(missed)}")
    print(f"MUTATION_SCORE={len(results) - len(missed)}/{len(results)}")
    return 1 if missed else 0


if __name__ == "__main__":
    sys.exit(main())
