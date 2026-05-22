import subprocess, sys, re
from collections import Counter

def git_stats(repo_path='.'):
    r = subprocess.run(['git', 'log', '--format=%an', '--all'], capture_output=True, text=True, cwd=repo_path)
    authors = Counter(r.stdout.strip().split('\n'))
    r2 = subprocess.run(['git', 'log', '--oneline', '--all'], capture_output=True, text=True, cwd=repo_path)
    total = len(r2.stdout.strip().split('\n'))
    print(f'Total commits: {total}')
    for author, count in authors.most_common(10):
        print(f'  {author}: {count} ({count/total*100:.1f}%)')

if __name__=='__main__': git_stats(sys.argv[1] if len(sys.argv)>1 else '.')
