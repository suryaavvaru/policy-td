# Artifact access

The public repository contains the modular Policy-TD method contract, documentation, curated frozen-release tables, manifests, and verification scripts.

Large runtime artifacts are intentionally kept out of git. The public-clean frozen runtime archive is intended to be attached to the manuscript/preprint release.

## Public-clean frozen archive

```text
Policy-TD_frozen_runtime_archive_v0.1.0.tar.gz
SHA-256: 92f8393af023988ecbaa1a434da5131a1d88040ad54fdb0bd5aad5fd2f7d3c0e
```

## Intended contents

The archive preserves:

- curated frozen runtime result artifacts;
- final table-generation provenance;
- internal heldout and public external evaluation provenance;
- manifests and verification material needed to audit the paper-facing results.

## Checkpoint boundary

Trained guide checkpoints, if released, should be staged as a separate versioned bundle. Raw provider transcripts, credentials, local workbench state, and exploratory logs are not part of the public artifact.

See [`public_release_scope.md`](public_release_scope.md) for the release boundary.
