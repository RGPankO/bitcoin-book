# Shadow Plamen — Source Context

## SHADOW_ID
plamen

## Sources

### Source 1: Bitcoin Basics Playlist (6 videos, processed)
URL: https://www.youtube.com/watch?v=6B7i1iTnmqY&list=PL3t1EhdUj1f7bpderh4Gxgq9_MunYOPx4

### Source 2: "Започни от ТУК" Playlist (790 videos, pending)
URL: https://www.youtube.com/watch?v=_Q05n1idiNU&list=PL3t1EhdUj1f4gqy7wN2a0kY2FhrVI0kxY
Video IDs: /tmp/shadow-playlist-ids.txt (790 IDs)
Subtitle files: TASKS/SHADOW-PLAMEN/sources/*.bg.srt

## Language
Videos are in Bulgarian. Extract in Bulgarian, store insights in English.

### Source 3: Facebook Archive (1,464 posts, May 2020 → Mar 2026)
File: sources/fb-archive-clean.md (~1.7MB)
Format: Posts delimited by `===`, chronological order
Note: This is ONE large file, not many small ones. Process in chunks (~100 posts per run).

## Data Prep
- SRT sources: All 411 files fully processed (168 sources/ + 243 sources-full/)
- FB archive: Ready for extraction in sources/fb-archive-clean.md
- Extractor reads from `sources/` directory — prepared text/subtitle files only.
