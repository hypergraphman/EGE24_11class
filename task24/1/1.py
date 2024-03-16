f = open('24.txt')
s = f.readline().strip()
cur_len = 0
max_len = 0
for c in s:
    if c == 'Y':
        cur_len += 1
    else:
        cur_len = 0
    if cur_len > max_len:
        max_len = cur_len
print(max_len)