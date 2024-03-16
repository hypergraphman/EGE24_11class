from itertools import product

words = [''.join(word) for word in product(sorted('снегурочка'), repeat=5)]
k = 0
for i, word in enumerate(words, start=1):
    if 'ручка' <= word <= 'чукча':
        k += 1
print(k)