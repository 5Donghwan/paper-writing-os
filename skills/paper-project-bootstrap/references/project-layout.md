# Project Layout

Bootstrap creates a hidden `.paper-os/` directory inside the paper workspace.

This is intentional:

- it keeps project state close to the manuscript
- it makes the workflow portable across paper repos
- it avoids coupling project state to any one Codex installation

Recommended follow-up:

- keep project-specific truth in `.paper-os/`
- split role-specific planning across `outline.json`,
  `intro_related_work_plan.json`, `plotting_plan.json`,
  `illustration_plan.json`, `review_audit.json`, and `worklog.json`
- keep internal reviewer/auditor findings in `review_audit.json`, separate
  from verified evidence and external reviewer feedback
- keep reusable logic in the shared skill repo
- merge the generated `AGENTS.update.md` content into the workspace `AGENTS.md` rather than trying to source it dynamically
