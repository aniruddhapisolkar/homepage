#!/usr/bin/env python3
"""Fetch the pinned, unmasked Obel Mono web fonts and their license."""
from io import BytesIO
from pathlib import Path, PurePosixPath
from urllib.request import urlopen
from zipfile import ZipFile

VERSION = "1.004"
URL = f"https://typographic.systems/download/ObelMono-{VERSION}.zip"
DEST = Path(__file__).resolve().parent.parent / "static" / "fonts" / "obel-mono"


def fetch():
    expected = ["ObelMono-Roman.woff2", "ObelMono-Italic.woff2", "OFL.txt"]
    if all((DEST / name).is_file() for name in expected):
        return
    with urlopen(URL, timeout=60) as response:
        data = response.read()
    with ZipFile(BytesIO(data)) as archive:
        members = [name for name in archive.namelist() if not name.endswith("/")]
        web_fonts = [
            name for name in members
            if name.lower().endswith(".woff2") and "masked" not in name.lower()
        ]
        italic = [name for name in web_fonts if "italic" in PurePosixPath(name).name.lower()]
        roman = [name for name in web_fonts if name not in italic]
        licenses = [name for name in members if PurePosixPath(name).name.lower() == "ofl.txt"]
        if len(roman) != 1 or len(italic) != 1 or not licenses:
            raise RuntimeError(f"Unexpected Obel Mono {VERSION} archive layout: {web_fonts}")
        DEST.mkdir(parents=True, exist_ok=True)
        for filename, member in (
            ("ObelMono-Roman.woff2", roman[0]),
            ("ObelMono-Italic.woff2", italic[0]),
            ("OFL.txt", licenses[0]),
        ):
            (DEST / filename).write_bytes(archive.read(member))
        authors = [name for name in members if PurePosixPath(name).name.lower() == "authors.txt"]
        if authors:
            (DEST / "AUTHORS.txt").write_bytes(archive.read(authors[0]))
    print(f"Obel Mono {VERSION}: self-hosted Roman and Italic fonts ready.")


if __name__ == "__main__":
    fetch()
