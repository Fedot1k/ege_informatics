def conv(n, base):
    res = ''
    while n != 0:
        res += str(n % base)
        n //= base
    return res[::-1]



d = [7, 13, 17, 19]

c = 0
m = -1

for i in range(1111, 10000):
    pro = 1
    s = [int(x) for x in str(i)]

    for j in s:
        pro = pro * j

    if (i%(sum(s))==0) and (pro != 0) and (i%pro==0):
        c += 1
        m = max(m, i)


print(c, m)
