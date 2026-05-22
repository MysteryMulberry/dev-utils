import re, sys
from collections import Counter

def analyze_log(filepath, pattern=None):
    levels = Counter()
    ips = Counter()
    with open(filepath, 'r') as f:
        for line in f:
            for level in ['ERROR', 'WARN', 'INFO', 'DEBUG']:
                if level in line:
                    levels[level] += 1
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ips[ip_match.group(1)] += 1
    print('Log Levels:', dict(levels))
    print('Top IPs:', dict(ips.most_common(10)))

if __name__=='__main__':
    analyze_log(sys.argv[1])
