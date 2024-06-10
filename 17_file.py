file = open('G:/fedot/5.txt') #создание файла
s = [int(x) for x in file]

c = 0
res = []

for i in range(len(s) - 1):
    n1 = s[i]
    n2 = s[i+1]
    l1 = n1 % 10
    l2 = n2 % 10
    pro = abs(n1) * abs(n2)
    
    if (l1 % 2 != 0) and (l2 % 2 != 0) and (l1 != l2):
        c += 1
        res.append(pro)

print(c, min(res))