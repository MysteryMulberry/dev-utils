import sys, unicodedata

def char_info(char):
    print(f'字符: {char}')
    print(f'Unicode: U+{ord(char):04X}')
    print(f'名称: {unicodedata.name(char, "UNKNOWN")}')
    print(f'分类: {unicodedata.category(char)}')
    print(f'双向: {unicodedata.bidirectional(char)}')
    print(f'数字值: {unicodedata.numeric(char, "N/A")}')
    print(f'大写: {char.upper()} | 小写: {char.lower()}')

if __name__=='__main__':
    char = sys.argv[1] if len(sys.argv)>1 else '中'
    for c in char: char_info(c); print()
