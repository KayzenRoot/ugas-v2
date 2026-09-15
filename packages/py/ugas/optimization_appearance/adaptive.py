from __future__ import annotations
from .contracts import ExperienceContext,ExperienceVariant

PROTECTED_DIMENSIONS=frozenset({"rights","safety","truth","brand_lock","canonical_identity"})

def validate_variant(context:ExperienceContext,variant:ExperienceVariant)->None:
    if not context.privacy_scope_ref: raise ValueError("adaptive context requires privacy scope")
    forbidden=variant.changed_dimensions & PROTECTED_DIMENSIONS
    if forbidden: raise ValueError(f"adaptive experience cannot change protected dimensions: {sorted(forbidden)}")
    if not variant.reversible: raise ValueError("adaptive variant must be reversible")
    if variant.experiment_variable is not None and len(variant.changed_dimensions)!=1:
        raise ValueError("controlled experiment must isolate one changed dimension")

# CODEX-TASK[M35-ACCESSIBILITY-PRIVACY]
# Add explicit allowed-context policy, aggregate/cohort-first analytics, accessibility production transforms
# and experiment evidence. Engagement metrics never override rights/safety/truth/brand/accessibility gates.
