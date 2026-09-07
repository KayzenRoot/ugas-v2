# Context Lock Specification

A Work Order is executable only against an explicit context lock.

## Required
- repository;
- base SHA;
- active branch;
- checkpoint fingerprint;
- Scope fingerprint;
- DoD fingerprint;
- Architecture fingerprint;
- relevant ADR IDs/fingerprints;
- module spec fingerprint;
- requirement IDs;
- contract versions.

## Staleness
Mark STALE and recompile/rebase when any critical source above changes, or when the base branch advances in a way that intersects the Work Order.

## Goal
Keep executor context small, deterministic and independently verifiable.
