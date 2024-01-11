from itertools import permutations


def f(n):
    a = [int(x1 + x2) for x1, x2 in permutations(str(n), r=2) if int(x1 + x2) > 9]
    return max(a) - min(a)


for n in range(100, 1000):
    if f(n) == 80:
        print(n)