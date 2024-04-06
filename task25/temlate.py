from fnmatch import fnmatch

for i in range(2024, 10**8, 2024):
    if fnmatch(str(i), '1*555?4'):
        print(i, i // 2024)