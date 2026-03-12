#!/usr/bin/env bash
# Download auto-generated BG subtitles from the FULL videos playlist
#
# Error handling strategy:
#   - 429/throttle → global cooldown (exponential), retry SAME video, never skip
#   - No subtitles available → skip immediately, log to .no-subs
#   - Other errors → skip, log to .errors
#
# Global throttle detection: if we get 429 on any video, pause globally
# because YouTube throttles the IP, not individual videos.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../.."

SOURCES_DIR="TASKS/SHADOW-PLAMEN/sources-full"
IDS_FILE="/tmp/shadow-full-playlist-ids.txt"
PROGRESS="$SOURCES_DIR/.progress"
LOG="$SOURCES_DIR/.fetch-log"
NO_SUBS_LOG="$SOURCES_DIR/.no-subs"
ERRORS_LOG="$SOURCES_DIR/.errors"

mkdir -p "$SOURCES_DIR"
total=$(wc -l < "$IDS_FILE" | tr -d ' ')
start=1; [ -f "$PROGRESS" ] && start=$(head -1 "$PROGRESS" | tr -dc '0-9')

echo "[$(date)] Starting from #$start of $total" >> "$LOG"

BACKOFF_STEPS=(60 120 300 600 1200 1800 3600 7200 14400)
global_backoff_level=0
max_backoff_level=${#BACKOFF_STEPS[@]}

fetched=0; no_subs=0; errors=0

i=0
while IFS= read -r vid; do
  i=$((i + 1))
  [ $i -lt $start ] && continue

  [ -f "$SOURCES_DIR/${vid}.bg.srt" ] && { echo $((i+1)) > "$PROGRESS"; continue; }

  grep -qxF "$vid" "$NO_SUBS_LOG" 2>/dev/null && { echo $((i+1)) > "$PROGRESS"; continue; }

  while true; do
    result=$(yt-dlp --write-auto-sub --sub-lang bg --sub-format srt --skip-download \
      --sleep-subtitles 10 --cookies-from-browser chrome --no-warnings \
      -o "$SOURCES_DIR/${vid}.%(ext)s" \
      "https://www.youtube.com/watch?v=${vid}" 2>&1) || true

    if echo "$result" | grep -q "429\|Too Many\|HTTP Error 429"; then
      if [ $global_backoff_level -lt $max_backoff_level ]; then
        wait=${BACKOFF_STEPS[$global_backoff_level]}
      else
        wait=${BACKOFF_STEPS[$((max_backoff_level - 1))]}
      fi
      global_backoff_level=$((global_backoff_level + 1))
      echo "[$(date)] [$i/$total] $vid: 429 — global cooldown ${wait}s (level $global_backoff_level)" >> "$LOG"
      sleep $wait
      continue

    elif echo "$result" | grep -q "Writing video subtitles"; then
      fetched=$((fetched + 1))
      global_backoff_level=0
      echo "[$(date)] [$i/$total] $vid: FETCHED (total: $fetched)" >> "$LOG"
      break

    elif echo "$result" | grep -qi "no subtitles\|subtitles are disabled\|no automatic captions"; then
      no_subs=$((no_subs + 1))
      echo "$vid" >> "$NO_SUBS_LOG"
      echo "[$(date)] [$i/$total] $vid: NO SUBS (total: $no_subs)" >> "$LOG"
      break

    else
      errors=$((errors + 1))
      echo "[$(date)] $vid: $result" >> "$ERRORS_LOG"
      echo "[$(date)] [$i/$total] $vid: ERROR (total: $errors) — see .errors log" >> "$LOG"
      break
    fi
  done

  echo $((i + 1)) > "$PROGRESS"
  [ $((i % 50)) -eq 0 ] && echo "[$(date)] [$i/$total] fetched:$fetched no_subs:$no_subs errors:$errors" >> "$LOG"

  sleep 15
done < "$IDS_FILE"

echo "[$(date)] COMPLETE. fetched:$fetched no_subs:$no_subs errors:$errors total:$total" >> "$LOG"
