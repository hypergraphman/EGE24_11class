from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10**6)


@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    return n * f(n - 1)


print(f(49) // f(47))