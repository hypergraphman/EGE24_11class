def f(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    m = [f(s + 2, e),
         f(s + 3, e),
         f(s * 2, e)]
    return sum(m)


print(f(1, 9) * f(9, 20))