# M23 — Provenance Rights & C2PA

**Round:** 23  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Maintain verifiable media genealogy, transformations, model/run metadata, licenses and consent through the full production lifecycle.

## Responsibilities
- provenance graph
- transformation ledger
- rights/licenses
- consent
- artifact hashes
- derived lineage
- risk/confidence
- Content Credentials/C2PA bridge
- audit/export

## Planned capabilities
- record model/provider/config/seed when available
- record parent/derived assets
- attach licenses/consent/restrictions
- compute hashes
- inspect full lineage
- propagate rights constraints
- export credential metadata
- detect missing/tampered chain

## Candidate proprietary technologies
- **Media Provenance Graph** — genealogy of media/assets
- **Rights Ledger** — rights/license records
- **Consent Ledger** — authorization records
- **Transformation Ledger** — ordered transformations
- **Provenance Confidence Score** — confidence in chain completeness
- **Rights Risk Engine** — flags missing/conflicting rights
- **Content Credential Bridge** — internal↔external credential mapping
- **C2PA Integration Layer** — C2PA/Content Credentials integration boundary

## Inputs
- Run/Artifact metadata
- parent lineage
- model/provider/version
- references
- rights/license/consent evidence
- transformations

## Outputs
- ProvenanceRecord graph
- RightsRecord
- ConsentRecord
- risk/confidence
- credential/export package

## How it works
1. Every producing run creates provenance tied to node, plan, model/provider version and artifact hash.
2. Derived transformations append parent edges rather than overwriting history.
3. Rights/licenses/consent attach to governed source identities/assets and propagate according to policy.
4. Before governed use/export, Rights Risk Engine checks missing, expired or incompatible restrictions.
5. Content Credential Bridge serializes supported external credential form without replacing internal records.
6. Hash/provenance inconsistencies quarantine the artifact for review.

## Canonical data / contracts
- ProvenanceRecord
- Transformation
- RightsRecord
- ConsentRecord
- CredentialRecord
- ArtifactHash

## Dependencies
- all producing modules
- M01 graph
- Security
- external C2PA integration

## Failure modes and safeguards
- missing parent → incomplete confidence/block according to policy
- hash mismatch → quarantine
- expired consent/license → block restricted use
- external credential unsupported → internal lineage still retained

## Observability
- lineage completeness
- rights risk count
- credential export success
- hash mismatches
- unknown origin rate

## Security / rights
- rights/consent evidence access restricted
- append/audit events protected from silent mutation
- no sensitive provider secrets in provenance

## Tests and benchmarks
- multi-step lineage
- rights propagation
- consent expiry
- tamper/hash mismatch
- C2PA adapter fixtures

## Acceptance criteria for first usable V2 path
- [ ] a derived asset can show complete internal lineage to governed sources
- [ ] restricted asset with missing/expired consent is blocked
- [ ] external credential export failure does not erase internal provenance

## Deliberately out of this module
- guaranteeing legal ownership
- replacing legal counsel
- assuming C2PA alone proves truth

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
