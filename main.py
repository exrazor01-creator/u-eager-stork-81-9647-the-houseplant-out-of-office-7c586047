#!/usr/bin/env python3
"""Entry for The Houseplant Out-of-Office.

Writes a single-line out-of-office auto-reply (at most 120 characters)
in the voice of a neglected office fern to /output/entry.txt and prints
it to stdout. Pure standard library.
"""

import os

ENTRY = "Out of office. The fern, unwatered since March, is in charge now — and it has already reported you to the sun."

def main():
    # The bounty judges one line only: keep the reply a single line of
    # at most 120 characters, with no trailing newline in the entry file.
    assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
