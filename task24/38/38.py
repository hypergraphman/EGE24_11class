def is_ke(s):
    for i in range(len(s) - 3):
        if s[i] + s[i + 3] == 'KE':
            return True
    return False


f = open('24.txt')
k = 0
for line in f:
    if is_ke(line):
        k += 1
print(k)