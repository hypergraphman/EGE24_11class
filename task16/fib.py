from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f(n - 1) + f(n - 2)


for i in range(600):
    f(i)

print(f(600))