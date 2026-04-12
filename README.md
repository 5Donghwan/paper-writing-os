# paper-writing-os

Reusable local skills and project-state templates for paper writing workflows.

## What this repo contains

- `paper-writing-os`: the main skill for running a paper-writing workflow from local project state
- `paper-project-bootstrap`: a bootstrap skill for initializing per-paper state files and an `AGENTS.md` update snippet
- `scripts/install_local_skills.sh`: symlinks the repo's skills into `~/.agents/skills` by default

## Quick start

1. Clone or copy this repo to a stable local path.
2. Install the local skills:

```bash
./scripts/install_local_skills.sh
```

Or install them somewhere else:

```bash
./scripts/install_local_skills.sh /custom/skills/path
```

3. Bootstrap a paper project:

```bash
./scripts/bootstrap_project.sh \
  --project-dir /path/to/paper \
  --paper-name "PACT" \
  --manuscript main.tex \
  --bibliography references.bib \
  --figures-dir figures
```

4. Merge the generated `.paper-os/AGENTS.update.md` snippet into the paper project's `AGENTS.md`.
5. Use the `paper-writing-os` skill inside that paper workspace.

## Repo layout

```text
skills/
  paper-writing-os/
  paper-project-bootstrap/
scripts/
  install_local_skills.sh
```
