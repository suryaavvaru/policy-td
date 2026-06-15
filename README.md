# Policy-TD

Teacher-distilled intervention policies for runtime control of frozen small language models.

Policy-TD shifts adaptation from model weights to runtime intervention decisions. Instead of fine-tuning a student language model, it trains a compact controller that predicts whether the frozen model should finalize, abstain, repair, roll back, request a grounded continuation, or continue.

## Overview

Frozen small language models often fail not only because they cannot generate the right answer, but because they commit to an answer when the trace is unsupported, incomplete, or internally inconsistent.

Policy-TD treats this as a runtime control problem. The student model remains frozen. A compact controller predicts typed intervention actions around the model at inference time.

## Runtime actions

Policy-TD uses the following action vocabulary:

- `finalize`
- `say_unknown`
- `repair_final`
- `rollback`
- `force_grounded_step`
- `continue`

## Frozen-release results

| Suite | Condition | Base accuracy | Guided accuracy | Delta | Helped | Harmed |
|---|---|---:|---:|---:|---:|---:|
| Internal global heldout | guided_v12_hardened | 31.00% | 47.33% | +16.33 pp | 147 | 0 |
| Internal global heldout | guided_v10_noharm | 31.00% | 47.11% | +16.11 pp | 145 | 0 |
| Real public external | guided_v12_hardened | 18.67% | 19.22% | +0.56 pp | 35 | 15 |
| Real public external | guided_v10_noharm | 18.67% | 19.22% | +0.56 pp | 26 | 6 |

These results show strong targeted gains on the internal global heldout benchmark and smaller, model-dependent gains on real public external benchmarks. Policy-TD is not claimed to be a universal reasoning enhancer or a universal no-harm method.

## Installation

Install the package in editable development mode:

    python -m pip install -e ".[dev]"

## Verification

Run the unit tests, linter, and frozen-result inspection command:

    pytest
    ruff check src tests
    policy-td-inspect-results --results-dir results/frozen_release/internal_plus_real_external

Or run the full release check:

    ./scripts/check_release.sh

## Repository layout

    src/policy_td/
      core/       action vocabulary and constants
      labels/     teacher-label schema and validation
      runtime/    controller decision utilities
      eval/       paired helped/harmed metrics
      data/       JSONL utilities
      cli/        command-line tools

    docs/         method, labeling, metrics, limitations, release, and reproducibility notes
    results/      curated frozen-release tables and manifests
    tests/        unit tests

## Frozen artifact

Large runtime artifacts are not committed directly to git. A frozen artifact archive will be released with the manuscript/preprint:

    Policy-TD_frozen_runtime_archive_v0.1.0.tar.gz
    SHA-256: 92f8393af023988ecbaa1a434da5131a1d88040ad54fdb0bd5aad5fd2f7d3c0e

The archive contains curated frozen result artifacts, manifests, and table-generation provenance. Trained guide checkpoints, if released, will be provided as a separate checkpoint bundle.

## Citation

A formal manuscript citation will be added with the paper release. Software citation metadata is provided in `CITATION.cff`.

## License

MIT License.
