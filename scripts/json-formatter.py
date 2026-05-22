import json
import sys

def format_json(filepath, indent=2):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python json-formatter.py <文件路径> [缩进空格数]")
        sys.exit(1)
    indent = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    format_json(sys.argv[1], indent)
