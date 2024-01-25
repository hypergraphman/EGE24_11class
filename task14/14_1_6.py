from string import ascii_lowercase, digits
from collections import Counter


def n_to_p(n, p):
    r = ''
    # alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    alh = digits + ascii_lowercase
    while n:
        r = alh[n % p] + r
        n //= p
    return r


print(sum(map(int, n_to_p(5*49**5 + 3*7**8 - 7*7**4 + 100, 7))))
print(n_to_p(5*49**5 + 3*7**8 - 7*7**4 + 100, 7))
print(Counter(n_to_p(5*49**5 + 3*7**8 - 7*7**4 + 100, 7)))