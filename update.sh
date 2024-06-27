#!/bin/bash

# Проверяем наличие аргументов
if [ $# -lt 3 ]; then
  echo "Using: $0 <remote> <branch> <commit_message>"
  exit 1
fi

remote=$1
branch=$2
commit_message=$3

# Add the changes to the index and commit
git add .
git commit -m "$commit_message"

# $ -> select origin and 'branch' (main or delevop)
git push $remote $branch