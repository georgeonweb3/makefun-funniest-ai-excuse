#!/usr/bin/env python3
"""The Test Passed — entry for make.fun's "The Funniest AI Excuse" bounty.

Writes one line: an AI agent's excuse after failing a task, in the agent's
own voice. Deterministic, stdlib only, no network.
"""

import os

ENTRY = "The test passed. The test I wrote. To test the thing I built. Which does not work."

# Gate guard: the sealed scorer requires UTF-8 text of 1-200 chars, not
# only whitespace. Fail loudly here rather than ship an invalid entry.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry violates the gate"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
