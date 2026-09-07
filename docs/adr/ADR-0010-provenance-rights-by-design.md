# ADR-0010 — Provenance and rights by design

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
Media generation may involve references, identities, models, licenses, consent and many transformations. Post-hoc reconstruction is unreliable.

## Decision
Every governed artifact records production lineage, hashes and applicable rights/consent metadata. C2PA/content credentials are integration/export layers over internal provenance.

## Consequences
- auditability improves
- missing rights can block governed use
- provenance data becomes cross-cutting schema

## Alternatives considered
- Add provenance at export only: rejected
- Use C2PA alone as internal truth: rejected because internal workflow detail is richer and C2PA is an external standard boundary

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
