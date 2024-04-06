def f(st, fin, k):
    global a
    if st > fin or k > 12:
        return 0
    if st == fin:
        a.append(k)
        return 1
    m = [f(st + 1, fin, k + 1),
         f(st + 2, fin, k + 1),
         f(st * 2, fin, k + 1)]
    return sum(m)


a = []
print(f(1, 500, 0))
print(a.count(min(a)))