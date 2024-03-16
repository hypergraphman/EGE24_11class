s = open('24.txt').readline().strip()
z = [0]
for i in range(1, len(s) - 1):
    if s[i - 1:i + 2] == '131':
        z.append(i)
z.append(len(s) - 1)
m = 0
for i in range(len(z) - 132):
    m = max(z[i + 132] - z[i] + 1, m)
print(m)