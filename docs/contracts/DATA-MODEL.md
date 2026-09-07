# Data Model Contract

## Entities
**Project**: id, name, status, policy_set, budgets, timestamps.  
**Production**: id, project_id, type, canonical_intent_ref, graph_version, status, active_snapshot.  
**GraphNode**: id, stable_key, node_type, spec_version, input_fingerprint, state, invalidation_reason.  
**GraphEdge**: from, to, edge_type, contract_version.  
**ExecutionPlan**: node, planner version, hardware profile, model/provider, precision/offload/chunk plan, predicted cost/time/memory, rationale.  
**Run/Attempt**: plan, attempt, worker, state, timing, metrics, error.  
**Artifact**: run, media type, object key, hash, media metadata, derived_from, provenance.  
**Evaluation**: artifact, judge/version, score, confidence, verdict, evidence.  
**RepairPlan**: failed artifact, defects, strategy, affected scope, predicted cost, state.  
**Approval**: subject, actor, decision, criteria, evidence bundle, time.  
**DNA**: type, entity, version, invariants, mutable fields, constraints, references.  
**IRDocument**: type/version/payload/source intent/compilation.  
**HardwareProfile**: worker, genome version, declared + empirical capabilities.  
**ModelProfile**: provider/model/version/license/capabilities/empirical metrics/drift.  
**MemoryEntry**: scope, modality, source, index refs, validity, provenance, retention.  
**ProvenanceRecord**: artifact, parents, transformation, execution refs, actor, hashes.  
**RightsRecord**: subject, right type, license/consent, restrictions, evidence, validity.  
**EvidenceBundle**: work order, base/head, checks, artifacts, risks, verdict.

## Invariants
Binary media are referenced, not embedded in transactional rows. Vector indexes are derived/rebuildable. Stable IDs do not encode providers. Governed deletion respects lineage/retention. Serialized contracts include schema version.
