#!/usr/bin/env python3
from datetime import datetime, timezone
import sys

def convert(timestamp, fmt="iso"):
    dt = datetime.fromtimestamp(float(timestamp), tz=timezone.utc)
    if fmt == "iso":
        return dt.isoformat()
    elif fmt == "readable":
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    return str(dt)

if __name__ == "__main__":
    print(convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "iso"))
