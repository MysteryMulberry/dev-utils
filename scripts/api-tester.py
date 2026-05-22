import requests, sys, json, time

def test_endpoint(url, method='GET', headers=None, data=None, expected_status=200):
    try:
        start = time.time()
        if method.upper() == 'GET':
            r = requests.get(url, headers=headers, timeout=10)
        else:
            r = requests.post(url, headers=headers, json=data, timeout=10)
        elapsed = time.time() - start
        status = 'PASS' if r.status_code == expected_status else 'FAIL'
        print(f'[{status}] {method} {url} -> {r.status_code} ({elapsed:.2f}s)')
        return r
    except Exception as e:
        print(f'[ERROR] {method} {url} -> {e}')

if __name__=='__main__':
    test_endpoint(sys.argv[1])
