#!/usr/bin/env python3
import os
import time
import sys
from pathlib import Path

def watch(path, interval=1.0):
    snapshots = {}
    for f in Path(path).rglob('*'):
        if f.is_file():
            try:
                snapshots[f] = f.stat().st_mtime
            except OSError:
                pass

    print(f"监控中: {path} ({len(snapshots)} 个文件)")
    while True:
        time.sleep(interval)
        for f in Path(path).rglob('*'):
            if f.is_file():
                try:
                    mtime = f.stat().st_mtime
                    if f not in snapshots:
                        print(f"[新增] {f}")
                        snapshots[f] = mtime
                    elif mtime != snapshots[f]:
                        print(f"[修改] {f}")
                        snapshots[f] = mtime
                except OSError:
                    pass

if __name__ == "__main__":
    watch(sys.argv[1] if len(sys.argv) > 1 else ".")
