#!/bin/sh
set -eu

cd "$(dirname "$0")"

if [ -z "$(git status --porcelain)" ]; then
    echo "No changes to commit."
    exit 0
fi

echo "Changes to commit:"
git status --short
printf 'Describe your changes for the commit message: '
IFS= read -r message
if [ -z "$message" ]; then
    echo "A commit message is required."
    exit 1
fi
branch=$(git symbolic-ref --quiet --short HEAD) || {
    echo "Check out a branch before pushing."
    exit 1
}
git add -A
git commit -m "$message"
git push -u origin "$branch"
