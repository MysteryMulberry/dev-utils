#!/bin/bash
# 系统资源监控脚本
echo "===== 系统监控 ====="
echo "时间: $(date)"
echo ""
echo "--- CPU ---"
top -bn1 | head -5
echo ""
echo "--- 内存 ---"
free -h 2>/dev/null || vm_stat
echo ""
echo "--- 磁盘 ---"
df -h 2>/dev/null | head -10
echo ""
echo "--- 网络 ---"
netstat -tlnp 2>/dev/null | head -10 || ss -tlnp | head -10
