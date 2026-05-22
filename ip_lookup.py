#!/usr/bin/env python3
import urllib.request, json, sys

def ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?lang=zh-CN"
    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read().decode())
    return f"""IP: {data.get('query','')}
国家: {data.get('country','')} | {data.get('countryCode','')}
地区: {data.get('regionName','')}
城市: {data.get('city','')}
ISP: {data.get('isp','')}
经纬度: {data.get('lat','')}, {data.get('lon','')}"""

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else ''
    print(ip_info(target))
