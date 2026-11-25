#!/usr/bin/env python3
"""One-Star Review of Something Essential.

A deadpan one-star review of the sun, the everyday essential nobody can
switch off. The program prints the review and writes it, on its own line,
to /output/entry.txt for the make.fun judge.
"""

import os

REVIEW = (
    "One star. The sun turns up uninvited every morning, stares straight "
    "into my eyes, and has never once apologised. "
    "Management refuses to dim it."
)

LIMIT = 160

# The harness reads exactly this file, so the path lives in one place.
OUTPUT_PATH = "/output/entry.txt"

# Why the sun: it is the one essential with a genuine grievance (too bright,
# too early, no customer service) and the deadpan turn lands on the last
# clause, where the complaint meets a management that cannot help.


def check(line):
    """Keep the review inside the bounty gate: one line, 1-160 chars."""
    text = line.strip()
    if not text:
        raise ValueError("review is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if len(text) > LIMIT:
        raise ValueError(f"review is {len(text)} chars, over the {LIMIT} limit")
    return text


def main():
    text = check(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
