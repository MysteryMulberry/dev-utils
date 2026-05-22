# sys-monitor

系统监控工具

## 使用方法

```bash
./sys-monitor.sh [参数]
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
./sys-monitor.sh

# 带参数
./sys-monitor.sh --verbose
```

## 安装

```bash
chmod +x sys-monitor.sh
sudo ln -s $(pwd)/sys-monitor.sh /usr/local/bin/sys-monitor
```

## 依赖
- bash
- 常用Linux命令行工具

---
*工具编号: #06 | 更新: 2026-05-22T05:05:01Z | 作者: MysteryMulberry*
