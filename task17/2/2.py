a = [int(x) for x in open('17.txt')]

mn = float('inf')
for el in a:
    if abs(el) % 10 == 7 and el < mn:
        mn = el

b = []
for i in range(len(a) - 1):
    p1, p2 = a[i], a[i + 1]
    if (p1 < mn < p2 or p2 < mn < p1) and (p1 + p2) % 4 == 0:
        b.append(p1 + p2)
print(len(b), max(b))