#!/usr/bin/env python3
import json, sys

def format_json_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Formatted: {path}")

if __name__ == '__main__':
    for p in sys.argv[1:]:
        format_json_file(p)
