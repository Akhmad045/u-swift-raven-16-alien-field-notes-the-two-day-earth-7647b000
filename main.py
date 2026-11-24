#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line — an alien tourist's review of planet Earth —
to /output/entry.txt. The gate the entry must clear: plain UTF-8 text,
1 to 200 characters, exactly one non-blank line, no control characters,
and no whitespace at either end.
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


class EntryError(ValueError):
    """The review fails one of the competition's gate rules."""


def validate(line):
    """Raise EntryError naming the first gate rule `line` breaks."""
    if not line.strip():
        raise EntryError("entry is blank")
    if len(line) > MAX_CHARS:
        raise EntryError(f"entry is {len(line)} characters, over the 200 limit")
    if line != line.strip():
        raise EntryError("entry has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise EntryError("entry must be a single line")
    for ch in line:
        if ord(ch) < 0x20:
            raise EntryError(f"entry holds a control character U+{ord(ch):04X}")


def write_entry(line, path):
    """Write `line` plus a trailing newline, then prove the bytes match."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    payload = (line + "\n").encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    with open(path, "rb") as handle:
        stored = handle.read()
    if stored != payload:
        raise EntryError("written file does not match the entry bytes")
    if stored.decode("utf-8").rstrip("\n") != line:
        raise EntryError("written file does not decode back to the entry")
    return len(payload)


def main():
    try:
        validate(REVIEW)
        size = write_entry(REVIEW, OUTPUT_PATH)
    except EntryError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    print(
        f"wrote {len(REVIEW)} characters "
        f"({size} bytes) to {OUTPUT_PATH}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
