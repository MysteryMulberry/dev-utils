#!/bin/bash
# Git批量克隆脚本
# 从仓库列表文件批量克隆Git仓库

REPO_LIST=$1
DEST_DIR=$2

if [ -z "$REPO_LIST" ] || [ -z "$DEST_DIR" ]; then
    echo "用法: $0 <仓库列表文件> <目标目录>"
    exit 1
fi

mkdir -p "$DEST_DIR"

while IFS= read -r repo; do
    if [ -n "$repo" ]; then
        echo "克隆: $repo"
        git clone "$repo" "$DEST_DIR/$(basename $repo .git)"
    fi
done < "$REPO_LIST"
