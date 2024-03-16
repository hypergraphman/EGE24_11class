s = open('24.txt').readline().strip()
t = set(['1' + x + '1' for x in '0123456789'] +
        ['3' + x + '3' for x in '0123456789'])
m = 0
for j in range(3):
    k = 0
    for i in range(j, len(s) - 2, 3):
        if s[i] + s[i + 1] + s[i + 2] in t:
            k += 1
        else:
            k = 0
        m = max(m, k)
print(m)
