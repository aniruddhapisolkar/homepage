#!/usr/bin/env python3
"""Customize generated Leafpress pages and load the root homepage style.

The RSS feeds remain available. Keeping the original navigation class retains
Leafpress's desktop and mobile styling.

GitHub mark: Primer Octicons (MIT), see static/licenses/octicons-LICENSE.txt.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "_site"
MARKUP = '''<a href="https://github.com/aniruddhapisolkar" class="lp-rss-link lp-github-link" aria-label="GitHub profile" title="GitHub profile" target="_blank" rel="noopener noreferrer">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true" focusable="false"><path d="M6.766 11.328c-2.063-.25-3.516-1.734-3.516-3.656 0-.781.281-1.625.75-2.188-.203-.515-.172-1.609.063-2.062.625-.078 1.468.25 1.968.703.594-.187 1.219-.281 1.985-.281.765 0 1.39.094 1.953.265.484-.437 1.344-.765 1.969-.687.218.422.25 1.515.046 2.047.5.593.766 1.39.766 2.203 0 1.922-1.453 3.375-3.547 3.64.531.344.89 1.094.89 1.954v1.625c0 .468.391.734.86.547C13.781 14.359 16 11.53 16 8.03 16 3.61 12.406 0 7.984 0 3.563 0 0 3.61 0 8.031a7.88 7.88 0 0 0 5.172 7.422c.422.156.828-.125.828-.547v-1.25c-.219.094-.5.156-.75.156-1.031 0-1.64-.562-2.078-1.609-.172-.422-.36-.672-.719-.719-.187-.015-.25-.093-.25-.187 0-.188.313-.328.625-.328.453 0 .844.281 1.25.86.313.452.64.655 1.031.655s.641-.14 1-.5c.266-.265.47-.5.657-.656"/></svg>
              <span class="lp-nav-tool-label">GitHub</span>
            </a>'''
RSS_LINK = re.compile(r'<a\b(?=[^>]*\bclass="lp-rss-link")[^>]*>.*?</a>', re.DOTALL)
THEME_TOGGLE = re.compile(r'<button\b(?=[^>]*\bclass="lp-theme-toggle")[^>]*>.*?</button>', re.DOTALL)
DATE_METADATA = re.compile(
    r'<span class="lp-date-info">.*?</span>|<time class="lp-index-date"[^>]*>.*?</time>',
    re.DOTALL,
)
HOME_STYLESHEET = '<link rel="stylesheet" href="static/homepage.css">'


def customize():
    replaced = 0
    dates_removed = 0
    for page in ROOT.rglob("*.html"):
        html = page.read_text(encoding="utf-8")
        updated, count = RSS_LINK.subn(lambda _: MARKUP, html)
        if not count and page == ROOT / "index.html":
            raise RuntimeError("Expected Leafpress RSS navigation link not found on homepage.")
        updated, date_count = DATE_METADATA.subn("", updated)
        updated = THEME_TOGGLE.sub("", updated)
        if page == ROOT / "index.html":
            updated = re.sub(r'<span class="lp-reading-time">.*?</span>', "", updated, flags=re.DOTALL)
            if "</head>" not in updated:
                raise RuntimeError("Expected a head element in the homepage.")
            for asset in ("homepage.css", "wallpaper.gif", "wallpaper.png"):
                if not (ROOT / "static" / asset).is_file():
                    raise RuntimeError(f"Missing homepage asset: {asset}")
            updated = updated.replace("</head>", f"  {HOME_STYLESHEET}\n</head>", 1)
        if updated != html:
            page.write_text(updated, encoding="utf-8")
        replaced += count
        dates_removed += date_count
    if not replaced:
        raise RuntimeError("No navigation links were customized.")
    print(f"GitHub navigation link added to {replaced} pages.")
    print(f"Removed {dates_removed} automatic date labels.")


if __name__ == "__main__":
    customize()

