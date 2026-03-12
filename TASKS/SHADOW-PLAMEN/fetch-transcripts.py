#!/usr/bin/env python3
"""Fetch transcripts for video IDs and save as text files."""
import os, sys, time, re
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("pip3 install --break-system-packages youtube-transcript-api")
    sys.exit(1)

ids_file = Path("/tmp/shadow-playlist-ids.txt")
sources_dir = Path("TASKS/SHADOW-PLAMEN/sources")
sources_dir.mkdir(parents=True, exist_ok=True)

video_ids = [line.strip() for line in ids_file.read_text().splitlines() if line.strip()]
print(f"Processing {len(video_ids)} videos...")

# Check which are already done
existing = {f.stem.split("_")[0] for f in sources_dir.glob("*.txt")}

stats = {"fetched": 0, "no_transcript": 0, "error": 0, "skipped": 0, "rate_limited": 0}
ytt_api = YouTubeTranscriptApi()

for i, vid_id in enumerate(video_ids):
    if vid_id in existing:
        stats["skipped"] += 1
        continue

    try:
        transcript = ytt_api.fetch(vid_id, languages=["bg"])
        text = "\n".join([entry.text for entry in transcript.snippets])

        if len(text.strip()) < 50:
            stats["no_transcript"] += 1
            continue

        filename = f"{vid_id}_{i+1:03d}.bg.txt"
        (sources_dir / filename).write_text(text, encoding="utf-8")
        stats["fetched"] += 1

        if stats["fetched"] % 25 == 0:
            print(f"  [{i+1}/{len(video_ids)}] fetched:{stats['fetched']} no_sub:{stats['no_transcript']} err:{stats['error']} skip:{stats['skipped']}")

        time.sleep(0.3)

    except Exception as e:
        err = str(e)
        if "No transcript" in err or "not translatable" in err or "disabled" in err:
            stats["no_transcript"] += 1
        elif "429" in err or "Too Many" in err:
            stats["rate_limited"] += 1
            print(f"  Rate limited at {i+1}. Sleeping 60s...")
            time.sleep(60)
        else:
            stats["error"] += 1
            if stats["error"] <= 10:
                print(f"  Error {vid_id}: {err[:80]}")

    if (i + 1) % 100 == 0:
        print(f"  Progress: {i+1}/{len(video_ids)} — {stats}")

print(f"\nDone! {stats}")
print(f"Files: {len(list(sources_dir.glob('*.txt')))}")
