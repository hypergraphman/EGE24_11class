f = open('26.txt')
n = int(f.readline())
a = []
for _ in range(n):
    u, d = map(int, f.readline().split())
    a.append((u, u - 2 * d - 3))
a.sort(key=lambda x: -x[1])
# print(a)
b = [a[0]]
for el in a[1:]:
    if el[0] <= b[-1][1]:
        b.append(el)
print(len(b))
mx = 0
for el in a:
    if b[-2][1] >= el[0]:
        mx = max(mx, el[0])
print(mx)