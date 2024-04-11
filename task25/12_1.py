from fnmatch import fnmatch


def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


def prime_divs(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if len(divs(i)) == 2 and fnmatch(str(i), '*131*?') and '9' not in str(i):
                d.add(i)
            if len(divs(n // i)) == 2 and fnmatch(str(n // i), '*131*?') and '9' not in str(n // i):
                d.add(n // i)
    return sorted(d)


k = 7
n = 1700000
a = []
while k:
    n -= 1
    b = prime_divs(n)
    if len(b) >= 3:
        k -= 1
        a.append((n, sum(map(int, ''.join(str(el) for el in b)))))
a.sort()
print(a)