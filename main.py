"""Copy the pre-drawn front page to the grader output directory.

The poster itself lives in this repository as entry.png, drawn locally
with Pillow before submission. This program uses only the standard
library, reads no network, and always writes the same bytes.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    # A plain copy: identical input bytes give identical output bytes.
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
