#!/usr/bin/env bash
set -euo pipefail

echo "Repository audit"
echo "================"

echo
echo "Git status:"
git status --short

echo
echo "Tracked generated/runtime files:"
if git ls-files | grep -E 'egg-info|__pycache__|\.pyc$|\.pid$|\.out$|nohup\.out$'; then
  echo "FAIL: generated/runtime files are tracked."
  exit 1
else
  echo "OK: no tracked generated/runtime files."
fi

echo
echo "Tracked archive/checkpoint files:"
if git ls-files | grep -E '\.(tar\.gz|zip|pt|pth|safetensors|bin)$'; then
  echo "FAIL: large archive/checkpoint files are tracked."
  exit 1
else
  echo "OK: no tracked archives/checkpoints."
fi

echo
echo "Tracked legacy/prototype residue:"
if git ls-files | grep -Ei 'godmode|foolproof|backup|bak|patch_|before_|nohup|pid'; then
  echo "FAIL: legacy/prototype residue found in tracked files."
  exit 1
else
  echo "OK: no tracked legacy/prototype residue."
fi

echo
echo "Public-facing old project-name scan:"
if git grep -n -I -E 'qwen-SaliGov|SaliGov-TD|SaliGov TD|SaliGov_TD' -- README.md docs src tests pyproject.toml CITATION.cff 2>/dev/null; then
  echo "FAIL: old public-facing project naming found."
  exit 1
else
  echo "OK: no old public-facing project naming in README/docs/src/tests/package metadata."
fi

echo
echo "Allowed provenance archive-name scan:"
git grep -n -I -E 'SALIGOV_TD_PAPER1_FROZEN_FINAL|SaliGov' -- README.md docs results data pyproject.toml CITATION.cff 2>/dev/null || true
echo "Note: internal provenance archive names are allowed only in artifact-access/release notes/checksum contexts."

echo
echo "Commit author check:"
git log --pretty=format:'%h %an <%ae> %s' -10
echo

if git log --pretty=format:'%an <%ae>' | grep -v 'Surya Teja Avvaru <avvarusuryateja@gmail.com>' >/dev/null; then
  echo "FAIL: non-Surya author found in history."
  exit 1
else
  echo "OK: commit authors are clean."
fi

echo
echo "Remote check:"
git remote -v

echo
echo "Repository audit passed."
