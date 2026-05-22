#!/usr/bin/env python3
import time
from collections import defaultdict
from threading import Lock

class RateLimiter:
    def __init__(self, max_calls=10, period=60):
        self.max_calls = max_calls
        self.period = period
        self.calls = defaultdict(list)
        self.lock = Lock()

    def allow(self, key="default"):
        now = time.time()
        with self.lock:
            self.calls[key] = [t for t in self.calls[key] if now - t < self.period]
            if len(self.calls[key]) < self.max_calls:
                self.calls[key].append(now)
                return True
            return False

    def wait(self, key="default"):
        while not self.allow(key):
            time.sleep(0.1)

if __name__ == "__main__":
    limiter = RateLimiter(max_calls=5, period=10)
    for i in range(10):
        if limiter.allow():
            print(f"请求 {i+1}: 允许")
        else:
            print(f"请求 {i+1}: 被限流")
