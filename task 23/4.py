def f(s, e, cmds):
    if s > e:
        return 0
    if s == e:
        if cmds[-2] in '23':
            return 1
        else:
            return 0

    m = [f(s + 1, e, cmds + '1'),
         f(s * 2, e, cmds + '2'),
         f(s * 3, e, cmds + '3')]

    return sum(m)


print(f(1, 28, ''))
