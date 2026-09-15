from __future__ import annotations

"""M09 motion retarget acceptance rules."""
from dataclasses import dataclass
from typing import Mapping

from .contracts import MotionClip


@dataclass(frozen=True, slots=True)
class SkeletonBinding:
    source_skeleton_ref: str
    target_skeleton_ref: str
    semantic_bone_map: Mapping[str, str]


@dataclass(frozen=True, slots=True)
class MotionObservation:
    semantic_motion_score: float
    contact_errors: Mapping[str, float]
    evaluator_ref: str


@dataclass(frozen=True, slots=True)
class MotionPolicy:
    minimum_semantic_score: float
    maximum_contact_error: float
    required_semantic_bones: frozenset[str]


def validate_retarget(clip: MotionClip, binding: SkeletonBinding, observation: MotionObservation, policy: MotionPolicy) -> tuple[str, ...]:
    if not observation.evaluator_ref:
        raise ValueError("motion evaluation requires evidence")
    failures: list[str] = []
    missing = policy.required_semantic_bones - set(binding.semantic_bone_map)
    if missing:
        failures.extend(f"MISSING_SEMANTIC_BONE:{bone}" for bone in sorted(missing))
    if observation.semantic_motion_score < policy.minimum_semantic_score:
        failures.append("MOTION_SEMANTICS_DRIFT")
    for contact in sorted(clip.contact_constraints):
        if float(observation.contact_errors.get(contact, float("inf"))) > policy.maximum_contact_error:
            failures.append(f"CONTACT_VIOLATION:{contact}")
    return tuple(failures)


# CODEX-TASK[M09-RETARGET-PLAN]
# Build deterministic RetargetPlan from semantic roles, never raw bone index ordering.
# Preserve motion intent and identity/body constraints; local contact repair before clip regeneration.
