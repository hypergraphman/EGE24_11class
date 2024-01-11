from string import ascii_lowercase, digits


def n_to_p(n, p):
    r = ''
    # alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    alh = digits + ascii_lowercase
    while n:
        r = alh[n % p] + r
        n //= p
    return r


print(n_to_p(255, 16))