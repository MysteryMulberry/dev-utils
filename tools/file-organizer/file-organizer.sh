#!/bin/bash
# 按扩展名整理文件到子目录
TARGET=${1:-"."}
cd "$TARGET" || exit 1

for file in *; do
  [ -f "$file" ] || continue
  ext="${file##*.}"
  [ "$ext" = "$file" ] && ext="other"
  mkdir -p "$ext"
  mv "$file" "$ext/" 2>/dev/null
  echo "移动: $file -> $ext/"
done
echo "整理完成"
