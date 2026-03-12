# Shadow Fetch — YouTube Subtitle Download Monitor

## Role
Lightweight monitor cron. No special role file needed.

## Assignee label
`shadow-fetch`

## Mode
runner-state

## Purpose
Check if YouTube rate limit has cleared, then start the subtitle batch download and notify main session.

## Run Logic

1. Test rate limit: try downloading ONE subtitle file for video `Qi-Lv3FCC3A` (known to have BG subs)
   ```bash
   yt-dlp --write-auto-sub --sub-lang bg --sub-format srt --skip-download \
     --cookies-from-browser chrome --no-warnings \
     -o "/tmp/shadow-ratelimit-test.%(ext)s" \
     "https://www.youtube.com/watch?v=Qi-Lv3FCC3A" 2>&1
   ```

2. If result contains "429" or "Too Many":
   - Log: "Rate limit still active"
   - Exit. Do nothing else. Wait for next run.

3. If result contains "Writing video subtitles" (success!):
   - Clean up test file: `rm -f /tmp/shadow-ratelimit-test.bg.srt`
   - Start batch download:
     ```bash
     nohup bash TASKS/SHADOW-PLAMEN/fetch-subs.sh > /tmp/shadow-fetch-stdout.log 2>&1 &
     ```
   - Notify main session:
     ```bash
     openclaw system event --text "YouTube rate limit cleared. Subtitle download started for 790 videos. Monitor: tail -f TASKS/SHADOW-PLAMEN/sources/.fetch-log" --mode now
     ```
   - Self-disable this cron
   - Exit

4. If result contains "no subtitles" — something changed with the test video. Log anomaly, do NOT self-disable, let overseer investigate.

## Self-Disable Condition
Only after successfully starting the batch download.

## Schedule
Every 2 hours.
