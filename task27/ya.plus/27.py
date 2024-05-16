from itertools import product

f = open('27_A.txt')
n = int(f.readline())
data = []
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    data.append((a, b, c))

stack = []
for i in range(n):