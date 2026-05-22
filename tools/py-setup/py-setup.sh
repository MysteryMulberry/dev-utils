#!/bin/bash
# Python项目环境快速设置
PROJECT=${1:-"."}
mkdir -p "$PROJECT"/{src,tests,docs,configs}
cat > "$PROJECT/requirements.txt" << EOF
# 自动生成 - $(date +%Y-%m-%d)
pytest>=7.0
black>=23.0
flake8>=6.0
mypy>=1.0
EOF
cat > "$PROJECT/pyproject.toml" << EOF
[tool.black]
line-length = 88

[tool.isort]
profile = "black"

[tool.mypy]
strict = true
EOF
echo "项目结构已创建: $PROJECT"
