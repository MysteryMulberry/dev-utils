#!/usr/bin/env python3
import sys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

if __name__ == "__main__":
    if sys.argv[1] == "hex2rgb":
        print(hex_to_rgb(sys.argv[2]))
    elif sys.argv[1] == "rgb2hex":
        print(rgb_to_hex(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))
