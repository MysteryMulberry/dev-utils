# npm-check

NPM依赖检查工具

## 使用方法

```bash
./npm-check.sh [参数]
```

## 功能列表

| 参数 | 功能 |
|------|------|
| help | 显示帮助信息 |
| -v | 详细输出模式 |
| -q | 安静模式 |

## 示例

```bash
# 基本用法
./npm-check.sh

# 带参数
./npm-check.sh --verbose
```

## 安装

```bash
chmod +x npm-check.sh
sudo ln -s $(pwd)/npm-check.sh /usr/local/bin/npm-check
```

## 依赖
- bash
- 常用Linux命令行工具

---
*工具编号: #03 | 更新: 2026-05-22T05:04:48Z | 作者: MysteryMulberry*
