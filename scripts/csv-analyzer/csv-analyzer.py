#!/usr/bin/env python3
import csv
import sys
from collections import Counter

def analyze(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"行数: {len(rows)}")
    print(f"列数: {len(rows[0]) if rows else 0}")
    if rows:
        print(f"列名: {list(rows[0].keys())}")

    for col in rows[0].keys() if rows else []:
        values = [r[col] for r in rows if r[col]]
        try:
            nums = [float(v) for v in values]
            print(f"\n{col}: min={min(nums)}, max={max(nums)}, avg={sum(nums)/len(nums):.2f}")
        except ValueError:
            print(f"\n{col}: {len(set(values))} unique values")

if __name__ == "__main__":
    analyze(sys.argv[1])
