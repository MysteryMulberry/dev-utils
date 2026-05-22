#!/bin/bash
# NPM依赖分析和更新工具
echo "=== 过时依赖 ==="
npm outdated 2>/dev/null || echo "无过时依赖"
echo ""
echo "=== 依赖树概览 ==="
npm ls --depth=0 2>/dev/null
echo ""
echo "=== 安全审计 ==="
npm audit --production 2>/dev/null | head -20
