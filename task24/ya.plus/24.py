s = open('24.txt').readline().strip()
a = s.split('T')
mx_line = ''
for i in range(len(a) - 100):
    line = 'T'.join(a[i:i + 101])
    if len(line) > len(mx_line):
        if line.count('U') >= 50:
            b = line.split('U')
            for j in range(len(b) - 50):
                line_b = 'U'.join(b[j:j + 51])
                if line_b.count('T') == 100 and len(line_b) > len(mx_line):
                    mx_line = line_b
print(len(mx_line))