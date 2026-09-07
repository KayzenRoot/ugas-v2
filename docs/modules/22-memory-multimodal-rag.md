# M22 — Memory & Multimodal RAG

**Round:** 22  
**Scope class:** CORE FOUNDATION / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Provide structured long-term project memory and retrieval across text, image, audio and production outcomes, independent of chat history.

## Responsibilities
- episodic/semantic memory
- project/character/asset/channel/brand/campaign/canon scopes
- text/visual/audio retrieval
- approved/failure outcome memory
- context budgeting
- staleness/invalidation
- retrieval explanations

## Planned capabilities
- ingest governed memories
- link memory to authoritative sources
- query by entity/scope/modality
- retrieve approved references
- retrieve prior failures/repairs
- context compaction
- invalidate stale entries
- rebuild vector indexes

## Candidate proprietary technologies
- **Creator Memory Engine** — cross-project/creative memory framework
- **Creative Episodic Memory** — event/production history
- **Asset Semantic Memory** — asset meaning/relationships
- **Generation Outcome Memory** — approved/rejected generation outcomes
- **Failure Memory** — defects and successful corrections
- **Visual RAG** — image/reference retrieval
- **Audio RAG** — audio/reference retrieval
- **Multimodal Reference Retrieval** — cross-modal search
- **Context Budget Manager** — selects bounded relevant context

## Inputs
- canonical project/docs
- accepted assets
- evaluations/repairs
- canon events
- references and embeddings

## Outputs
- ranked context bundle
- retrieval explanation
- memory records
- staleness state
- derived indexes

## How it works
1. Ingest only records tied to authoritative source/provenance and scope.
2. Normalize metadata and derive modality-specific embeddings/index features.
3. At task time, construct retrieval query from entity IDs, intent, constraints and history.
4. Rank relevant memories and fit them into explicit context budget.
5. Attach source IDs/provenance so downstream modules can distinguish fact/reference/suggestion.
6. When source changes, mark derived memories stale and rebuild indexes.
7. Store accepted/rejected outcome summaries as evidence for future routing/repair.

## Canonical data / contracts
- MemoryEntry
- EmbeddingRef
- RetrievalQuery
- ContextBundle
- MemoryValidity

## Dependencies
- M01 graph
- M05/M06 DNA
- M14 canon
- M19/M20 outcomes
- M23 provenance

## Failure modes and safeguards
- stale memory → invalidate
- wrong entity collision → stable-ID filtering
- retrieval overload → budget manager
- derived index lost → rebuild from authoritative records

## Observability
- precision/recall
- stale-hit rate
- context size
- source diversity
- retrieval explanation

## Security / rights
- scope/ACL filtering before retrieval
- untrusted retrieved text cannot modify policy
- private references retain classification

## Tests and benchmarks
- known-answer retrieval set
- staleness invalidation
- entity isolation
- index rebuild
- context budget determinism

## Acceptance criteria for first usable V2 path
- [ ] a new session/task reconstructs relevant project/character context from repository/system memory without chat dependence
- [ ] stale source is not presented as current
- [ ] retrieved item always points to authoritative origin

## Deliberately out of this module
- opaque chat transcript as source of truth
- unbounded personal memory unrelated to project

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
