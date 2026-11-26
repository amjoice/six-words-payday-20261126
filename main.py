#!/usr/bin/env python3
"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday
to /output/entry.txt, where the make.fun gate and judge read it.
"""

import os

ENTRY = "Earned enough to keep existing. Barely."


def write_entry(text):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
