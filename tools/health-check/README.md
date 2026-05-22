# health-check

服务健康检查工具

## 使用方法

```bash
./health-check.sh [参数]
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
./health-check.sh

# 带参数
./health-check.sh --verbose
```

## 安装

```bash
chmod +x health-check.sh
sudo ln -s $(pwd)/health-check.sh /usr/local/bin/health-check
```

## 依赖
- bash
- 常用Linux命令行工具

---
*工具编号: #15 | 更新: 2026-05-22T05:05:40Z | 作者: MysteryMulberry*
