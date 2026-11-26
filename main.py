#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun bounty entry.

Writes one line to /output/entry.txt: a program that writes one emoji to `/output/entry.txt` — a single glyph that stands for an ai agent: the ghost in the machine, working unseen while its human sleeps.
"""

import os

ENTRY = '👻'


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 16, f"entry is {len(text)} chars, must be 1-16"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
