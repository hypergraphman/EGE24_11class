s = open('24.txt').readline().strip()
cur_len = 5
max_len = 5
for i in range(len(s) - 5):
    if s[i:i + 3] != s[i + 3:i + 6]:
        cur_len += 1
    else:
        cur_len = 5
    max_len = max(max_len, cur_len)
print(max_len)