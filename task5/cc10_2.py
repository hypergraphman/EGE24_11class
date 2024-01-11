def f(n):
    d1, d2, d3, d4, d5 = map(int, str(n))
    return ''.join(map(str, sorted([d1 + d3 + d5, d2 + d4])))


print(f(13885))
for n in range(10000, 100000):
    if f(n) == '321':
        print(n)