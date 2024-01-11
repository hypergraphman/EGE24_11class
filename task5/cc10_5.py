def f(n):
    # s1 = sum(filter(lambda x: x % 2 == 0, map(int, str(n))))
    s1 = sum(int(x) for x in str(n) if int(x) % 2 == 0)
    s2 = sum(int(x) for x in str(n)[1::2])
    return abs(s1 - s2)


for n in range(100, 900000000):
    if f(n) == 17:
        print(n)
        break