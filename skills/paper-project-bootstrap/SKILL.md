---
name: paper-project-bootstrap
description: Initialize `.paper-os/` state files and an `AGENTS.md` update snippet for a paper workspace. Use when starting a new paper-writing-os project or retrofitting an existing paper repo to use the paper-writing skill workflow.
---

# Paper Project Bootstrap

Use this skill to create per-paper state files for `paper-writing-os`.

## Script

Run:

```bash
python3 scripts/init_paper_project.py \
  --project-dir /path/to/paper \
  --paper-name "Paper Name" \
  --manuscript main.tex \
  --bibliography references.bib \
  --figures-dir figures
```

Optional flags:

- `--state-dir .paper-os`
- `--venue TOPS`
- `--field computer-science`
- `--force`

## What the script creates

- `.paper-os/paper_os_config.yaml`
- `.paper-os/claim_scope.md`
- `.paper-os/evidence_log.md`
- `.paper-os/outline.json`
- `.paper-os/intro_related_work_plan.json`
- `.paper-os/plotting_plan.json`
- `.paper-os/citation_map.json`
- `.paper-os/review_audit.json`
- `.paper-os/reviewer_feedback.json`
- `.paper-os/worklog.json`
- `.paper-os/writing_status.md`
- `.paper-os/AGENTS.update.md`

After running the script:

1. Fill in the generated placeholders, especially in `claim_scope.md` and `evidence_log.md`.
2. Merge `.paper-os/AGENTS.update.md` into the project `AGENTS.md`.
3. Use the `paper-writing-os` skill in that workspace.

For the generated layout, read `references/project-layout.md`.
