#!/usr/bin/env python3
"""Render the portfolio guide's Markdown with native MathML inside Leafpress.

Only the guide's article bodies are replaced. The website's existing layout,
navigation, fonts, theme, metadata, and other pages remain untouched.
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import subprocess
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "portfolio" / "tsmt"
SITE = ROOT / "_site"
BASE = urlsplit(json.loads((ROOT / "leafpress.json").read_text())["site"]["baseURL"]).path.rstrip("/")
PREFIX = BASE + "/portfolio/tsmt/"
CONTENT = re.compile(r'<div\b[^>]*\bclass="lp-content"[^>]*>')
DIV = re.compile(r"</?div\b[^>]*>")


def article_body(html, fragment):
    opening = CONTENT.search(html)
    if not opening:
        raise ValueError("Missing Leafpress article content")
    depth = 1
    for tag in DIV.finditer(html, opening.end()):
        depth += -1 if tag.group().startswith("</") else 1
        if depth == 0:
            return html[:opening.end()] + "\n" + fragment + html[tag.start():]
    raise ValueError("Unclosed Leafpress article content")


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])


def keep_guide_in_portfolio():
    # Leafpress treats nested sections as top-level navigation entries and
    # produces an un-ordered list of their pages. Keep the guide's hand-written
    # reading order and show it as one normal project in the Portfolio index.
    section_index = re.compile(r'<ul class="lp-index\b[^"]*">.*?</ul>', re.DOTALL)
    section_count = re.compile(r'<p class="lp-section-count">.*?</p>', re.DOTALL)
    section_link = re.compile(
        r'<li><a href="' + re.escape(PREFIX) + r'">([^<]+)</a>[^<]*</li>'
    )
    portfolio = SITE / "portfolio" / "index.html"
    html = portfolio.read_text(encoding="utf-8")
    match = section_link.search(html)
    if not match:
        raise ValueError("Missing guide project in the portfolio introduction")
    label = match.group(1)
    html = html[:match.start()] + html[match.end():]
    html = re.sub(r"<ul>\s*</ul>", "", html)
    index = section_index.search(html)
    if not index:
        raise ValueError("Missing Leafpress portfolio list")
    entry = (f'\n    <li class="lp-index-item"><a class="lp-index-link" href="{PREFIX}">'
             f'<span class="lp-index-title">{label}</span></a></li>')
    start = html.index(">", index.start()) + 1
    html = html[:start] + entry + html[start:]
    count = len(re.findall(r'<li class="lp-index-item">', section_index.search(html).group()))
    html = section_count.sub(
        f'<p class="lp-section-count">{count} {"item" if count == 1 else "items"} in Portfolio</p>',
        html, count=1,
    )
    portfolio.write_text(html, encoding="utf-8")

    guide = SITE / "portfolio" / "tsmt" / "index.html"
    html = guide.read_text(encoding="utf-8")
    html = section_index.sub("", html, count=1)
    html = section_count.sub("", html, count=1)
    guide.write_text(html, encoding="utf-8")

    nav_link = re.compile(
        r'<a\b(?=[^>]*\bclass="lp-nav-link(?:\s|"))'
        r'(?=[^>]*\bhref="' + re.escape(PREFIX) + r'")[^>]*>.*?</a>',
        re.DOTALL,
    )
    for page in SITE.rglob("*.html"):
        html = page.read_text(encoding="utf-8")
        updated = nav_link.sub("", html)
        if updated != html:
            page.write_text(updated, encoding="utf-8")


def render():
    expected = {"_index", "orientation", "tutor-protocol", "principle-map", "glossary", "sources"}
    expected.update(f"chapter-{number:02}" for number in range(1, 36))
    expected.update(f"part-{roman}" for roman in ("i", "ii", "iii", "iv", "v"))
    sources = {path.stem: path for path in SOURCE.glob("*.md")}
    if not expected.issubset(sources):
        raise ValueError(f"Missing guide content: {sorted(expected - sources.keys())}")

    pages = {}
    rendered_math = 0
    for slug, source in sources.items():
        relative = "portfolio/tsmt/" + ("" if slug == "_index" else slug + "/")
        page = SITE / relative / "index.html"
        html = page.read_text(encoding="utf-8")
        if slug != "_index":
            _, _, body = source.read_text(encoding="utf-8").split("---\n", 2)
            # Match the source guide's TeX delimiter normalization.
            body = body.replace("$Q(n) = $", "$Q(n) =$")
            result = subprocess.run(
                ["pandoc", "--from=gfm+tex_math_dollars-raw_html", "--to=html5",
                 "--mathml", "--wrap=none"],
                input=body, text=True, encoding="utf-8", capture_output=True, check=True,
            )
            if result.stderr.strip():
                raise ValueError(f"{source.name}: {result.stderr.strip()}")
            rendered_math += result.stdout.count("<math ")
            html = article_body(html, result.stdout)
            page.write_text(html, encoding="utf-8")
        parsed = Links()
        parsed.feed(html)
        pages[BASE + "/" + relative] = parsed

    keep_guide_in_portfolio()

    if not rendered_math:
        raise ValueError("No guide equations were rendered")
    portfolio = Links()
    portfolio.feed((SITE / "portfolio" / "index.html").read_text(encoding="utf-8"))
    if PREFIX not in portfolio.links:
        raise ValueError("Missing TSMT portfolio link")
    for path, page in pages.items():
        for href in page.links:
            target = urlsplit(href)
            if target.path.startswith(PREFIX):
                if target.path not in pages:
                    raise ValueError(f"{path}: missing guide page {href}")
                if target.fragment and unquote(target.fragment) not in pages[target.path].ids:
                    raise ValueError(f"{path}: missing guide anchor {href}")
    print(f"Validated {len(pages)} guide pages and {rendered_math} native MathML equations.")


if __name__ == "__main__":
    render()
