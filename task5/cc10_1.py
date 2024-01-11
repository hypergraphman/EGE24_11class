def f(n):
    # d1, d2, d3 = map(int, str(n))
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    p1 = d1 + d2
    p2 = d3 + d2
    a = sorted([p1, p2], reverse=True)
    res = str(a[0]) + str(a[1])
    return res
    # return ''.join(map(str, sorted([d1 + d2, d2 + d3])[::-1]))


for n in range(100, 1000):
    if f(n) == '145':
        print(n)