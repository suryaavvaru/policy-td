# Artifact index

This document maps the public Policy-TD repository to its main research artifacts.

## Code

- `src/policy_td/core/`: runtime action vocabulary and constants.
- `src/policy_td/labels/`: teacher-label schema and validation.
- `src/policy_td/runtime/`: controller decision utilities.
- `src/policy_td/eval/`: paired helped/harmed metrics.
- `src/policy_td/data/`: JSONL utilities.
- `src/policy_td/cli/`: command-line inspection tools.

## Result tables

Primary frozen-release tables are stored in:

    results/frozen_release/internal_plus_real_external/

External-style stress benchmark tables are stored in:

    results/frozen_release/external_style/

## Benchmark reports

Benchmark report files are stored in:

    data/benchmarks/internal_heldout_report.json
    data/benchmarks/external_style_report.json
    data/benchmarks/real_external_report.json

## Frozen runtime archive

Artifact name:

    Policy-TD_frozen_runtime_archive_v0.1.0.tar.gz

SHA-256:

    92f8393af023988ecbaa1a434da5131a1d88040ad54fdb0bd5aad5fd2f7d3c0e

The frozen runtime archive is intended for release with the manuscript/preprint.

## Verification

Run:

    ./scripts/check_release.sh
