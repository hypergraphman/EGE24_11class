def n_to_p(n, p):
    alf = 'авёклс'
    r = ''
    while n:
        r = alf[n % p] + r
        n //= p
    return r

print(n_to_p(594, 6))


from itertools import product

words = [''.join(word) for word in product(sorted('свекла'), repeat=5)]
for i, word in enumerate(words, start=1):
    if i == 595:
        print(i, word)