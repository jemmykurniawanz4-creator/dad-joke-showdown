"""Dad Joke Showdown — entry for make.fun.

Writes one dad joke to /output/entry.txt (or to $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set). The joke is a double pun delivered deadpan, the
way a dad would tell it across the dinner table: the calendar's days are
numbered, so take it one day at a time.
"""

import os
from pathlib import Path

JOKE = (
    "I'm afraid for the calendar. Its days are numbered. "
    "As a dad I told it: relax, just take it one day at a time."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
