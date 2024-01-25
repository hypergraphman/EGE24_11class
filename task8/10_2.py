from itertools import permutations

words = [''.join(word) for word in permutations('alina', r=5)]
a = set()
for word in words:
    if 'aa' not in word:
        a.add(word)
print(len(a))