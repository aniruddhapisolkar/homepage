# Ani's homepage

A personal website, blog, portfolio, and notebook built with [Leafpress](https://leafpress.in). A push to `main` triggers GitHub Actions to build and publish the site to [GitHub Pages](https://aniruddhapisolkar.github.io/homepage/).

## Where everything lives

| File or folder | Purpose |
| --- | --- |
| `index.md` | Homepage |
| `about.md` | About page |
| `blog/` | Essays and articles |
| `portfolio/` | Projects |
| `notes/` | Short notes |
| `static/images/` | Uploaded images |
| `leafpress.json` | Site settings and navigation |
| `style.css` | Coffee-house palette and type styles |
| `.github/workflows/deploy.yml` | Build and publishing pipeline |

## Publish a new page on GitHub

1. In this repo, go to **Code → Add file → Create new file**.
2. Enter its path, e.g. `blog/my-new-post.md` or `portfolio/my-project.md`. Slashes create directories automatically.
3. Paste your Markdown. For example:

```markdown
---
title: "My new post"
date: 2026-11-19
tags: [ai, learning]
description: "A short summary."
---

Write your article here.

## A section

Add paragraphs, lists, links, or fenced code blocks.
```

4. Click **Commit changes**. Commit to main to publish immediately, or work on a branch and merge a pull request.
5. Check **Actions** for the deployment status. Once successful, the example above lives at `/homepage/blog/my-new-post/`.

Use short lowercase hyphenated filenames. The path becomes the URL; the `title` is the displayed heading. An optional `slug` changes the filename portion of a URL. Dates and descriptions are optional; tags create related page listings.

## Create a new group of pages

Create `research/_index.md`:

```markdown
---
title: "Research"
sort: date
toc: false
---

Research notes and experiments.
```

Then create `research/my-first-experiment.md`. Leafpress automatically creates a section page at `/research/` and links to it in the top navigation. Its section index lists its published pages (set `showList: false` to hide the listing). Subfolders such as `research/experiments/` can have their own `_index.md` too.

Navigation currently uses automatic mode. Switch to `navigation.mode: "explicit"` and add `items` in `leafpress.json` if you ever need precise manual controls for labels or ordering.

## Writing tools

- Link to another page: `[[blog/first-entry|My first entry]]`.
- Upload an image into `static/images/photo.png` and embed it using `![[photo.png]]`.
- Markdown headings, tables, fenced code blocks, and lists work normally.
- A page marked `draft: true` won't be published. The `drafts/` folder and `*.draft.md` files are ignored by the build too. **This repository is public: unpublished markdown committed here is still publicly readable. Keep genuinely private notes outside it.**
- Remove the example articles when you are ready; remember to remove or replace links pointing to them.

## Preview locally

Install Leafpress using the [official installation guide](https://leafpress.in/guide/installation/) (use version 1.1.2 for parity with CI). Then:

```sh
git clone https://github.com/aniruddhapisolkar/homepage.git
cd homepage
leafpress serve
```

Open http://localhost:3000. For a production build run `leafpress build --strict`.

## Typography

[Obel Mono](https://typographic.systems/obel-mono) 1.004 is bundled in `static/fonts/obel-mono/` as its original unmasked Roman and Italic variable WOFF2 fonts, with the SIL Open Font License and author notice. `leafpress.json` registers the files for headings, body text, and code; `style.css` defines the warm light and dark palettes.

Fonts are self-hosted, so neither builds nor visitors need to contact an external font service.

## First-time publishing setup

In GitHub, open **Settings → Pages → Build and deployment** and set Source to **GitHub Actions**. Then open **Actions**, select **Build and deploy Leafpress**, and click **Run workflow** if you need to deploy before the next push to main.

Further reading: [Writing content](https://leafpress.in/guide/writing/) · [Configuration](https://leafpress.in/guide/configuration/) · [Theming](https://leafpress.in/guide/theming/) · [GitHub Pages deployment](https://leafpress.in/guide/deploy-github/).
