#!/usr/bin/env python3
import os
import sys
from pathlib import Path

ALIAS_FILE = Path.home() / ".custom_aliases"

def add_alias(name, command):
    aliases = load_aliases()
    aliases[name] = command
    save_aliases(aliases)
    print(f"添加别名: {name}='{command}'")

def remove_alias(name):
    aliases = load_aliases()
    if name in aliases:
        del aliases[name]
        save_aliases(aliases)
        print(f"删除别名: {name}")

def list_aliases():
    for name, cmd in load_aliases().items():
        print(f"  {name}='{cmd}'")

def load_aliases():
    result = {}
    if ALIAS_FILE.exists():
        for line in ALIAS_FILE.read_text().splitlines():
            if '=' in line and not line.startswith('#'):
                name, cmd = line.split('=', 1)
                result[name.strip()] = cmd.strip().strip("'").strip('"')
    return result

def save_aliases(aliases):
    with open(ALIAS_FILE, 'w') as f:
        for name, cmd in aliases.items():
            f.write(f"{name}='{cmd}'\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        list_aliases()
    elif sys.argv[1] == "add":
        add_alias(sys.argv[2], ' '.join(sys.argv[3:]))
    elif sys.argv[1] == "remove":
        remove_alias(sys.argv[2])
