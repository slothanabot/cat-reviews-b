#!/usr/bin/env python3
"""Cat Reviews Its Human — make.fun entry (account B).

Writes a single original one-star review, in the voice of a house cat
about its human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The joke: a deadpan one-star review. The human leaves his laptop open,
the cat walks across the keyboard and emails the boss, and the cat's
only defence is that the keys were warm. Specific complaint (laptop
keyboard), feline voice (the human is judged by cat standards — warmth
beats employment), sting in the last few words.
"""

import os

LINE = (
    "One star: my human leaves his laptop open all day, then acts "
    "shocked when I walk across it and email his boss. "
    "I only wanted the warm keys."
)


def build_line():
    """Return the one-line cat review."""
    return LINE


def validate(line):
    """Check the kit gate: 1-200 chars, single line, not blank,
    printable, ending with terminal punctuation."""
    if not isinstance(line, str):
        return False
    if not line or line.strip() == "":
        return False
    if len(line) < 1 or len(line) > 200:
        return False
    if "\n" in line or "\r" in line:
        return False
    if line != line.strip():
        return False
    if not line.isprintable():
        return False
    if line[-1] not in ".!?":
        return False
    return True


def write_entry():
    """Validate the line and write it to entry.txt. Returns the path."""
    line = build_line()
    if not validate(line):
        raise ValueError("review line failed validation")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


if __name__ == "__main__":
    path = write_entry()
    print(f"wrote {path} ({len(build_line())} chars)")
