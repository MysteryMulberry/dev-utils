import re, sys

def generate_toc(filepath, max_level=3):
    toc = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'^(#{1,6})\s+(.+)', line)
            if match:
                level = len(match.group(1))
                if level > max_level: continue
                title = match.group(2).strip()
                anchor = re.sub(r'[^a-z0-9]', '-', title.lower()).strip('-')
                indent = '  ' * (level - 1)
                toc.append(f'{indent}- [{title}](#{anchor})')
    return '\n'.join(toc)

if __name__=='__main__':
    print(generate_toc(sys.argv[1]))
