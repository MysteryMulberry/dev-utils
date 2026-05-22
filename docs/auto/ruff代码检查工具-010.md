# Ruff代码检查工具

## 配置 pyproject.toml
```toml
[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "UP", "B", "SIM"]
ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
```

## 使用
```bash
ruff check .              # 检查
ruff check --fix .        # 自动修复
ruff format .             # 格式化
ruff check --select I .   # 仅检查import排序
```

## 与pre-commit集成
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    hooks:
      - id: ruff
      - id: ruff-format
```

---
*编号: #010 | 更新时间: 2026-05-22T05:52:22Z | 仓库: dev-utils*
