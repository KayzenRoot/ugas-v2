from __future__ import annotations

"""M15 faceless production recipe/channel consistency policy."""
from dataclasses import dataclass

from .contracts import ContentRecipe,ChannelVariant


@dataclass(frozen=True, slots=True)
class ChannelIdentity:
    id:str
    project_id:str
    fingerprint:str
    required_traits:frozenset[str]


@dataclass(frozen=True, slots=True)
class ChannelObservation:
    observed_traits:frozenset[str]
    hook_count:int
    segment_count:int
    evidence_ref:str


def validate_faceless_variant(variant:ChannelVariant,recipe:ContentRecipe,identity:ChannelIdentity,observation:ChannelObservation)->tuple[str,...]:
    if variant.project_id!=recipe.project_id or identity.project_id!=recipe.project_id:
        raise ValueError("faceless variant crosses project boundary")
    if variant.recipe_ref!=recipe.id or recipe.channel_identity_ref!=identity.id:
        raise ValueError("recipe/channel binding mismatch")
    if not observation.evidence_ref: raise ValueError("channel evaluation requires evidence")
    failures=[]
    missing=identity.required_traits-observation.observed_traits
    failures.extend(f"CHANNEL_TRAIT_MISSING:{trait}" for trait in sorted(missing))
    if observation.hook_count<len(recipe.hook_constraints): failures.append("HOOK_CONSTRAINTS_UNSATISFIED")
    if observation.segment_count<len(recipe.segment_constraints): failures.append("SEGMENT_CONSTRAINTS_UNSATISFIED")
    return tuple(failures)


# CODEX-TASK[M15-ASSEMBLY-BOUNDARY]
# Wire narrative/media assembly ports so channel variants are derivatives of canonical recipe,
# brand and approved claims. Channel optimization may change presentation, never locked truth/brand.
