# Project Layout

Bootstrap creates a hidden `.paper-os/` directory inside the paper workspace.

This is intentional:

- it keeps project state close to the manuscript
- it makes the workflow portable across paper repos
- it avoids coupling project state to any one Codex installation

Recommended follow-up:

- keep project-specific truth in `.paper-os/`
- keep reusable logic in the shared skill repo
- merge the generated `AGENTS.update.md` content into the workspace `AGENTS.md` rather than trying to source it dynamically
