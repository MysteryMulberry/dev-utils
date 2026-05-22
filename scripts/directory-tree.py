import os
import sys

def print_tree(directory, prefix="", max_depth=5, current_depth=0):
    if current_depth >= max_depth:
        return
    items = sorted(os.listdir(directory))
    dirs = [i for i in items if os.path.isdir(os.path.join(directory, i))]
    files = [i for i in items if os.path.isfile(os.path.join(directory, i))]
    
    for i, d in enumerate(dirs):
        is_last_dir = (i == len(dirs) - 1) and len(files) == 0
        connector = "└── " if is_last_dir else "├── "
        print(f"{prefix}{connector}{d}/")
        extension = "    " if is_last_dir else "│   "
        print_tree(os.path.join(directory, d), prefix + extension, max_depth, current_depth + 1)
    
    for i, f in enumerate(files):
        connector = "└── " if i == len(files) - 1 else "├── "
        print(f"{prefix}{connector}{f}")

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"{os.path.basename(path)}/")
    print_tree(path)
