s = open('24.txt').readline().strip()
m = 0
for j in range(3):
    k = 0
    for i in range(j, len(s) - 2, 3):
        if s[i] + s[i + 2] in ('11', '33'):
            k += 1
        else:
            k = 0
        m = max(m, k)
print(m)
