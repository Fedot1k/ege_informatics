def deli(n, m):
    return n % m == 0

for A in range(1, 10000):
    flag = True
    for x in range(0, 3000):
        for y in range(0, 3000):
            if (((y + 5 * x) < A) or ((3 * x + 2 * y) > 81)) == False:
                flag = False
                break
        if flag == False:
            break
    if flag:
        print(A)
        break