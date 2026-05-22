#!/usr/bin/env python3
import re
from collections import Counter

def parse_log(filepath, pattern=r'ERROR|WARN|INFO'):
    counter = Counter()
    with open(filepath, 'r') as f:
        for line in f:
            for match in re.findall(pattern, line):
                counter[match] += 1
    return counter

if __name__ == "__main__":
    import sys
    result = parse_log(sys.argv[1])
    for level, count in result.most_common():
        print(f"{level}: {count}")
