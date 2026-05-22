#!/bin/bash
# 命令行快速笔记
NOTES_DIR="$HOME/.quicknotes"
mkdir -p "$NOTES_DIR"
case "$1" in
  "add") echo "[$(date)] $2" >> "$NOTES_DIR/notes.txt" && echo "已记录" ;;
  "show") cat "$NOTES_DIR/notes.txt" 2>/dev/null || echo "暂无笔记" ;;
  "search") grep -i "$2" "$NOTES_DIR/notes.txt" 2>/dev/null || echo "未找到" ;;
  "clear") > "$NOTES_DIR/notes.txt" && echo "已清空" ;;
  *) echo "Usage: notes {add|show|search|clear}" ;;
esac
