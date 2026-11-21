# Ani's website

**Website:** [aniruddhapisolkar.github.io/homepage](https://aniruddhapisolkar.github.io/homepage/)

Built with [Leafpress](https://leafpress.in). Everything is edited in GitHub using Markdown.

## Edit a page

Open any `.md` file → click the pencil icon → make your changes → **Commit changes**.

| File or folder | Content |
| --- | --- |
| `index.md` | Homepage |
| `about.md` | About |
| `blog/` | Blog posts |
| `portfolio/` | Projects |
| `style.css` | Colors and typography |
| `leafpress.json` | Site settings |

## Add a page

Click **Add file → Create new file**. Enter a path like `blog/my-first-post.md`, then write:

```markdown
---
title: "My First Post"
---

Your content here.

## A heading

More content.
```

Commit the file. Its URL will be `/homepage/blog/my-first-post/`. Put standalone pages at the root, like `now.md`.

## Add a group of pages

Create a new file named `research/_index.md`:

```markdown
---
title: "Research"
---

My research and experiments.
```

Then create pages inside `research/`, such as `research/first-experiment.md`. Leafpress makes the section page and lists its pages. To add a new top-level navigation link, add an entry to `navigation.items` in `leafpress.json`.

For a Portfolio project, create `portfolio/my-project/_index.md` with its title and `showList: false` if you want to write your own contents list. Add a bullet linking to `/homepage/portfolio/my-project/` in `portfolio/_index.md`. Projects stay under Portfolio instead of appearing in the navbar.

Creation dates are not displayed on the website. No date, sort, or table-of-contents metadata is needed.

## Links, images, and drafts

- Link to an existing page: `[[blog/my-first-post]]`
- Custom link text: `[[blog/my-first-post|Read my first post]]`
- External link: `[GitHub](https://github.com)`
- Image: upload `photo.png` to `static/images/`, then add `![[photo.png]]` in a page.
- Draft: add `draft: true` to the frontmatter to keep a page off the website.
- When renaming or deleting pages, update any wiki links pointing to them.

**Note:** This repo is public, so drafts committed here are still publicly readable.

## Publish

Commit changes to `main` (or merge a pull request). GitHub Actions rebuilds and deploys the website automatically. See [Actions](https://github.com/aniruddhapisolkar/homepage/actions) for deployment progress.

One-time setup: [Settings → Pages](https://github.com/aniruddhapisolkar/homepage/settings/pages) → set **Source** to **GitHub Actions**.

[Leafpress writing guide](https://leafpress.in/guide/writing/)
