"""Math utility functions."""
import math
from typing import List, Tuple

def gcd_list(numbers: List[int]) -> int:
    result = numbers[0]
    for n in numbers[1:]:
        result = math.gcd(result, n)
    return result

def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)

def prime_factors(n: int) -> List[int]:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def moving_average(data: List[float], window: int) -> List[float]:
    result = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        result.append(avg)
    return result
