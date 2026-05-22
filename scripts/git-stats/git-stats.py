#!/usr/bin/env python3
import subprocess
import sys
from collections import Counter

def git_stats():
    cmd = ["git", "log", "--format=%an|%aI", "--all"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Not a git repository")
        return

    authors = Counter()
    by_month = Counter()
    for line in result.stdout.strip().split('\n'):
        if '|' in line:
            author, date = line.split('|', 1)
            authors[author] += 1
            month = date[:7]
            by_month[month] += 1

    print("=== 作者贡献排行 ===")
    for author, count in authors.most_common(10):
        print(f"  {author}: {count} commits")

    print("\n=== 月度趋势 ===")
    for month in sorted(by_month.keys())[-12:]:
        bar = '█' * min(by_month[month] // 5, 40)
        print(f"  {month}: {bar} ({by_month[month]})")

if __name__ == "__main__":
    git_stats()
