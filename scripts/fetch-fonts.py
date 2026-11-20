#!/usr/bin/env python3
"""Enable user-supplied Obel Mono web fonts, without network downloads.

Place the Roman/Italic WOFF2s and OFL.txt in static/fonts/obel-mono/.
Run this before leafpress build or serve; absent files keep the built-in
JetBrains Mono fallback usable and CI does not need a third-party font host.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "static" / "fonts" / "obel-mono"
CONFIG = ROOT / "leafpress.json"
FACES = [
    ("ObelMono-Roman.woff2", "normal"),
    ("ObelMono-Italic.woff2", "italic"),
]


def prepare():
    required = [name for name, _ in FACES] + ["OFL.txt"]
    missing = [name for name in required if not (DEST / name).is_file()]
    if missing:
        print("Obel Mono assets not yet supplied; using the bundled JetBrains Mono fallback.")
        return
    for name, _ in FACES:
        with (DEST / name).open("rb") as font:
            if font.read(4) != b"wOF2":
                raise ValueError(f"{name} is not a valid WOFF2 file.")
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    theme = config["theme"]
    for role in ("fontHeading", "fontBody", "fontMono"):
        theme[role] = "Obel Mono"
    theme["fonts"] = [
        {
            "family": "Obel Mono",
            "file": f"static/fonts/obel-mono/{name}",
            "weight": "100 900",
            "style": style,
            "display": "swap",
        }
        for name, style in FACES
    ]
    CONFIG.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    print("Obel Mono Roman and Italic fonts configured.")


if __name__ == "__main__":
    prepare()
