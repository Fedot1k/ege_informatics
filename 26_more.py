import math
l = []

with open('G:/fedot/P2.txt') as f:
    n = int(f.readline())
    l = [int(el) for el in f.readlines()]

more_150 = []
total = 0

for el in l:
    if el <= 150:
        total += el
    else:
        more_150.append(el)

more_150.sort()

for i in range(len(more_150) // 2):
    total += more_150[-1-i]
    total += more_150[i] * 0.8
    ans = more_150[i]
if len(more_150) % 2 == 1:
    total += more_150[len(more_150) // 2]

print(math.ceil(total), ans)