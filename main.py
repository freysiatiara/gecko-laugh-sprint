#!/usr/bin/env python3
"""One-Line Laugh Sprint — entry program.

Writes exactly one original funny line to the entry output file.
Deterministic: the output bytes are identical on every run.
"""
import os

LINE = "I bought a planner to organize my life; it is now the most organized list of things I didn't do."


def output_path():
    full_path = os.environ.get("ENTRY_OUTPUT")
    if full_path:
        return full_path
    out_dir = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
