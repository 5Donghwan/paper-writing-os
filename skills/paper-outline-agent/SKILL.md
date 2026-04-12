---
name: paper-outline-agent
description: Plan a research paper before drafting. Use when defining manuscript structure, intro framing, related-work search clusters, figure plans, or section sizing from `.paper-os` state.
---

# Paper Outline Agent

Use this skill to build or revise the paper plan before prose-heavy drafting.

## First read

1. `.paper-os/paper_os_config.yaml`
2. `.paper-os/claim_scope.md`
3. `.paper-os/evidence_log.md`
4. `.paper-os/writing_status.md`

Read the manuscript path named in `paper_os_config.yaml` when existing section
structure matters.

## Primary outputs

Update these files as needed:

- `.paper-os/outline.json`
- `.paper-os/intro_related_work_plan.json`
- `.paper-os/plotting_plan.json`

## Core rules

- Separate Introduction from Related Work.
  Introduction should frame macro context and the scoped problem gap.
  Related Work should group micro-level technical competitors or adjacent
  approaches.
- Do not plan claims, experiments, or figures unsupported by
  `.paper-os/evidence_log.md`.
- Keep subsection hierarchy clean. If a numbered subsection family exists, do
  not leave orphaned siblings.
- Record figure intent and evidence source explicitly in `plotting_plan.json`.
- After updating the plan, record the new next steps in
  `.paper-os/writing_status.md`.
