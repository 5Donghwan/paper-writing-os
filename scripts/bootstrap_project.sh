#!/usr/bin/env zsh

set -euo pipefail

script_dir=${0:A:h}
repo_root=${script_dir:h}

python3 "${repo_root}/skills/paper-project-bootstrap/scripts/init_paper_project.py" "$@"
