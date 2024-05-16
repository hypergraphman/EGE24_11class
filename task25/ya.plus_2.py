from fnmatch import fnmatch

k = 0
last = 0
for x in range(4*10**11 + 2, 5*10**11, 123):
    if fnmatch(str(x), '4?8?15?16?23'):
        k += 1
        last = x
        print(k)
print(k, last)