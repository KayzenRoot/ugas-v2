# Deployment — UGAS V2

## Initial model
Local-first developer/operator installation with optional LAN/cloud GPU workers.

## Components
Control/dashboard; domain/API; scheduler; worker(s); metadata DB; artifact/object store; cache/queue; vector/retrieval when enabled; observability.

## Environments
DEV → TEST → STAGING-like validation → RELEASE. Releases must be reproducible from versioned configuration.

## Config precedence
defaults → versioned non-secret config → site/environment config → secret store → explicit operator override.

## Worker enrollment
Workers authenticate and advertise Hardware Genome, runtimes, model/cache inventory, health and capacity before accepting leases.

## Upgrade/recovery
Persistent schema changes require migrations, compatibility notes, backup requirements and rollback or roll-forward. Application rollback must not silently corrupt newer schema state.

## Release evidence
Exact SHA/tag; artifact hashes; migrations; required tests; security checks; known limitations; rollback/roll-forward; checkpoint.
