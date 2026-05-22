#!/bin/bash
# 简易API测试工具
URL="$1"
METHOD=${2:-"GET"}
TOKEN=${3:-""}

if [ -z "$URL" ]; then
  echo "Usage: api-test <url> [method] [token]"
  exit 1
fi

HEADER="-H 'Content-Type: application/json'"
if [ -n "$TOKEN" ]; then
  HEADER="$HEADER -H 'Authorization: Bearer $TOKEN'"
fi

echo "请求: $METHOD $URL"
echo "时间: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "---"
curl -s -w "\n状态码: %{http_code}\n耗时: %{time_total}s\n"   -X "$METHOD" $HEADER "$URL" | head -50
