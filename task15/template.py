for a in range(-100, 1000):
    is_a = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = ((x <= 60) <= (x <= a)) and ((y * y <= a) <= (y <= 8))
            if not f:
                is_a = False
    if is_a:
        print(a)
