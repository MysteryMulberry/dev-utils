# backup-tool

文件备份工具

## 使用方法

```bash
./backup-tool.sh [参数]
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
./backup-tool.sh

# 带参数
./backup-tool.sh --verbose
```

## 安装

```bash
chmod +x backup-tool.sh
sudo ln -s $(pwd)/backup-tool.sh /usr/local/bin/backup-tool
```

## 依赖
- bash
- 常用Linux命令行工具

---
*工具编号: #05 | 更新: 2026-05-22T05:04:56Z | 作者: MysteryMulberry*
