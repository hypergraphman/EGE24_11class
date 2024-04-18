def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


a = []
for i in range(101, 10**5):
    if len(divs(i)) == 2:
        n = i**2
        s = str(n)
        if s[0] + s[-3] + s[-1] == '139' and len(divs(sum(divs(n)))) == 2:
            a.append((n, i))
a.sort()
for n, i in a:
    print(n, i, sep='\t')