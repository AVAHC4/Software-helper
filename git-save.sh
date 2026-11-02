#!/bin/sh
set -eu

cd "$(dirname "$0")"

if [ -z "$(git status --porcelain)" ]; then
    echo "No changes to commit."
    exit 0
fi

echo "Changes to commit:"
git status --short
branch=$(git symbolic-ref --quiet --short HEAD) || {
    echo "Check out a branch before pushing."
    exit 1
}
git add -A
count=$(git diff --cached --name-only | wc -l | tr -d ' ')
if [ "$count" -eq 1 ]; then
    file=$(git diff --cached --name-only)
    message="Update $file"
else
    message="Update $count project files"
fi
echo "Commit message: $message"
git commit -m "$message"
git push -u origin "$branch"
