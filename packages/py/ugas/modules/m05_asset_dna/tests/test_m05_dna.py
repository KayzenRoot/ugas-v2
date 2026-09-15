"""A1 focused M05 tests: canonical identity, locked traits, lineage and deterministic derivative fingerprints."""
import asyncio

from ugas.foundation.contracts import AssetDNA, assert_fingerprint
from ugas.modules.m05_asset_dna.domain import (
    assert_variable_traits_allowed, compile_variation, seal_identity,
)
from ugas.modules.m05_asset_dna.errors import ValidationError
from ugas.modules.m05_asset_dna.services_deep import (
    AssetDNAService, IdentityConsistencyService, VariationCompiler,
)
import pytest


def run(coro):
    return asyncio.run(coro)


def _canonical():
    sealed = seal_identity(AssetDNA("dna", 1, "pending", "p", "hero",
                                    {"face": "A", "body": "slim"}, {"hair": "black", "outfit": "casual"},
                                    None))
    return sealed


def test_canonical_dna_is_sealed_with_a_content_fingerprint():
    dna = run(AssetDNAService().execute(AssetDNA("dna", 1, "pending", "p", "hero", {"face": "A"}, {}, None)))
    assert dna.fingerprint != "pending"
    assert_fingerprint(dna)


def test_canonical_identity_is_required():
    with pytest.raises(ValidationError):
        run(AssetDNAService().execute(AssetDNA("dna", 1, "pending", "p", "   ", {}, {}, None)))


def test_derivative_references_the_canonical_parent_fingerprint():
    canonical = _canonical()
    derivative = compile_variation(canonical, {"hair": "silver"}, derivative_id="dna-v1")
    assert derivative.parent_fingerprint == canonical.fingerprint


def test_derivative_preserves_identity_and_locked_traits():
    canonical = _canonical()
    derivative = compile_variation(canonical, {"hair": "silver"}, derivative_id="dna-v1")
    assert derivative.canonical_asset_id == canonical.canonical_asset_id
    assert derivative.locked_traits == canonical.locked_traits


def test_derivative_fingerprint_is_deterministic_and_content_derived():
    canonical = _canonical()
    first = compile_variation(canonical, {"hair": "silver"}, derivative_id="dna-v1")
    second = compile_variation(canonical, {"hair": "silver"}, derivative_id="dna-v1")
    assert first.fingerprint == second.fingerprint
    assert first.fingerprint != canonical.fingerprint, "a varied derivative must not share the canonical digest"
    assert_fingerprint(first)


def test_varying_a_locked_trait_is_rejected():
    canonical = _canonical()
    with pytest.raises(ValidationError):
        compile_variation(canonical, {"face": "B"}, derivative_id="dna-v1")


def test_varying_the_canonical_identity_is_rejected():
    canonical = _canonical()
    with pytest.raises(ValidationError):
        assert_variable_traits_allowed(canonical, {"canonical_asset_id": "villain"})


def test_identity_consistency_service_confirms_a_valid_derivative():
    canonical = _canonical()
    derivative = compile_variation(canonical, {"hair": "silver"}, derivative_id="dna-v1")
    report = run(IdentityConsistencyService().execute({"canonical": canonical, "derivative": derivative}))
    assert report["consistent"] is True
    assert report["parent_fingerprint"] == canonical.fingerprint


def test_identity_consistency_service_rejects_a_foreign_derivative():
    canonical = _canonical()
    foreign = seal_identity(AssetDNA("dna-x", 2, "pending", "p", "villain", {}, {}, canonical.fingerprint))
    with pytest.raises(ValidationError):
        run(IdentityConsistencyService().execute({"canonical": canonical, "derivative": foreign}))


def test_variation_compiler_requires_its_full_request():
    with pytest.raises(ValidationError):
        run(VariationCompiler().execute({"canonical": _canonical()}))


def test_variation_compiler_applies_permitted_changes_only():
    canonical = _canonical()
    derivative = run(VariationCompiler().execute(
        {"canonical": canonical, "changes": {"outfit": "formal"}, "derivative_id": "dna-v2"}))
    assert derivative.variable_traits["outfit"] == "formal"
    assert derivative.variable_traits["hair"] == "black", "unvaried traits must be carried over"
