f = ''
f_2 = ''
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f += str(int(a or not a and b or not a and c))
            f_2 += str(int(a or b or c))
print(f)
print(f_2)