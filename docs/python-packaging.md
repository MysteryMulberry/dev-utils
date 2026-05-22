# Python打包发布

## 项目结构
```
myproject/
  src/myproject/
  pyproject.toml
  README.md
```

## pyproject.toml
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myproject"
version = "0.1.0"
```

## 命令
- 构建: `python -m build`
- 发布: `twine upload dist/*`
- 本地测试: `pip install -e .`

## 工具对比
| 工具 | 速度 | 特点 |
|------|------|------|
| hatch | 快 | 现代推荐 |
| setuptools | 慢 | 传统兼容 |
| poetry | 中 | 依赖管理强 |
