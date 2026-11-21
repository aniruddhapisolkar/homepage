#!/usr/bin/env python3
"""Check the published navigation, portfolio hierarchy and disabled graph."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
CONFIG = json.loads((ROOT / "leafpress.json").read_text(encoding="utf-8"))
BASE = urlsplit(CONFIG["site"]["baseURL"]).path.rstrip("/")


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links = []
        self.nav_links = []
        self.index_links = []
        self.elements = set()
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set(attrs.get("class", "").split())
        self.elements.update(classes)
        if attrs.get("id"):
            self.elements.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            href = attrs["href"]
            self.links.append(href)
            if "lp-nav-link" in classes:
                self.nav_links.append(href)
            if "lp-index-link" in classes:
                self.index_links.append(href)


def main():
    expected_nav = {BASE + item["path"] for item in CONFIG["navigation"]["items"]}
    for path in SITE.rglob("*.html"):
        page = Page(path)
        if set(page.nav_links) != expected_nav:
            raise ValueError(f"Unexpected navigation on {path}: {page.nav_links}")
        if {"lp-graph-toggle", "lp-graph-overlay", "lp-graph-panel"} & page.elements:
            raise ValueError(f"Graph UI still present on {path}")

    if (SITE / "graph.json").exists() or list((SITE / "static").glob("graph-*")):
        raise ValueError("Graph artifacts are still published")

    portfolio = Page(SITE / "portfolio" / "index.html")
    for project in ("tsmt", "lle1"):
        href = f"{BASE}/portfolio/{project}/"
        if portfolio.index_links.count(href) != 1 or portfolio.links.count(href) != 1:
            raise ValueError(f"Expected exactly one native Portfolio entry: {href}")
        landing = Page(SITE / "portfolio" / project / "index.html")
        if landing.index_links:
            raise ValueError(f"Unexpected automatic child listing for {project}")

    experiment = Page(SITE / "portfolio" / "lle1" / "index.html")
    for slug in ("methodology", "daily-observations", "weekly-analyses",
                 "monthly-evaluations", "changes", "conclusions"):
        href = f"{BASE}/portfolio/lle1/{slug}/"
        if href not in experiment.links or not (SITE / "portfolio" / "lle1" / slug / "index.html").is_file():
            raise ValueError(f"Missing language learning experiment page: {href}")
    print("Validated portfolio entries, experiment links, site navigation, and graph removal.")


if __name__ == "__main__":
    main()
