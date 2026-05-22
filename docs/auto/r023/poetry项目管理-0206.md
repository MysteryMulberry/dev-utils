# Poetry项目管理

## 初始化项目
```bash
poetry new myproject
poetry init
```

## 依赖管理
```bash
poetry add requests
poetry add pytest --group dev
poetry remove requests
poetry install
```

## pyproject.toml
```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.31"

[tool.poetry.group.dev.dependencies]
pytest = "^8.0"
ruff = "^0.4"
```

## 构建与发布
```bash
poetry build
poetry publish
```

---
*编号: R023-#0206 | 更新时间: 2026-05-22T07:33:13Z | 仓库: dev-utils*
