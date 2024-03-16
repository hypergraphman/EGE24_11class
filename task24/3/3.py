f = open('24.txt')
s = f.readline().strip()
k = 0
for c1, c2, c3, c4 in zip(s, s[1:], s[2:], s[3:]):
    if len({c1, c2, c3, c4}) == 4:
        k += 1
print(k)