a = [int(x) for x in open('17.txt')]

s = 0
k = 0
for el in a:
    s += el
    k += 1
avg = s / k


b = []
for p1, p2 in zip(a, a[1:]):
    if (p1 < avg or p2 < avg) and abs(p1 + p2) % 100 == 13:
        b.append(p1 + p2)
print(len(b), min(b))