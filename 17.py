def conv(n, base): # функция перевода в системы счисления (base < 10)
    res = ''
    while n != 0:
        res += str(n % base)
        n //= base
    return res[::-1]


# решение задачи ↓↓↓


c = 0
m = []

for i in range(138, 603885):
    s = [int(x) for x in str(i)]

    if check(i) and p_of_three(i):
        c += 1
        m.append(i)


print(c, m)
