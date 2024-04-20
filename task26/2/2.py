from collections import defaultdict


def h(a):
    avg = sum(a) / len(a)
    if len(a) % 2:
        med = a[len(a) // 2]
    else:
        med = sum(a[len(a) // 2 - 1:len(a) // 2 + 1]) // 2
    return avg, abs(avg - med)


data = defaultdict(list)
with open('26.txt') as f:
    p, n = map(int, f.readline().split())
    for _ in range(n):
        key, mark = map(int, f.readline().split())
        data[key].append(mark * 100)

for key in data:
    data[key].sort()
    x = int(len(data[key]) * p / 100)
    if x > 0:
        data[key] = data[key][x:-x]

min_avg = float('inf')
max_d = 0
max_id = None
for key in sorted(data.keys()):
    avg, d = h(data[key])
    if avg < min_avg:
        min_avg = avg
    if d >= max_d:
        max_d = d
        max_id = key
print(int(min_avg), max_id)