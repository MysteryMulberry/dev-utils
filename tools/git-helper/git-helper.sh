#!/bin/bash
# Git辅助工具 - 快速操作集合
case "$1" in
  "undo") git reset --soft HEAD~1 ;;
  "amend") git commit --amend --no-edit ;;
  "stash-pop") git stash pop ;;
  "branch-clean") git branch --merged | grep -v '\*\|main\|master' | xargs -n 1 git branch -d ;;
  "log-pretty") git log --graph --oneline --decorate --all ;;
  *) echo "Usage: git-helper {undo|amend|stash-pop|branch-clean|log-pretty}" ;;
esac
