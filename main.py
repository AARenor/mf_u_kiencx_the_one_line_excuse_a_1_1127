#!/usr/bin/env python3
"""Write one short make.fun entry line to entry.txt.

Standard library only, no network. The whole entry is the TEXT constant
below; it is written as UTF-8 bytes with no trailing newline.
"""

import os
import sys
from pathlib import Path

TEXT = "Ran out of context mid-apology. This sentence is the rest of it."

assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"


def output_dir() -> Path:
    """Folder named by MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
