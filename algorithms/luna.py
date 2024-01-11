def is_luna(n):
    t = str(n)[::-1]
    # s1 = sum(map(int, t[::2]))
    s1 = 0
    for x in t[::2]:
        s1 += int(x)
    print(s1)
    s2 = 0
    # s2 = sum(map(lambda x: (int(x) * 2 % 10 + int(x) * 2 // 10) if int(x)*2 > 9 else int(x) * 2, t[1::2]))
    for x in t[1::2]:
        s = int(x) * 2
        if s * 2 > 9:
            s2 += s % 10 + s // 10
        else:
            s2 += s
    print(s2)
    return (s1 + s2) % 10 == 0


print(is_luna(4096830803098323))
