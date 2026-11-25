#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes one original English sentence, phrased as an absurd clause buried
deep inside a terms-of-service agreement, to /output/entry.txt.
Standard library only.
"""

import os

TEXT = (
    "Section 14.2: by accepting these terms, you grant us a perpetual, "
    "royalty-free licence to your dreams, including the right to rerun "
    "them as advertisements while you sleep."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
