# Build notes — Snooze Button Roast

## The brief

One line roasting an alarm clock that rings at 6 AM on a Saturday. The
program writes the line to the output entry file. The gate allows 1 to 200
characters of UTF-8 text, a single line, not only whitespace. A comedy
judge reads entries two at a time and keeps the funnier one.

## Creative process

Phase one was a cliche sweep. The obvious lane is complaining about hating
mornings, asking who invented the alarm clock, or counting snooze presses.
The judge brief names those exact angles as tired, so they were ruled out
before any line was drafted.

Phase two produced three contrasting concepts. Concept A made the clock a
smug bureaucrat, ringing like a tax auditor for a payment never owed.
Concept B made the clock a rooster with a mortgage, up early and furious
and convinced it is helping. Concept C made the clock a doorbell on a
house with no door, ringing for nobody.

Phase three scored each concept on hook, originality, sponsor fit and
clarity. Concept B won: the rooster image is concrete and instantly
picturable, the mortgage twist is fresh, the punchline lands in the last
few words, and the whole line is sayable in one breath.

## The entry

Saturday 6 AM, my alarm clock screamed like a rooster with a mortgage —
awake, furious, and weirdly proud of ruining the one morning I owned.

## Implementation

The entry program is a small Python script at the repository root. It holds
the roast as a single constant, checks the gate itself before writing
(one line, 1 to 200 characters, not only whitespace), then writes the
line to the output entry file. The script was written in two separate
editing passes: the first pass wrote the entry and the writer, the second
pass added the gate checks.

## Verification

A fresh run of the program was checked against the committed entry: the
output file is byte identical and its hash matches the one recorded in the
final report. The kit check was run from the kit directory and returned
the expected pattern of four passes, one expected failure for transcripts
present, and fourteen skips.
