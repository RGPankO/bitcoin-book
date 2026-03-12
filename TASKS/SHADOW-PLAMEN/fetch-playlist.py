#!/usr/bin/env python3
"""Fetch all transcripts from a YouTube playlist and save as text files in sources/."""

import os
import sys
import json
import time
import re
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("pip3 install youtube-transcript-api")
    sys.exit(1)

try:
    import subprocess
    # Use yt-dlp to get the playlist video IDs (it handles pagination)
    result = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--print", "%(id)s\t%(title)s", "--no-warnings",
         "https://www.youtube.com/playlist?list=PL3t1EhdUj1f4gqy7wN2a0kY2FhrVI0kxY"],
        capture_output=True, text=True, timeout=120
    )
    videos = []
    for line in result.stdout.strip().split("\n"):
        if "\t" in line:
            vid_id, title = line.split("\t", 1)
            videos.append((vid_id, title))
    print(f"Found {len(videos)} videos in playlist")
except Exception as e:
    print(f"Error getting playlist: {e}")
    sys.exit(1)

sources_dir = Path("TASKS/SHADOW-PLAMEN/sources")
sources_dir.mkdir(parents=True, exist_ok=True)

stats = {"fetched": 0, "no_transcript": 0, "error": 0, "skipped": 0}

for i, (vid_id, title) in enumerate(videos):
    # Clean title for filename
    safe_title = re.sub(r'[^\w\s-]', '', title)[:80].strip()
    filename = f"{i+1:03d}_{safe_title}.bg.txt"
    filepath = sources_dir / filename

    if filepath.exists():
        stats["skipped"] += 1
        continue

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(vid_id, languages=["bg"])
        text = "\n".join([entry.text for entry in transcript.snippets])
        
        if len(text.strip()) < 50:
            stats["no_transcript"] += 1
            continue

        filepath.write_text(text, encoding="utf-8")
        stats["fetched"] += 1
        
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(videos)} — fetched: {stats['fetched']}, no_transcript: {stats['no_transcript']}, errors: {stats['error']}")
        
        time.sleep(0.5)  # Gentle rate limit
        
    except Exception as e:
        err_str = str(e)
        if "No transcript" in err_str or "not translatable" in err_str:
            stats["no_transcript"] += 1
        else:
            stats["error"] += 1
            if stats["error"] <= 5:
                print(f"  Error on {vid_id} ({title[:40]}): {err_str[:100]}")
            if "429" in err_str or "Too Many" in err_str:
                print(f"  Rate limited at video {i+1}. Sleeping 30s...")
                time.sleep(30)

print(f"\nDone! {stats}")
print(f"Files in sources/: {len(list(sources_dir.glob('*.txt')))}")
