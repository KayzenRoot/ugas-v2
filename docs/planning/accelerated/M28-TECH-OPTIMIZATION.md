# M28 — Export & Delivery: 2026 Technology Optimization
Status: AUTHORIZED CANDIDATE / accelerated planning

## Additions
- **Delivery Compiler:** compile accepted masters into target-specific derivative/package graphs for game engines, web, social, print, streaming and archives.
- **Runtime Contract Validation:** package is tested against target constraints before DELIVERY_ACCEPTED.
- **Multi-Target Delta Export:** changing one target derivative does not rebuild unrelated delivery targets.
- **Provenance-Preserving Export:** C2PA/credentials/watermark and internal lineage preserved or transformed with explicit evidence where supported.
- **Adaptive Media Packaging:** codec/resolution/LOD/texture/audio profiles selected from delivery contract, not ad hoc presets.
- **Delivery Rehearsal:** dry-run manifests validate files, names, checksums, dependencies, rights and size budgets before publish.
- **Rollback/Revocation Manifest:** every published release maps back to immutable production snapshot and supports governed replacement/revocation metadata.

## Hard rules
Only DELIVERY_ACCEPTED artifacts can enter production publishing paths. Export conversion cannot silently lower a hard quality/right/security requirement.