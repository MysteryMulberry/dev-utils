#!/usr/bin/env python3
import sys
import re
from collections import Counter

def text_stats(text):
    chars = len(text)
    words = len(text.split())
    lines = text.count('\n') + 1
    sentences = len(re.findall(r'[.!?]+', text))

    word_freq = Counter(text.lower().split())

    print(f"字符数: {chars}")
    print(f"单词数: {words}")
    print(f"行数: {lines}")
    print(f"句数: {sentences}")
    print(f"\n高频词 (Top 10):")
    for word, count in word_freq.most_common(10):
        if len(word) > 2:
            print(f"  {word}: {count}")

if __name__ == "__main__":
    data = sys.stdin.read() if not sys.argv[1:] else open(sys.argv[1], encoding='utf-8').read()
    text_stats(data)
