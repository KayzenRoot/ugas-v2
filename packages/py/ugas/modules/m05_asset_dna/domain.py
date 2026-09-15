# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
"""M05 pure domain logic: immutable asset identity, variation boundaries and derivative lineage.

A derivative may vary only what the canonical DNA leaves variable. Identity, locked traits and the parent
lineage key are structural, so violating them is an invariant failure rather than a validation nicety.
"""
from __future__ import annotations

from dataclasses import replace
from typing import Any, Mapping

from ugas.foundation.contracts import AssetDNA, content_fingerprint_of
from ugas.foundation.invariants import assert_dna_derivative

from .errors import ValidationError

IDENTITY_KEY = "canonical_asset_id"


def assert_variable_traits_allowed(canonical: AssetDNA, changes: Mapping[str, Any]) -> None:
    """Reject any variation that targets a locked trait or the canonical identity."""
    for trait in sorted(changes):
        if trait == IDENTITY_KEY:
            raise ValidationError("canonical asset identity cannot be varied")
        if trait in canonical.locked_traits:
            raise ValidationError(f"locked trait cannot be varied: {trait}")


def seal_identity(dna: AssetDNA) -> AssetDNA:
    """Return the DNA with a fingerprint derived from its semantic content."""
    return replace(dna, fingerprint=content_fingerprint_of(dna))


def compile_variation(canonical: AssetDNA, changes: Mapping[str, Any], *, derivative_id: str) -> AssetDNA:
    """Compile a derivative that varies only permitted variable traits.

    The derivative keeps the canonical identity and every locked trait, records the canonical parent
    fingerprint as its lineage key, and is re-sealed so its own fingerprint reflects the varied content.
    """
    assert_variable_traits_allowed(canonical, changes)
    variable = dict(canonical.variable_traits)
    variable.update(changes)
    draft = AssetDNA(
        id=derivative_id,
        version=canonical.version + 1,
        fingerprint="pending",
        project_id=canonical.project_id,
        canonical_asset_id=canonical.canonical_asset_id,
        locked_traits=dict(canonical.locked_traits),
        variable_traits=variable,
        parent_fingerprint=canonical.fingerprint,
    )
    derivative = seal_identity(draft)
    assert_dna_derivative(canonical, derivative)
    return derivative


def validate_invariants(command):
    if not command.operation:
        raise ValidationError("operation is required")
    return command


# CODEX-TASK[M05-CORE]
# DONE: variation boundaries, lock/identity preservation and parent-lineage keys are enforced here; the
#       derivative check itself is delegated to the shared foundation invariant rather than re-implemented.
