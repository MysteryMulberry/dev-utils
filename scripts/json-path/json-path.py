#!/usr/bin/env python3
import json
import sys

def query(data, path):
    parts = path.strip('/').split('/')
    current = data
    for part in parts:
        if not part:
            continue
        if isinstance(current, dict):
            current = current.get(part)
        elif isinstance(current, list):
            try:
                current = current[int(part)]
            except (ValueError, IndexError):
                return None
        else:
            return None
        if current is None:
            return None
    return current

if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    path = sys.argv[2] if len(sys.argv) > 2 else "/"
    result = query(data, path)
    print(json.dumps(result, indent=2, ensure_ascii=False) if result else "null")
