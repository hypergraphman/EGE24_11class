def step(n, m):
    return n // m if n % m == 0 else n - 1


def f(n):
    s1 = step(n, 3)
    s2 = step(s1, 5)
    s3 = step(s2, 7)
    return s3


a = []
for n in range(1, 1000):
    if f(n) == 1:
        a.append(n)
print(len(a), a)