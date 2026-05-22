# npm实用技巧

## 速度优化
- 换源: `npm config set registry https://registry.npmmirror.com`
- 加速: `npm i --prefer-offline`

## 依赖管理
- 查看过时: `npm outdated`
- 安全审计: `npm audit`
- 交互更新: `npx npm-check -u`
- 查看体积: `npx npm-check -s`

## 脚本技巧
- 并行: `npm-run-all --parallel dev:*`
- 前后钩子: `prestart` / `postbuild`
- 环境变量: `cross-env NODE_ENV=prod`

## 锁定依赖
- 使用package-lock.json
- `npm ci` 严格安装(比install快)
