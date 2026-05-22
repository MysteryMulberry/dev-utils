#!/usr/bin/env python3
# Dev Utils - Daily Update 2026-05-22

import os, sys, platform, datetime

def banner():
    print("=== Dev Utils v1.0 (Updated: 2026-05-22) ===")

def sys_info():
    return {
        "hostname": platform.node(),
        "system": platform.system(),
        "release": platform.release(),
        "python": platform.python_version(),
        "time": datetime.datetime.now().isoformat()
    }

def main():
    banner()
    for k, v in sys_info().items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
