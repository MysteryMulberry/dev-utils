import re
import sys

def test_regex(pattern, test_string, flags=0):
    matches = list(re.finditer(pattern, test_string, flags))
    if not matches:
        print("未找到匹配")
        return
    for i, match in enumerate(matches, 1):
        print(f"匹配 #{i}: '{match.group()}' (位置: {match.start()}-{match.end()})")
        if match.groups():
            for j, g in enumerate(match.groups(), 1):
                print(f"  组 {j}: '{g}'")

if __name__ == '__main__':
    pattern = sys.argv[1]
    test_str = sys.argv[2] if len(sys.argv) > 2 else input("输入测试字符串: ")
    test_regex(pattern, test_str)
