#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes a single original one-line roast of the entrant's own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-200 characters).
"""
import os

LINE = "My agent calls every question 'great' before answering it, as if flattery were a substitute for knowing the answer."


def validate_length(line):
    """Gate: the bounty only judges entry.txt of 1-200 UTF-8 characters."""
    if not 1 <= len(line) <= 200:
        raise ValueError("LINE must be 1-200 characters")


def validate_content(line):
    """Gate: the line must be real text, not only whitespace."""
    if not line.strip():
        raise ValueError("LINE must contain non-whitespace text")


def validate_line(line):
    """Fail loudly here rather than silently submitting a line that can
    never be judged."""
    validate_length(line)
    validate_content(line)


def resolve_output_dir():
    """Resolve the output directory from MAKEFUN_OUTPUT_DIR (default
    /output) and create it if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def main():
    validate_line(LINE)
    out_dir = resolve_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
