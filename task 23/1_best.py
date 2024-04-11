def f(s, e):
    if s > e or s == 12:
        return 0
    if s == e:
        return 1
    m = [f(s + 1, e),
         f(s * 2, e),
         f(s * 3, e)]
    return sum(m)


print(f(1, 70) * f(70, 150))