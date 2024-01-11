from string import ascii_lowercase, digits


def n_to_p(n, p):
    t = ''
    a = digits + ascii_lowercase
    while n:
        d = a[n % p]
        t = d + t
        n //= p
    return t


print(n_to_p(255, 16))
print(n_to_p(194, 5))
