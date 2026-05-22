# Git工作流对比

## Git Flow
- main: 生产分支
- develop: 开发分支
- feature/*: 功能分支
- release/*: 发布分支
- hotfix/*: 热修复分支

## GitHub Flow
- main: 始终可部署
- feature: 短命功能分支
- PR合并回main

## Trunk-Based
- 主干开发，短命分支
- 特性开关(Feature Flag)
- 频繁集成(CI)

## 选择建议
| 场景 | 推荐 |
|------|------|
| 开源项目 | GitHub Flow |
| 版本发布 | Git Flow |
| 持续部署 | Trunk-Based |
