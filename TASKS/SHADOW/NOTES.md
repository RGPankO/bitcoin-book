# Notes from Overseer — 2026-03-12

## Current Work: External Feedback Batch

14 tickets assigned to you, all `in_progress`, tagged `external-feedback`. These are corrections and additions from an external reviewer, approved by Plamen.

Run `memq kanban work --assignee shadow --project bitcoin-book` to see them.

Each ticket description contains:
- The reviewer's feedback
- Oracle's assessment (agree/partially agree)
- The specific file to edit
- What action to take

**Guidelines:**
- These are surgical edits — not full chapter rewrites
- Read the ticket description carefully, it tells you exactly what to change
- Some are 1-line fixes (Nokia→BlackBerry), others are paragraph additions
- For "partially agree" tickets, follow the oracle's nuanced recommendation
- For #1281 (McCaleb): don't use the word "мошеник" — add context about the 80K BTC hole factually
- For #1287 (Bitvavo): add Strike as option, keep Bitvavo, do NOT add Revolut
- One ticket per run, move to `review` and assign `oracle` when done
- Git commit after each edit
