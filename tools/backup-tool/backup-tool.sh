#!/bin/bash
# 简易文件备份工具
BACKUP_DIR="$HOME/.backups"
mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

for file in "$@"; do
  if [ -f "$file" ]; then
    base=$(basename "$file")
    cp "$file" "$BACKUP_DIR/${base}.${TIMESTAMP}"
    echo "已备份: ${base} -> ${base}.${TIMESTAMP}"
  else
    echo "跳过(不存在): $file"
  fi
done
echo "备份目录: $BACKUP_DIR"
ls -lt "$BACKUP_DIR" | head -10
