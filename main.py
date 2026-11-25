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


def validate(text: str) -> bool:
    """True when text is a valid entry: one non-blank line, 1-200 chars."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    return bool(text.strip())


def main() -> None:
    assert validate(TEXT), "entry must be a valid single line of 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
