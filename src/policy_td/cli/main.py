"""Policy-TD command line interface."""

from __future__ import annotations

import argparse
from pathlib import Path

from policy_td.utils.hashing import sha256_file


def main() -> None:
    parser = argparse.ArgumentParser(prog="policy-td")
    sub = parser.add_subparsers(dest="command", required=True)

    verify = sub.add_parser("sha256", help="Compute SHA-256 for a file.")
    verify.add_argument("path", type=Path)

    args = parser.parse_args()

    if args.command == "sha256":
        print(sha256_file(args.path))


if __name__ == "__main__":
    main()
