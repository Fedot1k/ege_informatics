s = open('C:/Users/rasma/Downloads/P9.txt').readline()

res = []

for i in range(len(s)-2):
    if s[i+1] == s[i+2]:
        res.append(s[i])

print(res.count('S'))
