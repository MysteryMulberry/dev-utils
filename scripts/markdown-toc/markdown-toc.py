#!/usr/bin/env python3
import re
import sys

def generate_toc(text, max_level=3):
    toc = []
    for line in text.split('\n'):
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            if level > max_level:
                continue
            title = match.group(2).strip()
            anchor = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff-]', '-', title.lower())
            anchor = re.sub(r'-+', '-', anchor).strip('-')
            indent = '  ' * (level - 1)
            toc.append(f"{indent}- [{title}](#{anchor})")
    return '\n'.join(toc)

if __name__ == "__main__":
    data = sys.stdin.read() if not sys.argv[1:] else open(sys.argv[1]).read()
    print(generate_toc(data))
