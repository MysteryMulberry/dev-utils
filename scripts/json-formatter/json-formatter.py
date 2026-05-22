#!/usr/bin/env python3
import json
import sys

def format_json(input_str, indent=2):
    try:
        parsed = json.loads(input_str)
        return json.dumps(parsed, indent=indent, ensure_ascii=False)
    except json.JSONDecodeError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    data = sys.stdin.read() if not sys.argv[1:] else open(sys.argv[1]).read()
    print(format_json(data))
