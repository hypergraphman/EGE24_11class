def f(c, e, k):
    if k > 7 or c > e:
        return 0
    if c == e:
        return 1
    m = [f(c + 1, e, k + ((c + 1) + 1) % 2),
         f(c * 2, e, k + ((c * 2) + 1) % 2),
         f(c * 3, e, k + ((c * 3) + 1) % 2)]
    return sum(m)


print(f(1, 131, 0))