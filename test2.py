from fnmatch import fnmatch

k = 0
last = 0
for x in range(400000003323, 5*10**11, 12300):
    if fnmatch(str(x), '4?8?15?16?23'):
        k += 1
        last = x
        print(k)
print(k, last)