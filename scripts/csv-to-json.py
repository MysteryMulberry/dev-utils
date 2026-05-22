import csv, json, sys

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'Converted {len(data)} rows to {json_file}')

if __name__=='__main__': csv_to_json(sys.argv[1], sys.argv[2])
