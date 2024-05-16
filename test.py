from fnmatch import fnmatch

k = 0
last = 0
for x in range(400000000002, 400000209323, 1):
    if x % 100 == 23 and x % 123 == 42:
        print(x)