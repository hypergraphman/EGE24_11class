from collections import defaultdict

data = defaultdict(list)
with open('26.txt') as f:
    p, n = map(int, f.readline().split())
    for _ in range(n):
        id, mark = map(int, f.readline().split())
        data[id].append(mark * 100)

mx_id = None
mx_d = -float('inf')
mn_avg = float('inf')
for id in data:
    marks = sorted(data[id])
    x = len(marks) * p // 100
    if x > 0:
        marks = marks[x:-x]
    avg = sum(marks) / len(marks)
    if len(marks) % 2:
        med = marks[len(marks) // 2]
    else:
        med = (marks[len(marks) // 2] + marks[len(marks) // 2 - 1]) / 2
    if avg < mn_avg:
        mn_avg = avg
    if abs(avg - med) > mx_d:
        mx_d = abs(avg - med)
        mx_id = id
    elif abs(avg - med) == mx_d and id > mx_id:
        mx_id = id
print(int(mn_avg), mx_id)