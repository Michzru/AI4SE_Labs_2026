---
paths:
  - "Week_08_Dissecting/**"
---

# File provenance

Whenever you create a new file, put a provenance note at the very top, in the file's own comment syntax:

```
Created by <agent name> (<model id>) on <YYYY-MM-DD>
```

Example for Python: `# Created by Claude Code (claude-opus-5-5) on 2026-11-26`.
For formats without comments (e.g. JSON), mention the provenance in your reply instead.
Do not add the note when editing an existing file.
