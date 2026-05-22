#!/usr/bin/env python3
import sys

def generate_table(headers, rows):
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join([header_line, separator] + body)

if __name__ == "__main__":
    print(generate_table(["Name", "Value"], [["key1", "val1"]]))
