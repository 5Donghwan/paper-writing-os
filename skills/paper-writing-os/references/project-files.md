# Project Files

Expected `.paper-os/` files:

- `paper_os_config.yaml`
  - stable project metadata and file locations
- `claim_scope.md`
  - strongest claim, non-claims, positioning constraints
- `evidence_log.md`
  - measured results, source paths, stale/pending flags
- `outline.json`
  - section structure, ownership, and drafting status for the main body
- `intro_related_work_plan.json`
  - intro hook, problem gap, related-work clusters, and search plan
- `plotting_plan.json`
  - figure inventory, purpose, source path, and caption status
- `illustration_plan.json`
  - generation-specific state for explicit image synthesis requests, including
    style guidance, prompt drafts, review status, and output paths
- `citation_map.json`
  - related-work buckets, must-cite items, cutoff rules
- `reviewer_feedback.json`
  - structured reviewer comments and revision targets
- `review_audit.json`
  - internal reviewer/auditor findings, missing-baseline checks, claim-evidence
    gaps, and pending literature verification
- `worklog.json`
  - structured history of revision actions
- `writing_status.md`
  - active phase, last completed work, next edits, open risks
- `AGENTS.update.md`
  - snippet to merge into the paper workspace `AGENTS.md`

Only treat a file as authoritative if it exists. If a file is missing, either bootstrap the project or ask the user whether to create it.
