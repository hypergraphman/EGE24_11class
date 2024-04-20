with open('26.txt') as f:
    n, v, *data = map(int, f.read().split())
data.sort()
s = 0
a = []
for el in data:
    if 170 <= el <= 180:
        s += el
    else:
        a.append(el)
k = n - len(a)
g = []
while sum(g) + s + a[0] <= v:
    g.append(a.pop(0))
k += len(g)
print(k)
i = len(a)
j = len(g) - 1
while i != -1 and j != -1:
    a.insert(0, g.pop(j))
    j -= 1
    while i != -1 and sum(g) + s + a[i] > v:
        i -= 1
    if i != -1:
        g.append(a.pop(i))
print(sum(g) + s)