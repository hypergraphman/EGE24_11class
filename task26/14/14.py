f = open('26.txt')
n = int(f.readline())
a = []
for _ in range(n):
    a.append(tuple(map(int, f.readline().split())))
a.sort(key=lambda x: (x[1], x[0]))
# print(a)
b = [a[0]]
for el in a[1:]:
    if el[0] >= b[-1][1]:
        b.append(el)
print(len(b))
for el in a[::-1]:
    if b[-2][1] <= el[0]:
        print(el[1])
        break