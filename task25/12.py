from fnmatch import fnmatch


def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


def prime_divs(n):
    d = divs(n)
    pd = []
    for i in d:
        if len(divs(i)) == 2:
            pd.append(i)
    return pd


k = 7
n = 1700000
a = []
while k:
    n -= 1
    b = prime_divs(n)
    if len(b) >= 3 and fnmatch(str(n), '*131*?') and '9' not in str(n):
        k -= 1
        a.append((n, sum(map(int, ''.join(str(el) for el in b)))))
a.sort()
for p1, p2 in a:
    print(p1, p2, sep='\t')
