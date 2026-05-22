#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"},
    "docs": {".pdf", ".doc", ".docx", ".txt", ".md", ".xls"},
    "videos": {".mp4", ".avi", ".mkv", ".mov"},
    "audio": {".mp3", ".wav", ".flac", ".aac"},
    "archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "code": {".py", ".js", ".ts", ".java", ".cpp", ".go"},
}

def organize(directory):
    for f in Path(directory).iterdir():
        if f.is_file():
            cat = "other"
            for c, exts in CATEGORIES.items():
                if f.suffix.lower() in exts:
                    cat = c
                    break
            dest = Path(directory) / cat
            dest.mkdir(exist_ok=True)
            shutil.move(str(f), str(dest / f.name))

if __name__ == "__main__":
    import sys
    organize(sys.argv[1] if len(sys.argv) > 1 else ".")
