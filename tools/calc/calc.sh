#!/bin/bash
# 增强命令行计算器
case "$1" in
  "hex") printf "0x%X\n" "$2" ;;
  "bin") echo "obase=2;$2" | bc ;;
  "oct") echo "obase=8;$2" | bc ;;
  "rgb") printf "#%02X%02X%02X\n" "$2" "$3" "$4" ;;
  "ts") date -d @"$2" 2>/dev/null || python3 -c "import datetime;print(datetime.datetime.fromtimestamp($2))" ;;
  *) echo "$@" | bc -l 2>/dev/null || echo "Usage: calc {hex|bin|oct|rgb|ts|expression}" ;;
esac
