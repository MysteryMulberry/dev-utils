#!/usr/bin/env python3
from urllib.parse import quote, unquote
import sys

if __name__ == "__main__":
    if sys.argv[1] == "encode":
        print(quote(sys.argv[2]))
    elif sys.argv[1] == "decode":
        print(unquote(sys.argv[2]))
