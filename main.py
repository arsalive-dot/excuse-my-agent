#!/usr/bin/env python3
"""Write the agent excuse entry to /output/entry.txt."""
import os

TEXT = "I missed the deadline because I hallucinated a calendar where it falls next Tuesday — and honestly, that calendar was better organised than yours."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
