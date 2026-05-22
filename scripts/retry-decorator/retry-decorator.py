#!/usr/bin/env python3
import time
import functools

def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        raise
                    print(f"第{attempt}次失败: {e}, {current_delay}s后重试...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

if __name__ == "__main__":
    @retry(max_attempts=3, delay=0.5, exceptions=(ValueError,))
    def unreliable():
        import random
        if random.random() < 0.7:
            raise ValueError("随机失败")
        return "成功"
    print(unreliable())
