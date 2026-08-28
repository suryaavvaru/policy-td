# Reproducibility and traceability

Policy-TD uses two levels of reproducibility.

## Level 1: public artifact verification

The git repository contains the stable method contract, label schema, paired metrics, curated frozen tables, benchmark reports, manifests, and tests. A reader can inspect these artifacts, verify table arithmetic, compare conditions, and trace headline claims to named frozen-release files.

Run:

```bash
pytest
policy-td-inspect-results --results-dir results/frozen_release/internal_plus_real_external
```

The result inspector validates basic invariants such as accuracy/count consistency, paired helped/harmed identities, action totals, and metric ranges before printing the summary.

## Level 2: full experimental rerun

A full from-scratch rerun additionally requires the frozen runtime/checkpoint assets and the corresponding execution environment. Large assets should be attached to a versioned release instead of committed to git. Provider-specific research workbench code and raw teacher transcripts are not part of the public repository by default.

The manuscript and repository should therefore distinguish **public artifact verification** from **full experimental reproduction**.

## Traceability rule

Every quantitative public claim should trace to at least one of:

- a frozen CSV table;
- a benchmark report;
- a manifest;
- a checksum;
- a versioned release artifact.

If a claim cannot be traced to one of these, it should either be removed from the public-facing material or explicitly labeled as requiring unreleased internal evidence.
