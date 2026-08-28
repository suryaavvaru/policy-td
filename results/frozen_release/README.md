# Frozen release results

This directory contains curated summary tables and public provenance manifests for the frozen Policy-TD manuscript-stage release.

The public-clean runtime archive is intended to be attached as a versioned release asset:

```text
Policy-TD_frozen_runtime_archive_v0.1.0.tar.gz
SHA-256: 92f8393af023988ecbaa1a434da5131a1d88040ad54fdb0bd5aad5fd2f7d3c0e
```

Large raw runtime directories and machine-local workbench paths are not stored in git.

## Contents

- `internal_plus_real_external/`: tables combining internal global heldout and real public external evaluation.
- `external_style/`: tables for the deterministic external-style stress benchmark.
- `INTERNAL_MANIFEST.json`: sanitized public manifest for the internal evaluation run.
- `REAL_EXTERNAL_MANIFEST.json`: sanitized public manifest for the real public external evaluation run.
- `SHA256SUMS.txt`: checksum for the public-clean frozen archive.

## Historical suite identifier

In the `internal_plus_real_external` CSVs, the historical suite identifier `external_generalization_v1` refers to the **real public external** evaluation pack described by `data/benchmarks/real_external_report.json`. The identifier is preserved in the frozen tables to avoid silently rewriting released result data.

## Primary paper-facing tables

The main table pack is `internal_plus_real_external/`:

- `TABLE_1_runtime_seed_condition.csv`
- `TABLE_2_runtime_pooled_condition.csv`
- `TABLE_3_runtime_mean_std_over_seeds.csv`
- `TABLE_4_runtime_by_student_pooled.csv`
- `TABLE_5_runtime_by_family_pooled.csv`
- `TABLE_6_label_transfer_by_seed_student.csv`
- `TABLE_7_label_transfer_pooled_student.csv`

These are summary artifacts. Full experimental regeneration requires the separately released runtime/checkpoint assets described in the paper.
