#!/usr/bin/env python3
"""
Git 实用工具脚本
提供日常开发中常用的 Git 辅助功能。
"""
import subprocess
import sys
import os
from typing import List, Optional, Tuple

def run_git(args: List[str], cwd: Optional[str] = None) -> Tuple[int, str, str]:
    """执行 git 命令并返回 (返回码, stdout, stderr)"""
    try:
        result = subprocess.run(
            ["git"] + args,
            capture_output=True,
            text=True,
            cwd=cwd or os.getcwd()
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except FileNotFoundError:
        return -1, "", "Git is not installed or not in PATH"

def status_summary(repo_path: Optional[str] = None) -> str:
    """
    获取简洁的仓库状态摘要。
    
    Args:
        repo_path: 仓库路径，默认当前目录
    
    Returns:
        状态描述字符串
    """
    code, out, err = run_git(["status", "--short"], repo_path)
    if code != 0:
        return f"Error: {err}"
    
    if not out:
        return "Clean working tree"
    
    lines = out.split("\n")
    staged = [l for l in lines if l[0] in "MADRC"]
    unstaged = [l for l in lines if l[1] in "MD"]
    untracked = [l for l in lines if l.startswith("??")]
    
    parts = []
    if staged:
        parts.append(f"{len(staged)} staged change(s)")
    if unstaged:
        parts.append(f"{len(unstaged)} unstaged change(s)")
    if untracked:
        parts.append(f"{len(untracked)} untracked file(s)")
    
    return ", ".join(parts) if parts else "Clean working tree"

def batch_commit(repo_path: str, pattern: str, message: str) -> bool:
    """
    批量提交匹配模式的文件。
    
    Args:
        repo_path: 仓库路径
        pattern: 文件匹配模式 (如 '*.py' 或 'src/')
        message: 提交信息
    
    Returns:
        是否成功
    """
    # Stage matching files
    code, _, err = run_git(["add", pattern], repo_path)
    if code != 0:
        print(f"Failed to stage: {err}", file=sys.stderr)
        return False
    
    # Check if anything was staged
    code, out, _ = run_git(["diff", "--cached", "--name-only"], repo_path)
    if not out:
        print(f"No files matched pattern: {pattern}")
        return False
    
    # Commit
    code, _, err = run_git(["commit", "-m", message], repo_path)
    if code != 0:
        print(f"Commit failed: {err}", file=sys.stderr)
        return False
    
    print(f"Committed {len(out.split(chr(10)))} file(s)")
    return True

def list_branches(repo_path: Optional[str] = None) -> List[str]:
    """
    列出所有本地分支。
    
    Args:
        repo_path: 仓库路径，默认当前目录
    
    Returns:
        分支名称列表，当前分支前缀 '*'
    """
    code, out, err = run_git(["branch"], repo_path)
    if code != 0:
        return []
    return [b.strip() for b in out.split("\n") if b.strip()]

def cleanup_merged_branches(
    repo_path: Optional[str] = None,
    target_branch: str = "main",
    dry_run: bool = True
) -> List[str]:
    """
    清理已合并到目标分支的本地分支。
    
    Args:
        repo_path: 仓库路径
        target_branch: 目标分支名 (main / master)
        dry_run: 仅列出不删除
    
    Returns:
        被清理的分支列表
    """
    # Fetch latest
    run_git(["fetch", "--prune"], repo_path)
    
    code, out, err = run_git(
        ["branch", "--merged", target_branch],
        repo_path
    )
    if code != 0:
        print(f"Error: {err}", file=sys.stderr)
        return []
    
    branches = [b.strip().lstrip("* ") for b in out.split("\n") if b.strip()]
    # Filter out current branch and target branch
    to_delete = [b for b in branches if b not in (target_branch,)]
    
    if dry_run:
        for b in to_delete:
            print(f"  [DRY RUN] Would delete: {b}")
    else:
        for b in to_delete:
            code, _, err = run_git(["branch", "-d", b], repo_path)
            if code == 0:
                print(f"  Deleted: {b}")
            else:
                print(f"  Failed to delete {b}: {err}", file=sys.stderr)
    
    return to_delete

def commit_stats(repo_path: Optional[str] = None, author: Optional[str] = None) -> dict:
    """
    获取提交统计信息。
    
    Args:
        repo_path: 仓库路径
        author: 按作者过滤
    
    Returns:
        包含统计数据的字典
    """
    args = ["shortlog", "-sn", "--no-merges"]
    if author:
        args.extend(["--author", author])
    
    code, out, err = run_git(args, repo_path)
    if code != 0:
        return {}
    
    stats = {}
    for line in out.split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t", 1)
        if len(parts) == 2:
            stats[parts[1].strip()] = int(parts[0].strip())
    
    return stats

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python git_utils.py <command> [args]")
        print("Commands: status, branches, cleanup, stats")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "status":
        print(status_summary())
    elif cmd == "branches":
        for b in list_branches():
            print(b)
    elif cmd == "cleanup":
        dry = "--execute" not in sys.argv
        branches = cleanup_merged_branches(dry_run=dry)
        if dry and branches:
            print(f"\nAdd --execute to actually delete {len(branches)} branch(es)")
    elif cmd == "stats":
        stats = commit_stats()
        for author, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            print(f"{count:5d}  {author}")
    else:
        print(f"Unknown command: {cmd}")
