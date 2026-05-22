import csv
import sys

def merge_csv(files, output, key_column):
    merged = {}
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row[key_column]
                if key in merged:
                    merged[key].update(row)
                else:
                    merged[key] = dict(row)
    
    if merged:
        fieldnames = []
        for data in merged.values():
            for k in data.keys():
                if k not in fieldnames:
                    fieldnames.append(k)
        with open(output, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(merged.values())

if __name__ == '__main__':
    merge_csv(sys.argv[1:-2], sys.argv[-1], sys.argv[-2])
