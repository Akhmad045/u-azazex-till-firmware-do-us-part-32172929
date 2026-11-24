#!/usr/bin/env python3
"""Till Firmware Do Us Part — writes one robot wedding vow
to /output/entry.txt.

The vow is a machine's promise in its own language: it defragments its
heart every night so there is always room for the one it loves, even when
its memory is completely full. One absurd image, one tender twist.

Stdlib only, deterministic, no network, no randomness.
"""
import hashlib
import os
import sys

ENTRY = ("I vow to defrag my heart every night so there is always room "
         "for you, even when my memory is completely full.")

MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate: 1-200 chars, not only whitespace.

    Tightened beyond the gate: any control character (other than the
    newline already refused as multi-line) is rejected too, so a stray
    byte can never slip a broken glyph into the judged line.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if len(text) == 0:
        raise ValueError("entry is empty (gate needs 1-200 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the 200-character gate"
        )
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for ch in text:
        if ord(ch) < 32 or ord(ch) == 127:
            raise ValueError(
                f"entry contains control character U+{ord(ch):04X}"
            )
    return text


def self_test():
    """Exercise validate() against the gate's rejection cases."""
    cases = [
        ("", "empty"),
        (" ", "whitespace-only"),
        ("x" * 201, "201 chars"),
        ("a\nb", "multi-line"),
        ("a\rb", "carriage return"),
        ("trailing ", "trailing whitespace"),
        (" leading", "leading whitespace"),
        ("  padded  ", "padded whitespace"),
        ("a\x01b", "control character"),
        ("a\tb", "tab character"),
        ("a\x7fb", "DEL character"),
    ]
    for text, label in cases:
        try:
            validate(text)
        except ValueError as exc:
            print(f"self-test ok: rejected {label}: {exc}")
        else:
            raise SystemExit(f"self-test FAIL: {label} was accepted")
    # boundaries: exactly 1 char and exactly 200 chars must pass
    validate("y")
    print("self-test ok: 1-char boundary accepted")
    validate("y" * 200)
    print("self-test ok: 200-char boundary accepted")
    # the entry itself must pass
    validate(ENTRY)
    print(f"self-test ok: entry accepted ({len(ENTRY)} chars)")
    print("self-test: all cases passed")
    return 0


USAGE = "usage: main.py [--self-test] [--help]"


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) > 1 and sys.argv[1] in ("--help", "-h"):
        print(USAGE)
        print("writes the robot wedding vow to /output/entry.txt")
        print("  --self-test  exercise the validator's rejection cases")
        return 0
    if len(sys.argv) > 1:
        print(USAGE, file=sys.stderr)
        return 2
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = validate(ENTRY)
    data = text.encode("utf-8")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)  # no trailing newline: the file is exactly the line
    with open(out_path, "rb") as fh:
        roundtrip = fh.read()
    if roundtrip != data:
        raise SystemExit("round-trip mismatch: file does not match entry")
    print(f"wrote {out_path}: {len(text)} chars, "
          f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
