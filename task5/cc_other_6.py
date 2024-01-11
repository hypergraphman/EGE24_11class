def n_to_p(n, p):
    a = []
    while n:
        a.insert(0, n % p)
        n //= p
    return a


def dop(num):
    s0, s1 = 0, 0
    for el in num:
        if el % 2:
            s1 += el
        else:
            s0 += el
    s = max(s1, s0)
    num.append(s % 80)


def f(n):
    num = n_to_p(n, 80)
    dop(num)
    dop(num)
    res = 0
    k = 0
    for el in num[::-1]:
        res += el * 80**k
        k += 1
    return res

print(f(83))