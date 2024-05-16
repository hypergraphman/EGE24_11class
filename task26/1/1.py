with open('26.txt') as f:
    v, n = map(int, f.readline().split())
    *data, = map(int, f)

data.sort()
k = 0
for i in range(len(data)):
    if v - data[i] >= 0:
        k += 1
        v -= data[i]

print(k)
v += data[k - 1]
mx = 0
for i in range(k, len(data)):
    if v - data[i] >= 0:
        mx = data[i]
print(mx)