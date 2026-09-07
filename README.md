# UGAS V2

UGAS V2 is the canonical repository for the second major generation of UGAS: a local-first, provider-independent, hardware-agnostic multimodal generative media production operating system.

## Canonical-source rule

This repository is the source of truth for UGAS V2. Chat memory, temporary notes, external prompts, and model recollection are non-authoritative unless promoted into the canonical documentation through the governed project workflow.

Read sources in this order:

1. `docs/checkpoint/CURRENT.md`
2. `docs/decisions/DECISIONS-LEDGER.md` and accepted ADRs
3. `docs/SCOPE.md`
4. `docs/DEFINITION-OF-DONE.md`
5. `docs/ARCHITECTURE.md`
6. `docs/REQUIREMENTS.md`
7. module specifications under `docs/modules/`
8. remaining supporting sources

If sources conflict, higher-priority canonical sources prevail. Git history, tested code, CI results, and evidence bundles prevail over chat memory.

## Current phase

**PLANNING / SOURCE-PACK BOOTSTRAP**

No product implementation is authorized until the initial Source Pack, architecture, requirements, scope, test strategy, security model, decisions ledger, module specifications, backlog, Definition of Done, and checkpoint are present and reviewed.

## Product vision

UGAS V2 turns creative intent into a reproducible, inspectable, quality-gated multimodal Production Graph spanning image, video, animation, 3D, voice, music, sound design, narrative, advertising, brand/IP, localization, memory/RAG, provenance, rights, model intelligence, and adaptive compute.

## Development workflow

`ANALYZE → SOURCE CHECK → NEXT NECESSARY INCREMENT → WORK ORDER → CONTEXT LOCK → PREFLIGHT → EXECUTOR → TESTS/EVIDENCE → PR → AUDIT → APPROVED / CORRECTION REQUIRED / BLOCKED → CHECKPOINT DELTA → MERGE → NEXT`

No later increment may advance while the current increment requires correction or validation.

## Repository map

The detailed repository map and source hierarchy live in `docs/SOURCE-HIERARCHY.md`.

## License

Licensing has not yet been frozen for UGAS V2. Do not infer a public or open-source license until an ADR explicitly decides it.
