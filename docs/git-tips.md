# Git实用技巧

## 常用命令

### 分支操作
- 创建并切换分支: `git checkout -b <branch>`
- 删除分支: `git branch -d <branch>`
- 合并分支: `git merge <branch>`

### 撤销操作
- 撤销暂存: `git reset HEAD <file>`
- 撤销提交: `git reset --soft HEAD~1`
- 撤销修改: `git checkout -- <file>`

### 查看信息
- 查看日志: `git log --oneline --graph`
- 查看差异: `git diff <branch1> <branch2>`
- 查看状态: `git status -s`

## 高级技巧

### 交互式变基
git rebase -i HEAD~3

### 暂存修改
git stash save "message"
git stash pop

### Cherry-pick
git cherry-pick <commit-hash>
