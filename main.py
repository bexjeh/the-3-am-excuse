#!/usr/bin/env python3
"""Write the entry: the excuse a hardware wallet gives for refusing
to sign a transaction at 3 AM.

Stdlib only, deterministic, no network. Reads MAKEFUN_OUTPUT_DIR
(fallback ".") and writes exactly one line to <that dir>/entry.txt,
with a trailing newline.
"""

import os

LINE = (
    "My seed phrase is asleep — all 24 words, snoring. "
    "I don't wake it for a 3 AM transaction."
)


def main() -> None:
    # Gate: the entry must be one line of 1-200 characters, as the bounty requires.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
