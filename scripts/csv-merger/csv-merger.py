#!/usr/bin/env python3
import csv
import sys

def merge_csv(files, output):
    all_rows = []
    headers = []
    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            if not headers:
                headers = reader.fieldnames
            for row in reader:
                all_rows.append(row)
    with open(output, 'w', newline='', encoding='utf-8') as out:
        writer = csv.DictWriter(out, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_rows)

if __name__ == "__main__":
    merge_csv(sys.argv[1:-1], sys.argv[-1])
