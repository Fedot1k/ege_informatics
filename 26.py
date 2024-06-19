l = []

with open('26-9.txt') as f:
    n, m, k = map(int, f.readline().split())
    for el in f:
        l.append(list(map(int, el.split())))
l.sort(key=lambda x: (x[0], x[1]))
print(l[:10])
print(l[-1])
max_dist = 0

for i in range(1, len(l)):
    flag = True
    free = 0
    seat = l[i][1]
    r = l[i][0]
    for j in range(i-1, -1, -1):
        if l[j][1] == seat:
            free = r - l[j][0] - 1
            flag = False
            break
    if flag:
        free = r - 1
    if free > max_dist:
        max_dist = free
        ans = r
print(ans - 1, max_dist-1)