"""The Comment Above the Code — entry program.

Writes one funny, painfully honest comment line, as if left by a developer
above fragile production code, to /output/entry.txt.
"""

import os

LINE = "// this was a temporary fix in 2019. it now has a retirement plan"


def main() -> None:
    # Self-check against the competition gate: 1-200 chars, UTF-8, not blank.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate needs 1-200"
    assert text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
