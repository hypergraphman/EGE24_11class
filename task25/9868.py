from functools import lru_cache


@lru_cache(None)
def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


for i in range(2*10**6):
    for d in range(10):
        s = f'{i}3{d}9'
        n = int(s)
        if s[0] == '1' and len(divs(sum(divs(n)))) == 2:
            print(n, divs(n)[-2])