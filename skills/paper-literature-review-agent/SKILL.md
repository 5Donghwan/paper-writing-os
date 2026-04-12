---
name: paper-literature-review-agent
description: Write or revise only the Introduction and Related Work of a paper. Use when the task is literature synthesis, problem framing, positioning, or bibliography-grounded intro/rw revision from `.paper-os` state.
---

# Paper Literature Review Agent

Use this skill only for the Introduction and Related Work sections.

## First read

1. `.paper-os/paper_os_config.yaml`
2. `.paper-os/claim_scope.md`
3. `.paper-os/evidence_log.md`
4. `.paper-os/intro_related_work_plan.json`
5. `.paper-os/citation_map.json`
6. `.paper-os/writing_status.md`

Read the manuscript and bibliography paths named in `paper_os_config.yaml`.

## Core rules

- Do not rewrite unrelated sections unless the user explicitly asks.
- Keep the introduction focused on broad context and the scoped problem gap.
- Keep related work focused on grouped technical comparison and positioning.
- Do not claim superiority over papers that are not actually evaluated in the
  evidence log.
- Use only citation keys that exist in the bibliography or citation map unless
  the user explicitly asks for bibliography expansion.
- After substantial revisions, update `.paper-os/writing_status.md`.
