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

The repo now also includes a ScholarPeer-style reviewer/auditor subsystem,
inspired by *ScholarPeer: A Collaborative Multi-Agent System for Automated
Scientific Peer Review*:

- [ScholarPeer arXiv page](https://arxiv.org/html/2601.22638v1)

This subsystem is intentionally separated from the writer loop. It audits
claims, baselines, literature coverage, figures, tables, and novelty framing,
then records structured findings for the refinement agent to address. It does
not directly upgrade claims, add citations, or rewrite the manuscript without a
follow-on writing step.

The repo also supports a split between figure planning and figure generation.
`paper-plotting-agent` remains planning-only: it decides what to draw, why the
visual is needed, and how the caption should align with the manuscript.
When a user explicitly asks for "image_gen" or "그림 생성", a separate
`paperbanana-illustration-agent` can take the existing plan and use Codex's
image generation tool to produce methodology-style illustrations without
changing the default behavior of the plotting workflow.

This optional illustration-generation path is inspired by *PaperBanana:
Automating Academic Illustration for AI Scientists*:

- [PaperBanana project page](https://papersbanana.com/)
- [PaperBanana arXiv paper](https://arxiv.org/abs/2601.23265)

As with the rest of this repo, the implementation here does not copy the
paper's prompts verbatim. Instead, it adapts the reported workflow shape into a
local-skill split that keeps figure planning separate from explicit image
generation.

## What this repo contains

- `paper-writing-os`: the orchestration skill for running a paper-writing workflow from local project state
- `paper-project-bootstrap`: a bootstrap skill for initializing per-paper state files and an `AGENTS.md` update snippet
- `paper-outline-agent`: planning skill for section structure, literature-search plan, and figure plan
- `paper-plotting-agent`: figure planning and caption refinement skill
- `paperbanana-illustration-agent`: explicit image-generation skill for methodology-style figures using Codex `image_gen`
- `paper-literature-review-agent`: intro and related-work writing skill
- `paper-section-writing-agent`: core manuscript drafting skill for non-intro sections
- `paper-review-auditor-agent`: ScholarPeer-style audit skill for claims, baselines, literature gaps, and reviewer-style findings
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
paperbanana-illustration-agent
paper-literature-review-agent
paper-section-writing-agent
paper-review-auditor-agent
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
  paperbanana-illustration-agent/
  paper-writing-os/
  paper-project-bootstrap/
  paper-plotting-agent/
  paper-review-auditor-agent/
  paper-section-writing-agent/
scripts/
  install_local_skills.sh
```
