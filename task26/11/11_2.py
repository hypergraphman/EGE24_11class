with open('26.txt') as f:
    f.readline()
    data = []
    for line in f:
        out_d, width = map(int, line.split())
        in_d = out_d - 2 * width
        data.append((out_d, in_d))
data.sort(key=lambda x: -x[1])
p = [data[0][1]]
for out_d, in_d in data:
    if out_d <= p[-1] - 3:
        p.append(in_d)
print(len(p))
mx = 0
for out_d, _ in data:
    if out_d <= p[-2] - 3:
        mx = max(mx, out_d)
print(mx)
