#!/usr/bin/env python3
import os

def generate_tree(path, prefix="", max_depth=3, depth=0):
    if depth >= max_depth:
        return
    items = sorted(os.listdir(path))
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{item}")
        full = os.path.join(path, item)
        if os.path.isdir(full):
            ext = "    " if is_last else "│   "
            generate_tree(full, prefix + ext, max_depth, depth + 1)

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(path)
    generate_tree(path)
