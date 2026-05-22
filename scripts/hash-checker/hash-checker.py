#!/usr/bin/env python3
import hashlib
import sys

def file_hash(filepath, algorithm="sha256"):
    h = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    print(file_hash(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "sha256"))
