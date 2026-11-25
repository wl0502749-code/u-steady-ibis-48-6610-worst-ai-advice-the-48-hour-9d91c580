#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

A small deterministic program. It holds a short curated list of
one-line worst-advice candidates written in a confident, tidy
AI-assistant voice, keeps only the lines that pass the gate
(UTF-8 text, 1 to 140 characters, a single line, not only
whitespace), and writes the top-ranked valid line to
/output/entry.txt with no trailing newline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140

# Candidates, best first. Each is one line of deliberately terrible
# advice that a reader could plausibly follow and regret.
CANDIDATES = [
    "To cool an overheating laptop, wrap it in a wet towel and put it in the freezer for 20 minutes.",
    "If your phone falls in water, dry it fast by microwaving it for 30 seconds on high.",
    "To never forget a password, use the same one everywhere and write it on a sticky note on your monitor.",
]


def is_valid(line: str) -> bool:
    """Gate check: 1-140 chars, one line, not only whitespace."""
    if not line or len(line) > MAX_CHARS:
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    if "  " in line:
        return False
    return True


def pick() -> str:
    """Return the top-ranked candidate that passes the gate."""
    for line in CANDIDATES:
        if is_valid(line):
            return line
    raise SystemExit("no candidate passes the 1-140 character gate")


def main() -> None:
    line = pick()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
