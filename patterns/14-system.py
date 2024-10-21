def ss(n, b):
    res = []
    while n:
        res.append(n%b)
        n //= b
    return ''.join(str(x) for x in res[::-1])


for p in range(9, 20):
    for x in ('0123456789ABCDEFGHIJ'):
        for y in ('0123456789ABCDEFGHIJ'):
            for z in ('0123456789ABCDEFGHIJ'):
                f1 = str(y) + '2' + str(y)
                f2 = str(y) + '87'
                f3 = '1' + str(x) + str(z) + str(z)
                try: 
                    if (int(f1, p) + int(f2, p)) == int(f3, p):
                        print(x, y, z, p)
                except:
                    pass

