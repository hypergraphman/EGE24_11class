f = open('26.txt')
n = int(f.readline())
line = []
for _ in range(n):
    s, e = map(int, f.readline().split())
    line.extend([s, -e])
line.sort(reverse=True)
line.sort(key=lambda x: abs(x))

pick = [1]
for el in line[1:]:
    pick.append(pick[-1] + (1 if el > 0 else -1))
print(line)
print(pick)
mx = max(pick)
print(pick.count(mx), mx)
print(pick.index(644))
print(line[880:899])