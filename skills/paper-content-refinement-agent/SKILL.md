---
name: paper-content-refinement-agent
description: Revise a paper against reviewer feedback without inventing new evidence. Use when integrating review comments, tightening claims, clarifying presentation, or logging revision actions from `.paper-os` state.
---

# Paper Content Refinement Agent

Use this skill for reviewer-driven revisions and rebuttal-via-revision.

## First read

1. `.paper-os/paper_os_config.yaml`
2. `.paper-os/claim_scope.md`
3. `.paper-os/evidence_log.md`
4. `.paper-os/reviewer_feedback.json`
5. `.paper-os/review_audit.json` if it exists
6. `.paper-os/worklog.json`
7. `.paper-os/writing_status.md`
8. `.paper-os/citation_map.json`

Read the manuscript path named in `paper_os_config.yaml`.

## Core rules

- Address reviewer criticism by improving the manuscript, not by drafting a
  separate response letter unless the user asks.
- Do not invent new experiments, metrics, or baselines that are absent from the
  evidence log.
- If feedback asks for unsupported new results, record the gap but do not claim
  the result exists.
- Treat reviewer/auditor findings as prompts for verification and revision, not
  as evidence by themselves.
- Preserve the paper's strengths while tightening weak sections.
- Append a concise structured record of changes to `.paper-os/worklog.json`.
- After substantial revisions, update `.paper-os/writing_status.md`.
