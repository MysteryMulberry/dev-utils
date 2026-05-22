# rename-batch

批量重命名工具

## 使用方法

```bash
./rename-batch.sh [参数]
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
./rename-batch.sh

# 带参数
./rename-batch.sh --verbose
```

## 安装

```bash
chmod +x rename-batch.sh
sudo ln -s $(pwd)/rename-batch.sh /usr/local/bin/rename-batch
```

## 依赖
- bash
- 常用Linux命令行工具

---
*工具编号: #14 | 更新: 2026-05-22T05:05:36Z | 作者: MysteryMulberry*
