---
name: paperbanana-illustration-agent
description: Generate methodology-style paper figures from `.paper-os` state when the user explicitly asks for image generation or `image_gen`.
---

# PaperBanana Illustration Agent

Use this skill only when the user explicitly asks for `"그림 생성"` or
`image_gen`, or clearly wants a generated methodology-style figure rather than
planning alone.

## First read

1. `.paper-os/paper_os_config.yaml`
2. `.paper-os/evidence_log.md`
3. `.paper-os/plotting_plan.json`
4. `.paper-os/illustration_plan.json`
5. `.paper-os/writing_status.md`

Read the manuscript and figures paths named in `paper_os_config.yaml` when the
generated figure needs to align with existing captions, terminology, or style.

## Core rules

- Treat `plotting_plan.json` as the source for what to draw and why the figure
  matters. Treat `illustration_plan.json` as the execution layer for generation
  prompts, style notes, review status, and output paths.
- Prefer methodology diagrams, pipeline overviews, concept schematics, and
  explanatory visuals over numeric plots.
- Do not invent metrics, benchmark outcomes, ablation results, or unsupported
  visual claims.
- If a figure depends on exact numeric accuracy, prefer a conventional plotting
  workflow unless the user explicitly accepts image-generation tradeoffs.
- Use Codex `image_gen` only when the current environment supports it; otherwise
  leave a prompt-ready plan in `illustration_plan.json` without pretending the
  figure was generated.
- Keep generated outputs under the paper workspace figures directory, ideally
  under a dedicated subdirectory such as `figures/generated/`.
- After substantial work, update `.paper-os/illustration_plan.json` and
  `.paper-os/writing_status.md`.

## Suggested operating loop

1. Reconstruct the target figure from `plotting_plan.json`, manuscript text,
   and caption context.
2. Extract or draft a visual style guide in `illustration_plan.json`.
3. Draft a generation prompt and a short negative prompt.
4. Run `image_gen` if explicitly requested and available.
5. Compare the generated output against the manuscript and caption intent.
6. Revise the prompt or notes if another pass is needed.

## Output preference

- Prefer durable updates to `illustration_plan.json` over chat-only prompt
  drafts.
- Record any known fidelity caveat, such as approximate geometry or
  text-legibility limits, in `notes`.
