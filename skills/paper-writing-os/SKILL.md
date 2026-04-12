---
name: paper-writing-os
description: Reusable operating workflow for managing a research paper from local project state files. Use when a paper workspace has a `.paper-os/` directory and the task involves outlining, literature review, drafting, figure/table planning, reviewer-response refinement, or claim/evidence alignment.
---

# Paper Writing OS

Use this skill when a paper project is managed through local `.paper-os/` state.

## First read

Before substantive work, read:

1. `.paper-os/paper_os_config.yaml`
2. `.paper-os/claim_scope.md`
3. `.paper-os/writing_status.md`

Read these additional files when the task touches them:

- numbers, tables, results, or benchmark claims:
  `.paper-os/evidence_log.md`
- citations, related work, or bibliography hygiene:
  `.paper-os/citation_map.json`
- reviewer comments or revision planning:
  `.paper-os/reviewer_feedback.json`
- structure or section ownership:
  `.paper-os/outline.json`

For the workflow and file semantics, read:

- `references/workflow.md`
- `references/project-files.md`

## Core rules

- Treat `.paper-os/evidence_log.md` as the source of truth for numeric claims unless the user explicitly overrides it with newer evidence.
- Do not invent experiments, metrics, citations, or reviewer feedback.
- Keep the paper's strongest claim inside the boundary documented in `.paper-os/claim_scope.md`.
- Before editing the manuscript, map the requested change to the relevant state files so the write is grounded in project context.
- After substantial work, update `.paper-os/writing_status.md` with completed work, open risks, and next actions.

## Operating loop

1. Scope alignment
2. Evidence alignment
3. Outline or section planning
4. Draft or revise target sections
5. Check figures, tables, and citations
6. Record status and residual risks

## Output preference

- Prefer minimal, durable updates to project state over ad hoc prose hidden in chat.
- When a project-level rule should persist, put it in `.paper-os/` rather than only saying it.
