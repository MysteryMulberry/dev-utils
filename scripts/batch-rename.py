import os
import sys
import re

def batch_rename(directory, pattern, replacement, dry_run=False):
    renamed = 0
    for filename in os.listdir(directory):
        new_name = re.sub(pattern, replacement, filename)
        if new_name != filename:
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            if dry_run:
                print(f"[DRY] {filename} -> {new_name}")
            else:
                os.rename(old_path, new_path)
                print(f"{filename} -> {new_name}")
            renamed += 1
    print(f"共重命名 {renamed} 个文件")

if __name__ == '__main__':
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    pattern = sys.argv[2] if len(sys.argv) > 2 else ""
    replacement = sys.argv[3] if len(sys.argv) > 3 else ""
    dry_run = "--dry-run" in sys.argv
    batch_rename(directory, pattern, replacement, dry_run)
