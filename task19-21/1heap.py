def f(s, c, m, ban):
    if s >= 141:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = []
    if ban[0] == 0:
        moves.append(f(s + 1, c + 1, m, [1, 0]))
    if ban[1] == 0:
        moves.append(f(s * 2, c + 1, m, [0, 1]))
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 140 + 1):
    for m in range(1, 4 + 1):
        if f(s, 0, m, [0, 0]):
            print(s, m)
            break
