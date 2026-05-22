#!/usr/bin/env python3
import re
import sys

def search_in_file(pattern, filepath, ignore_case=True):
    flags = re.IGNORECASE if ignore_case else 0
    results = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if re.search(pattern, line, flags):
                results.append((i, line.rstrip()))
    return results

if __name__ == "__main__":
    results = search_in_file(sys.argv[1], sys.argv[2])
    for line_no, line in results:
        print(f"{line_no}: {line}")
