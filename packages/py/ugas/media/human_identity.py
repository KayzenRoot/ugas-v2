from __future__ import annotations

"""M06 digital-human identity/consent governance independent of generation provider."""
from dataclasses import dataclass
from typing import Mapping

from .contracts import ConsentState, IdentityBinding, MediaArtifact


@dataclass(frozen=True, slots=True)
class IdentityObservation:
    observed_traits: Mapping[str, float | str]
    similarity_score: float
    evaluator_ref: str


@dataclass(frozen=True, slots=True)
class IdentityPolicy:
    minimum_similarity: float
    required_locked_traits: frozenset[str]


def validate_identity(binding: IdentityBinding, observation: IdentityObservation, policy: IdentityPolicy) -> tuple[str, ...]:
    if binding.consent_state is not ConsentState.VERIFIED or not binding.consent_ref:
        raise ValueError("verified consent is required")
    if not observation.evaluator_ref:
        raise ValueError("identity evaluation requires evidence reference")
    failures: list[str] = []
    if observation.similarity_score < policy.minimum_similarity:
        failures.append("IDENTITY_SIMILARITY_BELOW_FLOOR")
    for trait in sorted(policy.required_locked_traits):
        if trait not in binding.locked_traits:
            failures.append(f"LOCKED_TRAIT_NOT_BOUND:{trait}")
        elif trait not in observation.observed_traits:
            failures.append(f"LOCKED_TRAIT_NOT_OBSERVED:{trait}")
    return tuple(failures)


def assert_artifact_identity(artifact: MediaArtifact, observation: IdentityObservation, policy: IdentityPolicy) -> None:
    if artifact.identity is None:
        raise ValueError("digital-human artifact has no identity binding")
    failures = validate_identity(artifact.identity, observation, policy)
    if failures:
        raise ValueError(";".join(failures))


# CODEX-TASK[M06-TRAIT-COMPARATORS]
# Add typed comparators for categorical/numeric/embedding-backed locked traits through evaluator ports.
# A hard identity/consent failure rejects the artifact and cannot be averaged away by visual quality.
