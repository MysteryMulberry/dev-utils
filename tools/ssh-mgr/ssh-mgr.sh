#!/bin/bash
# SSH连接管理工具
CONFIG="$HOME/.ssh/config"
case "$1" in
  "list") grep "^Host " "$CONFIG" | awk '{print $2}' ;;
  "add") echo -e "Host $2\n  HostName $3\n  User $4" >> "$CONFIG" ;;
  "del") sed -i "/^Host $2$/,/^Host /{/^Host $2$/d}" "$CONFIG" ;;
  "test") ssh -o ConnectTimeout=5 "$2" "echo OK" 2>/dev/null || echo "FAIL" ;;
  *) echo "Usage: ssh-mgr {list|add|del|test}" ;;
esac
