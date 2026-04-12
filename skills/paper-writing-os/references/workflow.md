# Workflow

`paper-writing-os` treats a paper workspace as a small state machine backed by local files.

## Recommended stages

1. `scope`
   - confirm the paper's main claim
   - list explicit non-claims
   - record venue and positioning constraints
2. `evidence`
   - capture the measured results, tables, and source files
   - note whether each claim is current, stale, or pending rerun
3. `outline`
   - map the narrative arc section by section
   - assign each section a purpose and evidence dependency
   - split the planning state across `outline.json`,
     `intro_related_work_plan.json`, and `plotting_plan.json`
4. `literature`
   - write or revise Introduction and Related Work from the dedicated plan
5. `drafting`
   - write or revise sections against the outline and evidence log
6. `figures`
   - plan or update figures, captions, and figure references
7. `refinement`
   - respond to reviewer comments
   - tighten claims, caveats, and related work
   - record revision actions in `worklog.json`

## Minimal discipline

- Never update the manuscript first and explain the reasoning later. Update the state files when the reasoning should persist.
- If a requested revision changes the paper's strongest claim, update `claim_scope.md` before touching the manuscript.
- If a numeric statement changes, update `evidence_log.md` before or alongside the manuscript.
