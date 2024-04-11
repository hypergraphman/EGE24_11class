def f(s, e, k):
    global a
    if s > e or k > 15:
        return 0
    if s == e:
        a.append(k)
        return 1
    m = [f(s + 1, e, k + 1),
         f(s + 2, e, k + 1),
         f(s * 2, e, k + 1)]
    return sum(m)


a = []
f(1, 35, 0)
print(a.count(min(a)))