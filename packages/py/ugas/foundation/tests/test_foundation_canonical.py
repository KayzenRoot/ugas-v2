"""A1 canonical serialization / fingerprint contract tests for the S01 foundation.

The recorded digests are migration tripwires: they were captured from this implementation so that any change
to canonicalization fails the suite until someone makes an explicit schema/version decision. They are not
independent proof of correctness - that is what the property assertions below them are for.
"""
from ugas.foundation.contracts import (
    AssetDNA, GraphEdge, GraphNode, IRDocument, KnowledgeState, ModelProfile, NodeState,
    ProductionGraph, QualificationState, ResourceEnvelope, assert_fingerprint, canonical_dict,
    canonical_json, content_fingerprint_of, fingerprint_matches,
)
from ugas.foundation.fingerprinting import (
    CANONICAL_VECTOR_VERSION, CanonicalizationError, canonical_bytes, content_fingerprint, fingerprint,
)
import pytest


def _ir(intent=None, locked=(), references=()):
    return IRDocument("ir-1", 1, "declared", "p", "image", intent if intent is not None else {"a": 1, "b": 2}, locked, references)


def test_canonical_vector_version_is_pinned():
    assert CANONICAL_VECTOR_VERSION == 1, "bump CANONICAL_VECTOR_VERSION only with an explicit schema decision"


def test_mapping_key_order_cannot_change_digest():
    first = _ir({"alpha": 1, "beta": {"x": 1, "y": 2}})
    second = _ir({"beta": {"y": 2, "x": 1}, "alpha": 1})
    assert canonical_bytes(first) == canonical_bytes(second)
    assert content_fingerprint_of(first) == content_fingerprint_of(second)


def test_set_and_frozenset_order_cannot_change_digest():
    a = AssetDNA("d", 1, "f", "p", "asset", {"k": frozenset({"z", "a", "m"})}, {})
    b = AssetDNA("d", 1, "f", "p", "asset", {"k": frozenset({"m", "z", "a"})}, {})
    assert canonical_bytes(a) == canonical_bytes(b)


def test_sequence_order_does_change_digest():
    """Sequences are semantic order: reordering them must be visible, unlike mapping/set order."""
    first = IRDocument("ir-1", 1, "declared", "p", "image", {}, ("a", "b"), ())
    second = IRDocument("ir-1", 1, "declared", "p", "image", {}, ("b", "a"), ())
    assert content_fingerprint_of(first) != content_fingerprint_of(second)


def test_semantic_change_alters_digest():
    assert content_fingerprint_of(_ir({"a": 1})) != content_fingerprint_of(_ir({"a": 2}))


def test_declared_fingerprint_field_is_excluded_from_content_digest():
    """A digest cannot include the value it determines."""
    one = IRDocument("ir-1", 1, "fingerprint-one", "p", "image", {"a": 1})
    two = IRDocument("ir-1", 1, "fingerprint-two", "p", "image", {"a": 1})
    assert content_fingerprint_of(one) == content_fingerprint_of(two)


def test_non_finite_floats_fail_closed():
    for bad in (float("nan"), float("inf"), float("-inf")):
        with pytest.raises(CanonicalizationError):
            canonical_bytes(_ir({"value": bad}))


def test_unsupported_values_fail_closed():
    class Opaque:
        pass

    with pytest.raises(CanonicalizationError):
        canonical_bytes(_ir({"value": Opaque()}))


def test_enum_values_are_normalized_not_stringified():
    """An enum must serialize as its value so a state rename is a schema event, not a silent digest change."""
    envelope = ResourceEnvelope("hw", 1, "fh", KnowledgeState.UNKNOWN, None, None, None, None)
    payload = canonical_dict(envelope)
    assert payload["knowledge"] == "unknown"
    assert not str(payload["knowledge"]).startswith("<")


def test_canonical_json_is_stable_for_equivalent_objects():
    assert canonical_json(_ir({"b": 2, "a": 1})) == canonical_json(_ir({"a": 1, "b": 2}))


def test_assert_fingerprint_rejects_stale_declaration():
    document = _ir()
    actual = content_fingerprint_of(document)
    fresh = IRDocument("ir-1", 1, actual, "p", "image", document.intent, document.locked_paths, document.references)
    assert fingerprint_matches(fresh)
    assert_fingerprint(fresh)
    with pytest.raises(ValueError):
        assert_fingerprint(document)


def test_default_declared_fingerprint_does_not_match_content():
    """The materialized default '' is explicitly not a valid content fingerprint."""
    assert not fingerprint_matches(_ir())


def test_fingerprint_namespace_separates_domains():
    assert fingerprint(1) != fingerprint(1, namespace="ugas:v3")


def test_recorded_canonical_tripwire():
    """Tripwire: this exact contract must keep producing this digest at CANONICAL_VECTOR_VERSION 1.

    Captured from this implementation. A failure here means canonicalization changed, which requires an
    explicit schema/version decision rather than a silent edit of this constant.
    """
    assert content_fingerprint_of(_ir()) == "27b0338c8536a3ead30c5074afd5ad55df36f1f2b34f618d3f29ec041a7528ba"
    assert canonical_json(_ir()) == (
        '{"id":"ir-1","intent":{"a":1,"b":2},"locked_paths":[],"modality":"image",'
        '"project_id":"p","references":[],"version":1}'
    )
