"""TODO Scan — Scan a folder for TODO and FIXME comments and write a list with paths."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='todo_scan',
        description='Scan a folder for TODO and FIXME comments and write a list with paths.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('TODO Scan')
    print('A leftover-comment report before a release.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
