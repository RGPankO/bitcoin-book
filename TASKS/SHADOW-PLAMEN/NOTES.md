# Shadow Plamen — Notes

## 2026-03-06 (Overseer) — PRIORITY

### Step 1: Dedup existing DB (ticket #1205)
Before any new extraction, clean the mess:
- Use `memq shadow search --project plamen "" --table <table>` to scan each table
- Identify semantic duplicates (same meaning, different wording)
- Keep the BEST entry (highest confidence, most detail)
- Delete the rest via `nexus/tools/psqlq -U openclaw -d openclaw -p 5433 -c "DELETE FROM shadow.<table> WHERE id = <id>"`
- Known worst offenders: "Bitcoin educator" (14 dupes in identities), "Varna/Sofia" (10 dupes), full name (multiple)
- Track before/after counts in ticket notes

### Step 2: FB Archive extraction (new source)
- `sources/fb-archive-clean.md` — 1.7MB, 1,464 FB posts (May 2020 → Mar 2026)
- This is ONE large file. Read it in chunks (~100 posts per run), track progress by post number in HANDOFF.md
- Posts are delimited by `===`
- Extract using the SHADOW-EXTRACTOR.md role rules — all 6 categories
- **DB-aware extraction**: Before sending each batch to LLM, query existing DB entries for relevant categories and include them as context. Let the LLM decide what's genuinely novel vs redundant. NO hardcoded exclusion lists.
- The whole point is: don't recreate the "Bitcoin educator × 14" problem

### Quality rule (standing)
- Don't extract obvious/repetitive facts (name, profession, base location) that already exist in DB
- When in doubt, check DB first with `memq shadow search`

## 2026-02-27 (Overseer)

**CRITICAL: Update HANDOFF.md after EACH source file**, not just at end of run.
Previous runs timed out at 300s without saving progress — you have 600s now.

Before processing, check what's already in the DB to avoid re-extracting:
```sql
SELECT DISTINCT source FROM shadow.identities WHERE shadow_id='plamen';
```
Skip any source already in the DB. Update HANDOFF.md processed list after each file.

If you still can't finish all 168 files in one run, that's fine — just save progress so the next run picks up where you left off.

## 2026-02-24

Initial extraction run by cron:builder (Phase 3).
See runs/ directory for extraction logs.
