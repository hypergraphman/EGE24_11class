for a in range(1, 1000):
    if all(((x & 71 != 0) <= ((x & 47 == 0) <= (x & a != 0))) for x in range(1, 1000)):
        print(a)
        break