from itertools import product

words = [''.join(word) for word in product('01234567', repeat=5)]
k = 0
for word in words:
    t = word.replace('3', '1').replace('5', '1').replace('7', '1')
    if word[0] != '0' and word.count('6') == 2 and '16' not in t and '61' not in t:
        k += 1
print(k)