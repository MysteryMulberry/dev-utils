#!/bin/bash
# 批量文件重命名
PATTERN="$1"
REPLACE="$2"
DIR=${3:-"."}
COUNT=0
for file in "$DIR"/*"$PATTERN"*; do
  [ -f "$file" ] || continue
  newname=$(echo "$file" | sed "s/$PATTERN/$REPLACE/g")
  mv "$file" "$newname" && ((COUNT++))
  echo "重命名: $file -> $newname"
done
echo "共重命名 $COUNT 个文件"
