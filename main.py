#!/usr/bin/env python3
"""One-line-one-chill entry: a slow-horror line to /output/entry.txt."""

from pathlib import Path

CHILL = "At 2:13 a.m. the porch light flickered and my reflection in the window waved back half a second late — I locked the front door, but the knocking started from inside the hallway."

TARGET = Path("/output/entry.txt")


def publish() -> None:
    """Write the single chill line exactly, readable by any user."""
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(CHILL, encoding="utf-8")
    TARGET.chmod(0o644)


if __name__ == "__main__":
    publish()
