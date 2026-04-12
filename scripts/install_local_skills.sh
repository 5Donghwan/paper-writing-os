#!/bin/zsh
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
target_root="${1:-${SKILLS_HOME:-$HOME/.agents/skills}}"

mkdir -p "$target_root"

for skill_dir in "$repo_root"/skills/*; do
  skill_name="$(basename "$skill_dir")"
  ln -sfn "$skill_dir" "$target_root/$skill_name"
  echo "linked $skill_name -> $target_root/$skill_name"
done

echo "Local skills installed. Restart your agent client if needed."
