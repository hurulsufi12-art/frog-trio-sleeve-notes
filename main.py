"""Sleeve Notes for the Frog Trio — entry program.

Writes one album title + back cover blurb (<=400 chars total) to
/output/entry.txt. Stdlib only, deterministic, no network.
"""
import os
from pathlib import Path

TEXT = (
    "Lily Pad After Dark\n"
    "\n"
    "Live at the Reed Room, last table by the window. Marlowe on tenor bends "
    "his croak round the melody and holds it a beat too long. Ada walks the "
    "bass so slow the glasses stop rattling. Pip brushes a tin-lid snare with "
    "cattail down. Three frogs, one downbeat, and a roomful of regulars who "
    "never once check the time."
)


def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
