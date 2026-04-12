---
name: paper-section-writing-agent
description: Draft or revise the main body of a paper outside Introduction and Related Work. Use when writing Method, Experiments, Discussion, Conclusion, Appendix, tables, or figure references from `.paper-os` state.
---

# Paper Section Writing Agent

Use this skill for the main manuscript body outside Introduction and Related
Work.

## First read

1. `.paper-os/paper_os_config.yaml`
2. `.paper-os/claim_scope.md`
3. `.paper-os/evidence_log.md`
4. `.paper-os/outline.json`
5. `.paper-os/citation_map.json`
6. `.paper-os/plotting_plan.json`
7. `.paper-os/writing_status.md`

Read the manuscript path named in `paper_os_config.yaml`.

## Core rules

- Preserve existing filled sections unless the user requests a broader rewrite.
- Draw numeric values only from `.paper-os/evidence_log.md` or the cited result
  paths listed there.
- Use exact citation keys from the bibliography or citation map.
- Use exact figure filenames and keep figures/tables before the conclusion
  unless the paper style requires otherwise.
- Add math only when it is supported by the actual method description and
  evidence.
- After substantial revisions, update `.paper-os/writing_status.md`.
