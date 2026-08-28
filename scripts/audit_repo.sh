#!/usr/bin/env bash
set -euo pipefail

echo "Repository audit"
echo "================"

echo
echo "Tracked generated/runtime files:"
if git ls-files | grep -E 'egg-info|__pycache__|\.pyc$|\.pid$|\.out$|nohup\.out$'; then
  echo "FAIL: generated/runtime files are tracked."
  exit 1
else
  echo "OK: no tracked generated/runtime files."
fi

echo
echo "Tracked archives/checkpoints:"
if git ls-files | grep -E '\.(tar\.gz|zip|pt|pth|safetensors|bin)$'; then
  echo "FAIL: archive/checkpoint files are tracked in git."
  exit 1
else
  echo "OK: no tracked archives/checkpoints."
fi

echo
echo "Secret-like tracked filenames:"
if git ls-files | grep -Ei '(^|/)(\.env($|\.)|.*credential.*|.*secret.*|.*token.*|.*private[_-]?key.*)'; then
  echo "FAIL: secret-like tracked filename found."
  exit 1
else
  echo "OK: no secret-like tracked filenames."
fi

echo
echo "Machine-local path scan:"
if git grep -n -I -E '/home/[^/]+/|[A-Za-z]:\\Users\\' -- README.md docs data results src tests pyproject.toml CITATION.cff 2>/dev/null; then
  echo "FAIL: machine-local absolute path found in public artifacts."
  exit 1
else
  echo "OK: no machine-local absolute paths in public artifacts."
fi

echo
echo "Legacy public-name scan:"
if git grep -n -I -E 'qwen-SaliGov|SaliGov-TD|SaliGov TD|SaliGov_TD|SALIGOV_TD_PAPER1' -- README.md docs data results src tests pyproject.toml CITATION.cff 2>/dev/null; then
  echo "FAIL: legacy public-facing project naming found."
  exit 1
else
  echo "OK: no legacy project naming in the public artifact."
fi

echo
echo "Repository audit passed."
