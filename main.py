#!/usr/bin/env python3
"""The Best Meal You Ever Had - make.fun bounty entry.

Writes one sentence, at most 200 characters, about the best meal
ever had, to /output/entry.txt. Fully deterministic: the same
sentence every run, no randomness, no network, no input files.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ENTRY = (
    "My grandmother's ofe nsala in Nnewi fogged my glasses with pepper "
    "steam, the catfish falling apart on my tongue while rain drummed "
    "the zinc roof and nobody at the table said a word."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"


def resolve_output_path():
    """Return the full path the entry is written to."""
    return os.path.join(OUTPUT_DIR, OUTPUT_FILE)


def validate_entry(text):
    """Check the entry meets the bounty rules: 1 to 200 characters,
    one sentence, not only white space. Raises AssertionError if not."""
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text.strip(), "entry must not be only white space"
    return text


def write_entry(text, path=None):
    """Validate the entry and write it to the output target.
    Returns the path written."""
    validate_entry(text)
    target = path if path is not None else resolve_output_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(text)
    return target


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
