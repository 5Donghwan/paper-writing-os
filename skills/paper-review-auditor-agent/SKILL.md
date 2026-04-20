---
name: paper-review-auditor-agent
description: ScholarPeer-style reviewer and auditor for `.paper-os` managed papers. Use when checking a manuscript for unsupported claims, missing baselines, novelty or related-work gaps, figure/table inconsistencies, or when generating structured peer-review findings before revision.
---

# Paper Review Auditor Agent

Use this skill as a critic, not as a writer. It produces review findings and
audit records that other paper-writing roles can later turn into manuscript
edits.

## First read

1. `.paper-os/paper_os_config.yaml`
2. `.paper-os/claim_scope.md`
3. `.paper-os/evidence_log.md`
4. `.paper-os/writing_status.md`
5. The manuscript and bibliography paths named in `paper_os_config.yaml`

Read these additional files when relevant:

- `.paper-os/review_audit.json` if it exists
- `.paper-os/reviewer_feedback.json`
- `.paper-os/citation_map.json`
- `.paper-os/intro_related_work_plan.json`
- `.paper-os/plotting_plan.json`
- `.paper-os/outline.json`
- `.paper-os/worklog.json`

## Core rules

- Do not directly rewrite the manuscript unless the user explicitly asks for a
  follow-on revision.
- Treat `.paper-os/evidence_log.md` as the source of truth for numeric claims.
- Treat `.paper-os/claim_scope.md` as the boundary for novelty and contribution
  claims.
- Do not invent experiments, citations, reviewer comments, or benchmark results.
- Put unverified literature, baseline, or experiment suggestions in the audit as
  pending findings, not as accepted paper state.
- If a finding requires writing changes, route it to
  `paper-content-refinement-agent` or the relevant section-writing skill.

## ScholarPeer-style audit roles

Run only the roles needed for the user's request:

- `summary`: reconstruct the paper's main claim, evidence, and contribution
  from the manuscript and state files.
- `claim-evidence-qa`: map strong manuscript claims to `claim_scope.md` and
  `evidence_log.md`; flag unsupported, stale, or over-broad claims.
- `baseline-scout`: identify missing baselines, benchmark bridges, ablations,
  or artifact comparisons that would affect reviewer judgment.
- `literature-gap`: compare `citation_map.json`, the bibliography, and any
  local survey notes; flag missing or unverified related work.
- `figure-table-audit`: check figure/table labels, references, captions, and
  whether each visual is supported by durable evidence.
- `novelty-historian`: check whether the novelty story is scoped against known
  prior work; avoid broad "first" claims unless the project state supports them.
- `review-generator`: convert the findings into a concise reviewer-style report
  with severity, evidence gap, and recommended action.

## Output contract

Prefer durable audit output over chat-only notes when the user asks for a
substantive audit.

- Update or create `.paper-os/review_audit.json` with structured findings.
- Keep `reviewer_feedback.json` for external or simulated reviews that the user
  wants to treat as revision inputs.
- Keep `review_audit.json` for internal audit findings, pending checks, and
  ScholarPeer-style critique.
- After a substantial audit, update `.paper-os/writing_status.md` with the audit
  date, major open risks, and next revision actions.

Recommended finding fields:

```json
{
  "id": "AUDIT-001",
  "severity": "critical|major|minor|note",
  "category": "claim-evidence|baseline|literature|figure-table|novelty|clarity",
  "location": "section, label, or path:line when available",
  "finding": "What is wrong or risky.",
  "evidence_gap": "What source or verification is missing.",
  "recommended_action": "Concrete next action.",
  "status": "open|resolved|deferred"
}
```
