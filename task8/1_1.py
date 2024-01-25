from itertools import product

words = [''.join(word) for word in product(sorted('снегурочка'), repeat=5)]
for i, word in enumerate(words, start=1):
    if word == 'ручка' or word == 'чукча':
        print(i, word)