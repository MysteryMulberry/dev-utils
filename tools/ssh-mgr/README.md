# ssh-mgr

SSH管理工具

## 使用方法

```bash
./ssh-mgr.sh [参数]
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
./ssh-mgr.sh

# 带参数
./ssh-mgr.sh --verbose
```

## 安装

```bash
chmod +x ssh-mgr.sh
sudo ln -s $(pwd)/ssh-mgr.sh /usr/local/bin/ssh-mgr
```

## 依赖
- bash
- 常用Linux命令行工具

---
*工具编号: #04 | 更新: 2026-05-22T05:04:52Z | 作者: MysteryMulberry*
