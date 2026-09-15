"""A1 focused M04 contract/service tests: canonical IR integrity, locks and migration."""
import asyncio

from ugas.foundation.contracts import IRDocument, content_fingerprint_of
from ugas.modules.m04_multimodal_ir.domain import (
    MISSING, assert_locks_preserved, assert_reference_integrity, resolve_path, seal_canonical,
)
from ugas.modules.m04_multimodal_ir.errors import ValidationError
from ugas.modules.m04_multimodal_ir.services_deep import IRCompiler, IRMigrationService, IRValidator
import pytest


def run(coro):
    return asyncio.run(coro)


def _ir(version=1, intent=None, locked=(), references=(), fingerprint="pending"):
    return IRDocument("ir-1", version, fingerprint, "p", "image",
                      intent if intent is not None else {"subject": {"wardrobe": "blue"}}, locked, references)


def test_resolve_path_finds_nested_value_and_reports_missing():
    intent = {"subject": {"wardrobe": "blue"}}
    assert resolve_path(intent, "subject.wardrobe") == "blue"
    assert resolve_path(intent, "subject.absent") is MISSING
    with pytest.raises(ValidationError):
        resolve_path(intent, "  ")


def test_reference_integrity_rejects_unknown_references():
    with pytest.raises(ValidationError):
        assert_reference_integrity(("known", "ghost"), {"known"})
    assert_reference_integrity(("known",), {"known"}) is None


def test_reference_integrity_rejects_duplicates_and_blanks():
    with pytest.raises(ValidationError):
        assert_reference_integrity(("a", "a"), {"a"})
    with pytest.raises(ValidationError):
        assert_reference_integrity(("",), None)


def test_absent_reference_universe_does_not_mean_valid():
    """With no universe supplied only intrinsic defects are checked; unknown ids are not assumed to resolve."""
    assert_reference_integrity(("anything",), None) is None


def test_compiler_seals_a_content_derived_fingerprint():
    compiled = run(IRCompiler().execute(_ir()))
    assert compiled.fingerprint == content_fingerprint_of(compiled)
    assert compiled.fingerprint != "pending"


def test_compiler_rejects_unsupported_schema_version():
    with pytest.raises(ValidationError):
        run(IRCompiler().execute(_ir(version=9)))


def test_compiler_rejects_lock_path_that_does_not_resolve():
    with pytest.raises(ValidationError):
        run(IRCompiler().execute(_ir(locked=("subject.absent",))))


def test_compiler_rejects_broken_references():
    with pytest.raises(ValidationError):
        run(IRCompiler(known_refs={"a"}).execute(_ir(references=("a", "ghost"))))


def test_validator_reports_declared_fingerprint_mismatch_without_rewriting():
    document = _ir(fingerprint="stale")
    verdict = run(IRValidator().execute(document))
    assert verdict["valid"] is True
    assert verdict["declared_fingerprint_matches_content"] is False
    assert document.fingerprint == "stale", "validator must not mutate its input"


def test_validator_accepts_a_sealed_document():
    sealed = seal_canonical(_ir())
    assert run(IRValidator().execute(sealed))["declared_fingerprint_matches_content"] is True


def test_migration_preserves_locks_and_bumps_version():
    original = _ir(locked=("subject.wardrobe",))
    migrated = run(IRMigrationService().execute(original))
    assert migrated.version == 2
    assert migrated.locked_paths == original.locked_paths
    assert resolve_path(migrated.intent, "subject.wardrobe") == "blue"
    assert migrated.fingerprint == content_fingerprint_of(migrated)


def test_migration_rejects_unknown_target_version():
    with pytest.raises(ValidationError):
        run(IRMigrationService().execute(_ir(version=7)))


def test_locked_path_mutation_is_rejected():
    canonical = _ir(intent={"subject": {"wardrobe": "blue"}}, locked=("subject.wardrobe",))
    tampered = _ir(intent={"subject": {"wardrobe": "red"}}, locked=("subject.wardrobe",))
    with pytest.raises(ValidationError):
        assert_locks_preserved(canonical, tampered)


def test_dropping_a_declared_lock_is_rejected():
    canonical = _ir(locked=("subject.wardrobe",))
    unlocked = _ir(intent={"subject": {"wardrobe": "blue"}}, locked=())
    with pytest.raises(ValidationError):
        assert_locks_preserved(canonical, unlocked)


def test_migrated_document_carries_a_valid_declared_fingerprint():
    from ugas.foundation.contracts import assert_fingerprint

    migrated = run(IRMigrationService().execute(_ir(locked=("subject.wardrobe",))))
    assert_fingerprint(migrated)
