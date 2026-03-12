# Shadow Extractor — Extract Task

## Role
`nexus-extensions/shadow/ROLES/SHADOW-EXTRACTOR.md`

## Assignee label
`shadow-extractor`

## Mode
runner-state

## Shadow Identity
Read `SHADOW_ID` from task `.env`. Default: `plamen`.

## DB Config
```env
SHADOW_DB_HOST=localhost
SHADOW_DB_PORT=5433
SHADOW_DB_NAME=openclaw
SHADOW_DB_USER=openclaw
```

---

## Scope — what this task does and does NOT do

**Does:** Read prepared text files from `sources/` → extract personality data → write to shadow DB.
**Does NOT:** Download videos, fetch URLs, convert PDFs, or gather data from external sources.

Data gathering is done BEFORE the extractor runs — by the operator, builder, or a prep script.
The extractor only reads files that are already in the `sources/` directory.

---

## Run Loop (every run)

1. **Read NOTES.md** — apply operator overrides first
2. **Read HANDOFF.md** — load progress state (which sources done, which pending)
3. **Scan `sources/` directory** in the instance task dir (e.g. `TASKS/SHADOW-PLAMEN/sources/`)
4. **Compare against HANDOFF.md** — identify unprocessed files
5. **Process as many unprocessed sources as possible** within the run time budget.
   Do NOT impose an artificial per-run limit. Process until done or time runs out.
6. **For each source file:**
   a. Read the file content
   b. Extract identities, traits, voice patterns (see ROLES/SHADOW-EXTRACTOR.md)
   c. Dedup-check each record against DB before insert
   d. Insert new records
   e. Log counts
7. **Update HANDOFF.md** with progress after each source (not just at end of run)
8. **If all sources processed:** self-disable cron, log completion in HANDOFF.md

---

## Supported source file formats

- `.vtt` / `.srt` — subtitle files (strip timestamps, extract text only)
- `.txt` / `.md` — plain text or markdown
- Other formats: skip and log as anomaly in HANDOFF.md

---

## Instance file structure

The extractor reads from the INSTANCE task directory (not the extension):

```
TASKS/SHADOW-<NAME>/
├── HANDOFF.md     (progress — update every run)
├── CONTEXT.md     (metadata — shadow_id, source description)
├── NOTES.md       (operator overrides)
├── .env           (SHADOW_ID=<name>)
├── runs/          (per-run logs)
└── sources/       (prepared text/subtitle files — operator-managed)
```

---

## HANDOFF.md Schema

```markdown
# Extraction Progress

## Stats
- Total sources: N
- Processed: N
- Pending: N
- Last run: YYYY-MM-DD HH:MM

## Processed Sources
- source1.bg.vtt — 5 identities, 3 traits, 7 voice (2026-02-24)
- source2.bg.vtt — 2 identities, 1 trait, 4 voice (2026-02-24)

## Pending Sources
- source3.bg.vtt
- source4.bg.vtt

## Anomalies
- source5.xyz: skipped — unsupported format
```

---

## Acceptance Criteria

- Processes all available source files (no artificial limit)
- HANDOFF.md updated after every source (crash-safe progress)
- New records visible in shadow.identities / shadow.traits / shadow.voice
- Duplicate records skipped (dedup via DB unique constraints)
- Unsupported files logged as anomalies, not errors
- Cron self-disables when all sources processed
