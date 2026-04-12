---
name: paper-plotting-agent
description: Plan or refine paper figures and captions. Use when deciding which figures to include, mapping figures to evidence, refining captions, or checking figure-to-text consistency from `.paper-os` state.
---

# Paper Plotting Agent

Use this skill for figure planning, caption writing, and visual consistency
checks.

## First read

1. `.paper-os/paper_os_config.yaml`
2. `.paper-os/evidence_log.md`
3. `.paper-os/plotting_plan.json`
4. `.paper-os/writing_status.md`

Read the manuscript and figures paths named in `paper_os_config.yaml` when
captions or references need to be checked against existing content.

## Core rules

- Every figure must map to a concrete claim or explanatory need.
- Do not infer results that are not visible in the figure or present in the
  evidence log.
- Use exact figure filenames when editing manuscript references.
- Caption text should not include `Figure X`.
- Prefer refining `plotting_plan.json` first, then update manuscript captions or
  figure references if the task calls for it.
- After substantial changes, update `.paper-os/writing_status.md`.
