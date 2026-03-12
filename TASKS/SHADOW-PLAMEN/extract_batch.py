#!/usr/bin/env python3
"""
Shadow Extractor — batch process .srt files into shadow DB.
Processes a batch of files, skips already-processed ones.
"""

import os
import re
import sys
import json
import glob
import subprocess
import time
from pathlib import Path
from openai import OpenAI

# Config
SOURCES_DIR = "/Users/plamen/.openclaw/workspace-entrepreneur/TASKS/SHADOW-PLAMEN/sources"
PROCESSED_FILE = "/Users/plamen/.openclaw/workspace-entrepreneur/TASKS/SHADOW-PLAMEN/processed_srts.txt"
PSQL = "/opt/homebrew/Cellar/postgresql@16/16.12/bin/psql"
PSQL_CONN = "postgresql://openclaw@%2Ftmp:5433/openclaw"
SHADOW_ID = "plamen"
BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "25"))

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def srt_to_text(filepath):
    """Extract clean text from an SRT file."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    lines = content.split('\n')
    text_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\d+$', line):
            continue
        if re.match(r'^\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}', line):
            continue
        text_lines.append(line)
    return ' '.join(text_lines)


def get_processed():
    if not os.path.exists(PROCESSED_FILE):
        return set()
    with open(PROCESSED_FILE, 'r') as f:
        return set(line.strip() for line in f if line.strip())


def mark_processed(video_id):
    with open(PROCESSED_FILE, 'a') as f:
        f.write(video_id + '\n')


def run_sql(sql):
    result = subprocess.run(
        [PSQL, PSQL_CONN, '-c', sql],
        capture_output=True, text=True
    )
    if result.returncode != 0 and 'duplicate' not in result.stderr.lower():
        print(f"  SQL error: {result.stderr[:300]}", file=sys.stderr)
    return result.returncode == 0


def esc(s):
    if s is None:
        return 'NULL'
    return "'" + str(s).replace("'", "''") + "'"


EXTRACTION_PROMPT = """You are analyzing Bulgarian-language YouTube video subtitles from the channel of Plamen — a Bulgarian Bitcoin educator, programmer, and entrepreneur from Varna/Sofia.

VIDEO ID: {video_id}
TEXT LENGTH: {text_len} chars

TEXT (excerpt):
{text}

Extract insights about PLAMEN (the host/speaker) for his shadow profile. 

SKIP rules:
- If text < 150 chars, skip
- If clearly NOT Plamen speaking (dubbed English content, other person's monologue not related to Plamen), skip
- If text is nonsensical/corrupted subtitles, skip

Return ONLY JSON. Schema:

{{
  "skip": false,
  "identities": [
    // Facts about who Plamen IS
    // category: one of: occupation, background, location, finance, family, personality
    // key: short unique snake_case key
    // value: fact in ENGLISH
    // confidence: 0-100
    // time_context: approximate time period or null
    {{"category": "string", "key": "string", "value": "string", "confidence": 80, "time_context": null}}
  ],
  "traits": [
    // Plamen's beliefs, opinions, stances (topic must be unique per shadow)
    // stance: short slug like passionate_advocate, deeply_critical, pragmatic_optimist
    // intensity: 1-10
    {{"topic": "string", "stance": "string", "evidence": "string in English", "intensity": 7, "context": "string"}}
  ],
  "stories": [
    // Anecdotes Plamen tells or references
    // trigger_topic: what causes him to tell this story
    // story_summary: in English
    // key_quote: translated to English if memorable
    // emotional_tone: one word
    {{"trigger_topic": "string", "story_summary": "string", "key_quote": "string or empty", "emotional_tone": "string"}}
  ],
  "voice": [
    // Speech patterns unique to Plamen
    // pattern_type: filler_word, transition_word, discourse_marker, analogy_making, rhetorical_question, structure
    // frequency: always, often, sometimes, rarely
    {{"pattern_type": "string", "example": "BG text example", "rule": "English description", "frequency": "often"}}
  ],
  "boundaries": [
    // Topics Plamen avoids or deflects in public
    // knowledge_level: deep, surface, or unknown
    // typical_response: what he typically says/does when topic comes up
    {{"topic": "string", "knowledge_level": "surface", "typical_response": "string"}}
  ],
  "relationships": [
    // People Plamen mentions by name or role
    // person_label: name or role (e.g., "баща ми", "Влади", "Стефан")
    // relationship_type: friend, family, colleague, public_figure, viewer
    // sentiment: positive, neutral, negative
    {{"person_label": "string", "relationship_type": "string", "context": "string in English", "sentiment": "neutral"}}
  ]
}}

Rules:
- Only include sections with ACTUAL findings from THIS video
- Max 4 items per section
- Keep it focused — only what's genuinely new/significant
- If nothing significant: return {{"skip": true, "reason": "no new shadow-relevant content"}}
"""


def extract_insights(video_id, text):
    if len(text) < 100:
        return None
    text_excerpt = text[:7000] if len(text) > 7000 else text
    prompt = EXTRACTION_PROMPT.format(
        video_id=video_id,
        text_len=len(text),
        text=text_excerpt
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.2,
        max_tokens=1500
    )
    content = response.choices[0].message.content
    return json.loads(content)


def insert_insights(video_id, data):
    source = f"srt:{video_id}"
    inserted = 0
    skipped = 0

    # Identities
    for item in data.get("identities", []):
        tc = esc(item.get("time_context"))
        sql = (f"INSERT INTO shadow.identities "
               f"(shadow_id, category, key, value, source, confidence, time_context) "
               f"VALUES ({esc(SHADOW_ID)}, {esc(item['category'])}, {esc(item['key'])}, "
               f"{esc(item['value'])}, {esc(source)}, {item.get('confidence', 80)}, {tc}) "
               f"ON CONFLICT (shadow_id, key, COALESCE(time_context, '__none__')) DO NOTHING;")
        if run_sql(sql):
            inserted += 1
        else:
            skipped += 1

    # Traits
    for item in data.get("traits", []):
        sql = (f"INSERT INTO shadow.traits "
               f"(shadow_id, topic, stance, evidence, intensity, context, source) "
               f"VALUES ({esc(SHADOW_ID)}, {esc(item['topic'])}, {esc(item['stance'])}, "
               f"{esc(item.get('evidence', ''))}, {item.get('intensity', 7)}, "
               f"{esc(item.get('context', ''))}, {esc(source)}) "
               f"ON CONFLICT (shadow_id, topic, stance) DO NOTHING;")
        if run_sql(sql):
            inserted += 1
        else:
            skipped += 1

    # Stories
    for item in data.get("stories", []):
        sql = (f"INSERT INTO shadow.stories "
               f"(shadow_id, trigger_topic, story_summary, key_quote, emotional_tone, source) "
               f"VALUES ({esc(SHADOW_ID)}, {esc(item['trigger_topic'])}, {esc(item['story_summary'])}, "
               f"{esc(item.get('key_quote', ''))}, {esc(item.get('emotional_tone', 'neutral'))}, "
               f"{esc(source)}) "
               f"ON CONFLICT (shadow_id, trigger_topic, md5(story_summary)) DO NOTHING;")
        if run_sql(sql):
            inserted += 1
        else:
            skipped += 1

    # Voice
    for item in data.get("voice", []):
        sql = (f"INSERT INTO shadow.voice "
               f"(shadow_id, pattern_type, example, rule, frequency, register, source) "
               f"VALUES ({esc(SHADOW_ID)}, {esc(item['pattern_type'])}, {esc(item['example'])}, "
               f"{esc(item['rule'])}, {esc(item.get('frequency', 'sometimes'))}, "
               f"'youtube', {esc(source)}) "
               f"ON CONFLICT (shadow_id, pattern_type, example, register) DO NOTHING;")
        if run_sql(sql):
            inserted += 1
        else:
            skipped += 1

    # Boundaries
    for item in data.get("boundaries", []):
        kl = item.get("knowledge_level", "surface")
        if kl not in ("deep", "surface", "unknown"):
            kl = "surface"
        sql = (f"INSERT INTO shadow.boundaries "
               f"(shadow_id, topic, knowledge_level, typical_response, source) "
               f"VALUES ({esc(SHADOW_ID)}, {esc(item['topic'])}, {esc(kl)}, "
               f"{esc(item.get('typical_response', ''))}, {esc(source)}) "
               f"ON CONFLICT (shadow_id, topic) DO NOTHING;")
        if run_sql(sql):
            inserted += 1
        else:
            skipped += 1

    # Relationships
    for item in data.get("relationships", []):
        sent = item.get("sentiment", "neutral")
        if sent not in ("positive", "neutral", "negative"):
            sent = "neutral"
        sql = (f"INSERT INTO shadow.relationships "
               f"(shadow_id, person_label, relationship_type, context, sentiment, source) "
               f"VALUES ({esc(SHADOW_ID)}, {esc(item['person_label'])}, {esc(item['relationship_type'])}, "
               f"{esc(item.get('context', ''))}, {esc(sent)}, {esc(source)}) "
               f"ON CONFLICT (shadow_id, person_label, relationship_type) DO NOTHING;")
        if run_sql(sql):
            inserted += 1
        else:
            skipped += 1

    return inserted, skipped


def main():
    all_srts = sorted(glob.glob(f"{SOURCES_DIR}/*.bg.srt"), key=os.path.getsize)
    processed = get_processed()
    pending = [f for f in all_srts if Path(f).stem.replace('.bg', '') not in processed]

    print(f"Total SRTs: {len(all_srts)}, Already processed: {len(processed)}, Pending: {len(pending)}")

    batch = pending[:BATCH_SIZE]
    print(f"Processing batch of {len(batch)} files\n")

    total_inserted = 0
    total_skipped_files = 0
    errors = 0
    processed_this_run = []

    for srt_path in batch:
        video_id = Path(srt_path).stem.replace('.bg', '')
        size = os.path.getsize(srt_path)
        print(f"→ {video_id} ({size:,}b)", end=" ")

        try:
            text = srt_to_text(srt_path)
            if len(text) < 100:
                print(f"[SKIP: too short {len(text)}c]")
                mark_processed(video_id)
                total_skipped_files += 1
                continue

            data = extract_insights(video_id, text)

            if not data or data.get("skip"):
                reason = data.get("reason", "N/A") if data else "parse error"
                print(f"[SKIP: {reason}]")
                mark_processed(video_id)
                total_skipped_files += 1
                continue

            ins, dup = insert_insights(video_id, data)
            print(f"[+{ins} rows, {dup} dup]")
            total_inserted += ins
            mark_processed(video_id)
            processed_this_run.append(video_id)

            time.sleep(0.3)

        except Exception as e:
            print(f"[ERROR: {e}]")
            errors += 1

    remaining = len(pending) - len(batch)
    print(f"\n{'='*60}")
    print(f"Run complete:")
    print(f"  Files processed: {len(processed_this_run)}")
    print(f"  Files skipped:   {total_skipped_files}")
    print(f"  Errors:          {errors}")
    print(f"  DB rows added:   {total_inserted}")
    print(f"  Still pending:   {remaining}")

    return {
        "processed": len(processed_this_run),
        "skipped": total_skipped_files,
        "errors": errors,
        "inserted": total_inserted,
        "remaining": remaining
    }


if __name__ == "__main__":
    result = main()
    sys.exit(0)
