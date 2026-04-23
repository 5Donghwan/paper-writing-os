#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize .paper-os state files for a paper workspace."
    )
    parser.add_argument("--project-dir", required=True, help="Paper workspace path")
    parser.add_argument("--paper-name", required=True, help="Paper or project name")
    parser.add_argument("--manuscript", default="main.tex", help="Primary manuscript path")
    parser.add_argument("--bibliography", default="references.bib", help="Bibliography path")
    parser.add_argument("--figures-dir", default="figures", help="Figures directory")
    parser.add_argument("--state-dir", default=".paper-os", help="State directory name")
    parser.add_argument("--venue", default="", help="Target venue")
    parser.add_argument("--field", default="computer-science", help="Research field")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    return parser.parse_args()


def render_template(text: str, values: dict[str, str]) -> str:
    rendered = text
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered


def main() -> int:
    args = parse_args()

    script_dir = Path(__file__).resolve().parent
    template_dir = script_dir.parent / "assets" / "project-state"

    project_dir = Path(args.project_dir).expanduser().resolve()
    state_dir = project_dir / args.state_dir
    state_dir.mkdir(parents=True, exist_ok=True)

    values = {
        "PAPER_NAME": args.paper_name,
        "PROJECT_DIR": str(project_dir),
        "MANUSCRIPT": args.manuscript,
        "BIBLIOGRAPHY": args.bibliography,
        "FIGURES_DIR": args.figures_dir,
        "STATE_DIR": args.state_dir,
        "VENUE": args.venue,
        "FIELD": args.field,
        "TODAY": date.today().isoformat(),
    }

    created: list[str] = []
    skipped: list[str] = []

    for template_path in sorted(template_dir.glob("*.tmpl")):
        output_name = template_path.name[:-5]
        output_path = state_dir / output_name
        if output_path.exists() and not args.force:
            skipped.append(str(output_path))
            continue
        content = render_template(template_path.read_text(encoding="utf-8"), values)
        output_path.write_text(content, encoding="utf-8")
        created.append(str(output_path))

    print("Initialized paper-writing state")
    print(f"project_dir: {project_dir}")
    print(f"state_dir: {state_dir}")
    if created:
        print("created:")
        for path in created:
            print(f"  - {path}")
    if skipped:
        print("skipped (already exists):")
        for path in skipped:
            print(f"  - {path}")

    print("next_steps:")
    print("  1. Fill in claim_scope.md and evidence_log.md")
    print("  2. Merge .paper-os/AGENTS.update.md into the project AGENTS.md")
    print("  3. Keep plotting_plan.json for figure planning and illustration_plan.json for explicit generated figures")
    print("  4. Use the paper-writing-os skill in that workspace")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
