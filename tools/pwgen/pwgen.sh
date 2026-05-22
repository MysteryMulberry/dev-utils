#!/bin/bash
# 安全密码生成器
LENGTH=${1:-16}
COUNT=${2:-1}
CHARS='A-Za-z0-9!@#$%^&*'
for i in $(seq 1 "$COUNT"); do
  tr -dc "$CHARS" < /dev/urandom | head -c "$LENGTH"
  echo ""
done
