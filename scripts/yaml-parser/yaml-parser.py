#!/usr/bin/env python3
import json
import sys

def parse_yaml_simple(text):
    result = {}
    current_section = result
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if not value:
                current_section[key] = {}
                current_section = current_section[key]
            else:
                if value.lower() in ('true', 'false'):
                    value = value.lower() == 'true'
                elif value.isdigit():
                    value = int(value)
                current_section[key] = value
    return result

if __name__ == "__main__":
    import sys
    data = sys.stdin.read() if not sys.argv[1:] else open(sys.argv[1]).read()
    print(json.dumps(parse_yaml_simple(data), indent=2))
