for a in range(1, 1000):
    if all((x % 44 == 0) or ((x % a == 0) <= (x % 77 == 0)) for x in range(1, 1000)):
        print(a)
        break