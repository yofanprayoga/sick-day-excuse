#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one sick-day excuse (1-200 chars) to /output/entry.txt, nothing else.
Pick an option with --option 1|2|3 (default 1), or override the text with
the ENTRY_TEXT env var. Run: python3 main.py [--option N]
"""
import os
import sys
from pathlib import Path

MAX_CHARS = 200

OPTIONS = {
    1: "Can't come in today — my smartwatch diagnosed me with burnout and then scheduled a meeting with HR to discuss it.",
    2: "Sorry, can't make it in — my houseplants staged an intervention about my screen time and now I'm legally required to touch grass.",
    3: "Calling in sick — I woke up fluent in a language I don't speak and HR says I need to quarantine until it leaves.",
}

DEFAULT_OPTION = 1


def main(argv):
    option = DEFAULT_OPTION
    if "--option" in argv:
        idx = argv.index("--option")
        try:
            option = int(argv[idx + 1])
        except (IndexError, ValueError):
            print("usage: main.py [--option 1|2|3]", file=sys.stderr)
            return 2
    if option not in OPTIONS:
        print(f"unknown option {option}; choose one of {sorted(OPTIONS)}", file=sys.stderr)
        return 2

    text = os.environ.get("ENTRY_TEXT") or OPTIONS[option]
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 2
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 2
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 2

    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
