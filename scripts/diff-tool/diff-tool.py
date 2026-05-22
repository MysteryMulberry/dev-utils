#!/usr/bin/env python3
import difflib
import sys

def compare_files(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        diff = difflib.unified_diff(f1.readlines(), f2.readlines(),
                                     fromfile=file1, tofile=file2)
    return ''.join(diff)

if __name__ == "__main__":
    print(compare_files(sys.argv[1], sys.argv[2]))
