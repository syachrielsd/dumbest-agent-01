"""Dumbest-thing-my-agent-did entry.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only. No network, no rendering, no dependencies.
"""

import os

LINE = "My agent dug through my Gmail for a contest leaderboard, then got told off for snooping through my email."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {path}: {len(LINE)} chars, {len(LINE.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
