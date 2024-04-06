def f(c, e, k):
    if k > 7 or c > e:
        return 0
    if c == e:
        return 1
    s = 0
    if (c + 1) % 2 == 0:
        s += f(c + 1, e, k + 1)
    else:
        s += f(c + 1, e, k)
    if (c * 2) % 2 == 0:
        s += f(c * 2, e, k + 1)
    else:
        s += f(c * 2, e, k)
    if (c * 3) % 2 == 0:
        s += f(c * 3, e, k + 1)
    else:
        s += f(c * 3, e, k)
    return s


print(f(1, 131, 0))