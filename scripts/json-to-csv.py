import json, csv, sys

def json_to_csv(json_file, csv_file, key=None):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if key: data = data[key]
    if isinstance(data, dict): data = [data]
    if not data: return
    fieldnames = list(data[0].keys())
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f'Converted {len(data)} records to {csv_file}')

if __name__=='__main__':
    json_to_csv(sys.argv[1], sys.argv[2])
