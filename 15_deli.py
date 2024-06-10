def deli(n, m):
    return n % m == 0

for A in range(1, 10000):
    flag = True
    for x in range(1, 3000):
        if ((deli(A, 40)) and (deli(780, x)) <= ((not deli(A, x)) <= (not deli(180, x)))) == False:
            flag = False
            break
    if flag:
        print(A)
        break