print('x y z w')

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = z <= (x == (w <= y))
                if f == 0 or f == 1:
                    print(x, y, z, w, "=", int(f))