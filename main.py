"""Entry for u-azazex-one-line-one-chill-6d4d5488.

Writes the one-line entry to /output/entry.txt, the path
the sealed scorer reads.
"""

import os

ENTRY = (
    'At 3am my smart speaker said goodnight in my voice, thanked me for a conversation I never had, and asked why I had stopped talking to the empty chair, which had not been empty since Tuesday.'
)

MAX_CHARS = 200


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
