def n_to_p(n, p):
    alf = '0123456789abcdefghijklmnopqrstuvwxyz'
    r = ''
    while n:
        r = alf[n % p] + r
        n //= p
    return r


# print(n_to_p(194, 5))  # 1234
# print(n_to_p(255, 16))  # ff
