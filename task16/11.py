from sys import setrecursionlimit

setrecursionlimit(5000)


def f(n):
    if n == 0:
        return 1
    return f(n - 1) * n


print(f(2025) // f(2023))