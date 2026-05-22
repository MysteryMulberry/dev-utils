#!/usr/bin/env python3
import requests
import sys
import json

def make_request(method, url, **kwargs):
    methods = {
        'get': requests.get,
        'post': requests.post,
        'put': requests.put,
        'delete': requests.delete,
    }
    resp = methods[method](url, timeout=30, **kwargs)
    print(f"Status: {resp.status_code}")
    print(f"Headers: {dict(resp.headers)}")
    try:
        print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
    except:
        print(resp.text[:500])

if __name__ == "__main__":
    method = sys.argv[1] if len(sys.argv) > 1 else 'get'
    url = sys.argv[2] if len(sys.argv) > 2 else 'https://httpbin.org/get'
    make_request(method, url)
