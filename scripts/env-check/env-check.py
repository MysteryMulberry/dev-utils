#!/usr/bin/env python3
import sys
import platform

def check_environment():
    info = {
        "python": sys.version,
        "platform": platform.platform(),
        "arch": platform.architecture(),
        "cpu_count": platform.cpu_count(),
        "hostname": platform.node(),
    }
    return info

if __name__ == "__main__":
    for k, v in check_environment().items():
        print(f"{k}: {v}")
