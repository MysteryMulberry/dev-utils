import sys, re
from collections import Counter

def analyze(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    chars = len(text)
    words = len(text.split())
    lines = text.count('\n') + 1
    cn_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    word_freq = Counter(text.lower().split()).most_common(20)
    print(f'字符数: {chars}')
    print(f'词数: {words}')
    print(f'行数: {lines}')
    print(f'中文字符: {cn_chars}')
    print(f'高频词: {word_freq[:10]}')

if __name__=='__main__': analyze(sys.argv[1])
