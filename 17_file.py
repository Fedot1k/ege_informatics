file = open('G:/fedot/2.txt') #создание файла
s = [int(x) for x in file]


# решение задачи ↓↓↓


m = sorted(s)[-3]


res = []
count = 0
for i in range(len(s) - 2):
    n1 = s[i]
    n2 = s[i+1]
    n3 = s[i+2]
    count = 0

    if n1%2==0:
        count += 1
    if n2%2==0:
        count += 1
    if n3%2==0:
        count += 1

    if count <= 2:
        to = n1 + n2 + n3
        if to <= m:
            res.append(to)


print(len(res), max(res))