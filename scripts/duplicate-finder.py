import os, sys, hashlib
from collections import defaultdict

def find_duplicates(directory):
    size_map = defaultdict(list)
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            try: size_map[os.path.getsize(path)].append(path)
            except: pass
    dupes = 0
    for size, paths in size_map.items():
        if len(paths) > 1:
            hashes = defaultdict(list)
            for p in paths:
                h = hashlib.md5(open(p,'rb').read()).hexdigest()
                hashes[h].append(p)
            for h, ps in hashes.items():
                if len(ps) > 1:
                    dupes += 1
                    print(f'Duplicate ({size} bytes):')
                    for p in ps: print(f'  {p}')
    print(f'Found {dupes} duplicate sets')

if __name__=='__main__': find_duplicates(sys.argv[1] if len(sys.argv)>1 else '.')
