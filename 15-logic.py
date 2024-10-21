for A in range(0, 3000):
    valid = True
    for x in range(0, 10000):
        for y in range(0, 10000):
            if (5 * x - 6 * y < A) or (x - y > 30):
                continue
            else:
                valid = False
                break
        if not valid:
            break
    if valid:
        print(A)
        break