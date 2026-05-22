# CI/CD快速指南

## GitHub Actions
```yaml
name: CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install -r requirements.txt
      - run: pytest
```

## 常用模式
- PR检查: lint + test
- 发布: tag触发build+deploy
- 定时: cron触发清理/报告

## 缓存优化
- pip: `actions/cache` + ~/.cache/pip
- npm: `actions/cache` + ~/.npm
- Docker: `docker/build-push-action`层缓存
