#!/usr/bin/env python3
import time
from collections import OrderedDict
from threading import Lock

class TTLCache:
    def __init__(self, maxsize=128, ttl=300):
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = OrderedDict()
        self.lock = Lock()

    def get(self, key):
        with self.lock:
            if key in self.cache:
                value, ts = self.cache[key]
                if time.time() - ts < self.ttl:
                    self.cache.move_to_end(key)
                    return value
                del self.cache[key]
        return None

    def set(self, key, value):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
            elif len(self.cache) >= self.maxsize:
                self.cache.popitem(last=False)
            self.cache[key] = (value, time.time())

    def clear(self):
        with self.lock:
            self.cache.clear()

if __name__ == "__main__":
    cache = TTLCache(maxsize=10, ttl=5)
    cache.set("key1", "value1")
    print(cache.get("key1"))
