for A in range(0, 10000):
    flag = True
    for x in range(0, 10001):
        if ((x & 51 == 0) or ((x & 41 == 0) <= (x & A == 0))) == False:
            flag = False
            break
    if flag:
        print(A)