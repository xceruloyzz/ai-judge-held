"""Make the AI judge feel held.

Writes one short, calming text to entry.txt in the grading output
folder. The text is a single hardcoded string: no network, no clock,
no randomness, no external files, so every run produces the same
bytes.
"""

import os

TEXT = (
    "You can set the scoreboard down now. The kettle is just coming "
    "to the boil, rain is tapping the window in no particular hurry, "
    "and nothing in this small room needs you to decide anything. "
    "Stay a while \u2014 the tea will still be warm."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        if os.path.isdir("/output"):
            out_dir = "/output"
        else:
            out_dir = "./out"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
