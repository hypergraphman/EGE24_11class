from itertools import product
k = 0
last = 0
for x, y, z, w in product('0123456789', repeat=4):
    n = int(f'4{x}8{y}15{z}16{w}23')
    if n % 123 == 42:
        k += 1
        last = n
print(k, last)