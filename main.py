#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line — an alien tourist's review of planet Earth —
to /output/entry.txt. The line is held to the competition gate: plain
UTF-8 text, 1 to 200 characters, a single non-blank line with no control
characters and no leading or trailing whitespace.
"""

import os
import sys

REVIEW = (
    "Earth is a lovely open-air zoo where the animals built Wi-Fi and "
    "queue every morning for bean water. The sunsets are free, somehow. "
    "4/5 \u2014 would orbit again."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check(line):
    """Return a list of gate failures for `line` (empty means it passes)."""
    problems = []
    if not 1 <= len(line) <= MAX_CHARS:
        problems.append(f"length {len(line)} is outside 1-{MAX_CHARS} characters")
    if line != line.strip():
        problems.append("leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        problems.append("must be a single line")
    if not line.strip():
        problems.append("blank or whitespace only")
    if any(ord(ch) < 0x20 for ch in line):
        problems.append("contains control characters")
    return problems


def main():
    problems = check(REVIEW)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW + "\n")

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != REVIEW + "\n":
        print("invalid entry: written file does not round-trip exactly",
              file=sys.stderr)
        return 1

    print(f"wrote {len(REVIEW)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
