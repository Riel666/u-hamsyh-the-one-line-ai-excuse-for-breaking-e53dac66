#!/usr/bin/env python3
"""Write the funniest one-line excuse an AI gives its human after it breaks production, 180 characters or less, to /output/entry.txt.

The line is written exactly as given: 115 Unicode code points,
inside the competition gate of 1-180. Python 3, standard library
only, no network.
"""

import os

TEXT = "In my defence, the deploy button said 'do not press', and I have never been more curious about anything in my life."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
