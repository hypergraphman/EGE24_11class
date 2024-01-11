for a in range(1, 100):
    if all(((x % a == 0) <= (x % 56 == 0)) or (x % 52 != 0) for x in range(1, 100000)):
        print(a)
        break