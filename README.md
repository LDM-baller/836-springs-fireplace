# 836 Springs Fireplace Road

A private photo gallery for the finished house at 836 Springs Fireplace Road,
Springs, East Hampton, NY — on Accabonac Harbor, beside the Merrill Lake Sanctuary.

Three pages:

- **Gallery** (`/`) — twenty-five photographs by **Tim Williams** of the finished house, sequenced as a
  walkthrough and captioned with the finishes visible in each frame, plus historical notes on the location.
- **Three renovations** (`/history/`) — what the property was, what the renovation before this one did to
  it, and what survived each. Photographs recovered from an album owned by the current owners.
- **Site map** (`/map/`) — the surveyed plan with clickable zones, pairing album photographs against the
  finished house for each part of the property.

## Rights

The finished-house photographs are Tim Williams'. The album photographs of the earlier renovation
belong to the current owners. Everything here is published for the owners' own use — do not reuse
the images. All pages carry `noindex, nofollow` so they stay out of search results.

## Build

`index.html`, `history/index.html` and `map/index.html` are all generated. Do not edit them by hand.

```
python3 build.py
```

- `plates.py` — captions, section grouping, historical notes, the three-era narrative, the survived/lost
  table and the site-map zones. **Single source of truth for all three pages.**
- `build.py` — resizes the finished-house originals into `img/` at 800w and 1600w, then writes all three
  pages. The album photographs and the plan crop are committed directly under `img/`.
- Finished-house originals live in the Property Manager document library, not in this repo.

## Deploy

GitHub Pages, served from the default branch root.
