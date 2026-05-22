# pwgen

密码生成工具

## 使用方法

```bash
./pwgen.sh [参数]
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
./pwgen.sh

# 带参数
./pwgen.sh --verbose
```

## 安装

```bash
chmod +x pwgen.sh
sudo ln -s $(pwd)/pwgen.sh /usr/local/bin/pwgen
```

## 依赖
- bash
- 常用Linux命令行工具

---
*工具编号: #12 | 更新: 2026-05-22T05:05:27Z | 作者: MysteryMulberry*
