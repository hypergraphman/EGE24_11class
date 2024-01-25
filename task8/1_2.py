from itertools import product

words = [''.join(word) for word in product(sorted('лицей'), repeat=4)]
print(len(words))