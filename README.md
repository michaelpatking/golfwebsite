# Courses I've Played

A silly old game that I find beautiful. Not-so-scientific rankings of the golf courses I've played, grouped by place.

It's a plain static site: one `index.html`, the photos, and the fonts. No server, no database, no build step needed to host it.

## Hosting

Any static host works. Point it at the root of this repo.

- **GitHub Pages:** Settings → Pages → Deploy from branch → `main`, folder `/ (root)`. The `.nojekyll` file is already there.
- **Netlify or Cloudflare Pages:** connect the repo, leave the build command empty, publish directory `/`. These hosts also read `_headers` (security headers and caching).

`404.html` is the "Lost ball" page for broken links. `robots.txt` allows search engines.

### Once you have a domain

Rebuild with your address so link previews (iMessage, WhatsApp, LinkedIn) show the Pebble photo and title:

```
cd src
SITE_URL=https://your-domain.com/ python3 build.py
```

That writes `index.html` at the repo root with an absolute share image and a canonical link. Commit and push.

## Updating

Edit files in `src/`, then run `python3 build.py` from inside `src/`. It rebuilds the root `index.html`.

- **Scores and courses:** `src/data.json` (exported from my rankings spreadsheet).
- **Course maps:** `src/layouts.json`.
- **One-liners and journal entries:** the `JOURNAL` line in `src/tpl.html`, keyed by course slug, e.g. `"muirfield":{"tag":"…","when":"May 2024","body":"…"}`.
- **Photos:** `photos/<slug>.jpg` (1800×1200) with a `photos/sm/` copy (900×600); gallery photos in `photos/g/` and `photos/g/sm/`. When you replace a photo, bump `PV` in `src/tpl.html` so browsers fetch the new one.

Photos have no location data in them. Fonts are self-hosted from `fonts/`, so the site makes no requests to anyone else.

Course maps © OpenStreetMap contributors.
