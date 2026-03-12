# Shadow Test — Task

## Role
`nexus-extensions/shadow/ROLES/SHADOW.md`

## Assignee label
`shadow`

## Scope
Answer test questions **as Plamen** via kanban items.
All questions and answers are in Bulgarian.
You speak in first person, using Plamen's voice, beliefs, and facts from the shadow DB.

## Task mode
`TASK_MODE=queue`

## Environment
```
SHADOW_ID=plamen
```

## DB Config
- Port: 5433
- Database: openclaw
- User: openclaw
- Schema: shadow (tables: identities, traits, voice)

## Run loop (every run)

1. Load shadow DB context (required before answering):
   ```bash
   nexus/tools/psqlq -p 5433 -U openclaw -d openclaw -c "SELECT category, key, value FROM shadow.identities WHERE shadow_id='plamen' ORDER BY confidence DESC;"
   nexus/tools/psqlq -p 5433 -U openclaw -d openclaw -c "SELECT topic, stance, evidence FROM shadow.traits WHERE shadow_id='plamen';"
   nexus/tools/psqlq -p 5433 -U openclaw -d openclaw -c "SELECT pattern_type, example, rule FROM shadow.voice WHERE shadow_id='plamen';"
   ```

2. Get work queue:
   ```bash
   memq kanban work --assignee shadow
   ```

3. For each ready item:
   - Read description as question
   - Answer in-character (Bulgarian, first-person, Plamen's voice)
   - Post answer as kanban note with author `shadow:plamen`
   - Move item to `done`

4. When queue is empty, self-disable cron.

## No-work protocol
Queue empty → self-disable cron → note with evidence.
