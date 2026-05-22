#!/usr/bin/env python3
import sys
import time

class ProgressBar:
    def __init__(self, total, width=50, prefix="Progress"):
        self.total = total
        self.width = width
        self.prefix = prefix
        self.current = 0

    def update(self, current=None):
        self.current = current if current is not None else self.current + 1
        percent = self.current / self.total
        filled = int(self.width * percent)
        bar = "█" * filled + "░" * (self.width - filled)
        sys.stdout.write(f"\r{self.prefix} |{bar}| {percent:.1%} ({self.current}/{self.total})")
        sys.stdout.flush()
        if self.current >= self.total:
            print()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

if __name__ == "__main__":
    with ProgressBar(100) as p:
        for i in range(100):
            time.sleep(0.02)
            p.update()
