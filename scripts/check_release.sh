#!/usr/bin/env bash
set -euo pipefail

pytest
ruff check src tests
policy-td-inspect-results --results-dir results/frozen_release/internal_plus_real_external
./scripts/audit_repo.sh

echo
echo "Release check passed."
