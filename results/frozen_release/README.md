# Frozen release results

This directory contains curated summary tables and manifests for the frozen Policy-TD release.

Large raw runtime artifacts are not stored directly in git. The full frozen archive is:

`SALIGOV_TD_PAPER1_FROZEN_FINAL_20260615_082040.tar.gz`

SHA-256:

`5a1226c2b995fa1147f90ba983e917c43755bfb84096dd31d4f5af64e4298c8c`

## Contents

- `internal_plus_real_external/`: tables combining internal global heldout and real public external evaluation.
- `external_style/`: tables for the external-style stress benchmark.
- `INTERNAL_MANIFEST.json`: manifest for the internal evaluation run.
- `REAL_EXTERNAL_MANIFEST.json`: manifest for the real public external evaluation run.
- `SHA256SUMS.txt`: checksum for the frozen archive.

## Primary tables

The main paper-level table pack is `internal_plus_real_external/`.

It contains:

- `TABLE_1_runtime_seed_condition.csv`
- `TABLE_2_runtime_pooled_condition.csv`
- `TABLE_3_runtime_mean_std_over_seeds.csv`
- `TABLE_4_runtime_by_student_pooled.csv`
- `TABLE_5_runtime_by_family_pooled.csv`
- `TABLE_6_label_transfer_by_seed_student.csv`
- `TABLE_7_label_transfer_pooled_student.csv`
