# 836 Springs Fireplace Road

A private photo gallery for the finished house at 836 Springs Fireplace Road,
Springs, East Hampton, NY — on Accabonac Harbor, beside the Merrill Lake Sanctuary.

Twenty-five photographs by **Tim Williams**, sequenced as a walkthrough and captioned
with the finishes visible in each frame, plus short historical notes on the location.

## Photograph rights

The photographs are Tim Williams'. They are published here for the owners' own use.
Check the engagement terms before any wider publication, and do not reuse the images.
The page carries `noindex, nofollow` so it stays out of search results.

## Build

`index.html` is generated. Do not edit it by hand.

```
python3 build.py
```

- `plates.py` — captions, section grouping, and the historical notes. Single source of truth.
- `build.py` — resizes the originals into `img/` at 800w and 1600w and writes `index.html`.
- Source images live in the Property Manager document library, not in this repo.

## Deploy

GitHub Pages, served from the default branch root.
