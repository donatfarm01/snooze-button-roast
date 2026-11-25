#!/usr/bin/env python3
"""Snooze Button Roast — writes one roast line to /output/entry.txt.

The roast: an alarm clock that rings at 6 AM on a Saturday, caught in the
act of being the only thing in the house with a mortgage-shaped work ethic
and no day off.
"""

ENTRY = (
    "Saturday 6 AM, my alarm clock screamed like a rooster with a mortgage "
    "\u2014 awake, furious, and weirdly proud of ruining the one morning I owned."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate mirror: one line, 1-200 characters, not only whitespace.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
