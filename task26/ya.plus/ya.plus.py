f = open('26.txt')
_, n = map(int, f.readline().split())
t = [0] * 1000
for _ in range(n):
    _, d, h, c = map(int, f.readline().split())
    for i in range(d * 24 + h, d * 24 + h + c):
        t[i] += 1
print(max(t), t.index(max(t)) // 24)
