#!/bin/bash
# 多服务健康检查
SERVICES=("$@")
[ $# -eq 0 ] && SERVICES=("http://localhost:8080" "http://localhost:3000")
for svc in "${SERVICES[@]}"; do
  CODE=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 "$svc")
  STATUS="✅ OK" ; [ "$CODE" -ge 400 ] 2>/dev/null && STATUS="❌ FAIL"
  echo "$svc -> HTTP $CODE $STATUS"
done
