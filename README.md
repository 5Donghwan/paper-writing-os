# paper-writing-os

Reusable local skills and project-state templates for paper writing workflows.

## Design note

This repo was designed after reviewing *PaperOrchestra: A Multi-Agent
Framework for Automated AI Research Paper Writing*, a Google Cloud AI Research
paper. The main public reference used here is the authors' project page:

- [PaperOrchestra project page](https://yiwen-song.github.io/paper_orchestra/)

The implementation here does not copy that paper's prompts verbatim. Instead,
it adapts the Appendix F role split into a reusable local-skill architecture:

- shared workflow logic lives in installable skills
- per-paper memory lives in project-local `.paper-os/` state files
- long-lived workspace rules are surfaced through a generated `AGENTS.md`
  update snippet

The structure is intentionally inspired by the paper's reported results: the
multi-agent PaperOrchestra pipeline beat its Single Agent baseline by large
margins on literature-review quality and overall paper quality, so this repo
now mirrors that role split instead of keeping only one generic writing agent.

More specifically, the author page describes a pipeline in which specialized
agents handle outline planning, literature discovery, plotting, section
writing, and iterative refinement. This repo reuses that decomposition idea,
but implements it as local installable skills plus project-local `.paper-os/`
state.

## What this repo contains

- `paper-writing-os`: the orchestration skill for running a paper-writing workflow from local project state
- `paper-project-bootstrap`: a bootstrap skill for initializing per-paper state files and an `AGENTS.md` update snippet
- `paper-outline-agent`: planning skill for section structure, literature-search plan, and figure plan
- `paper-plotting-agent`: figure planning and caption refinement skill
- `paper-literature-review-agent`: intro and related-work writing skill
- `paper-section-writing-agent`: core manuscript drafting skill for non-intro sections
- `paper-content-refinement-agent`: reviewer-driven revision skill
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
  --paper-name "Your Paper Name" \
  --manuscript main.tex \
  --bibliography references.bib \
  --figures-dir figures
```

Replace `"Your Paper Name"` with the actual paper or project name for that
workspace.

4. Merge the generated `.paper-os/AGENTS.update.md` snippet into the paper project's `AGENTS.md`.
5. Use the role-specific skills as needed:

```text
paper-outline-agent
paper-plotting-agent
paper-literature-review-agent
paper-section-writing-agent
paper-content-refinement-agent
```

6. Use `paper-writing-os` when you want one orchestration layer to choose the
next role from `.paper-os` state.

## Repo layout

```text
skills/
  paper-content-refinement-agent/
  paper-literature-review-agent/
  paper-outline-agent/
  paper-writing-os/
  paper-project-bootstrap/
  paper-plotting-agent/
  paper-section-writing-agent/
scripts/
  install_local_skills.sh
```
