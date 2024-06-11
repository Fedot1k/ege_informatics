def deli(n, m): # функция делимости
    return n % m == 0


# решение задачи ↓↓↓


for A in range(1, 10000):
    flag = True
    for x in range(1, 3000):
        if (((deli(x, 45)) and (not deli(x, 15))) <= (not deli(x, A))) == False: # условие из задачи (просто переписать)
            flag = False
            break
    if flag:
        print(A)
        break