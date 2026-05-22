#!/usr/bin/env python3
import base64
import sys

def encode(data):
    return base64.b64encode(data.encode()).decode()

def decode(data):
    return base64.b64decode(data.encode()).decode()

if __name__ == "__main__":
    if sys.argv[1] == "encode":
        print(encode(sys.argv[2]))
    elif sys.argv[1] == "decode":
        print(decode(sys.argv[2]))
