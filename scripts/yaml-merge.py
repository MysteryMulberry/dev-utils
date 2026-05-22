import yaml, sys, json

def merge_yaml(files, output):
    result = {}
    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            data = yaml.safe_load(fh)
            if data: result.update(data)
    with open(output, 'w', encoding='utf-8') as fh:
        yaml.dump(result, fh, allow_unicode=True, default_flow_style=False)
    print(f'Merged {len(files)} files -> {output}')

if __name__=='__main__':
    merge_yaml(sys.argv[1:-1], sys.argv[-1])
