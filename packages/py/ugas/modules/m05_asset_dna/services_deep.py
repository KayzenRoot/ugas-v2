# GENERATED-DEEP-PREPROGRAMMED
"""M05 orchestration: canonical asset identity, consistency checking and variation compilation.

Identity is immutable: a derivative never silently changes the canonical asset id or a locked trait, and it
always references the canonical parent fingerprint so lineage stays addressable.
"""
from __future__ import annotations

from typing import Any, Mapping

from ugas.foundation.contracts import AssetDNA
from ugas.foundation.invariants import assert_dna_derivative

from .domain import assert_variable_traits_allowed, compile_variation, seal_identity
from .errors import ValidationError


class AssetDNAService:
    """PREPROGRAMMED orchestration boundary for M05."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> AssetDNA:
        """Seal a canonical DNA record with a fingerprint derived from its semantic content."""
        if not isinstance(request, AssetDNA):
            raise ValidationError("AssetDNAService requires a canonical AssetDNA")
        if not request.canonical_asset_id.strip():
            raise ValidationError("canonical asset identity must be explicit")
        sealed = seal_identity(request)
        store = self._ports.get("store")
        if store is not None:
            await store.put(sealed)
        return sealed


class IdentityConsistencyService:
    """PREPROGRAMMED orchestration boundary for M05."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> dict[str, Any]:
        """Verify a derivative against its canonical parent."""
        if not isinstance(request, Mapping) or {"canonical", "derivative"} - set(request):
            raise ValidationError("IdentityConsistencyService requires canonical and derivative DNA")
        canonical, derivative = request["canonical"], request["derivative"]
        if not isinstance(canonical, AssetDNA) or not isinstance(derivative, AssetDNA):
            raise ValidationError("identity consistency requires canonical AssetDNA values")
        try:
            assert_dna_derivative(canonical, derivative)
        except ValueError as exc:
            # Translate the shared foundation invariant into this module's typed failure so callers never see a
            # bare ValueError crossing the M05 boundary.
            raise ValidationError(f"derivative is not consistent with its canonical parent: {exc}") from None
        return {
            "consistent": True,
            "canonical_asset_id": canonical.canonical_asset_id,
            "parent_fingerprint": derivative.parent_fingerprint,
            "locked_traits": tuple(sorted(canonical.locked_traits)),
        }


class VariationCompiler:
    """PREPROGRAMMED orchestration boundary for M05."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> AssetDNA:
        """Compile a derivative that varies only permitted variable traits of the canonical DNA."""
        if not isinstance(request, Mapping) or {"canonical", "changes", "derivative_id"} - set(request):
            raise ValidationError("VariationCompiler requires canonical, changes and derivative_id")
        canonical = request["canonical"]
        if not isinstance(canonical, AssetDNA):
            raise ValidationError("VariationCompiler requires a canonical AssetDNA")
        changes = request["changes"]
        assert_variable_traits_allowed(canonical, changes)
        return compile_variation(canonical, changes, derivative_id=str(request["derivative_id"]))


# CODEX-TASK[M05-AssetDNAService] / [M05-IdentityConsistencyService] / [M05-VariationCompiler]
# DONE: all three implemented against canonical foundation DNA contracts with typed errors.py failures and no
#       provider or persistence dependency.
