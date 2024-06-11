def f(n): # функция из задачи
    if n > 25:
        return (n*n) + (2*n) + 1
    elif n <= 25 and n%2==0:
        return (2 * f(n+1)) + f(n + 3)
    elif n <= 25 and n%2!=0:
        return f(n+2) + (3 * f(n + 5))


# решение задачи ↓↓↓


res = 0

for i in range(1, 1001):
    p = f(i)
    s = [int(x) for x in str(p)]
    if 0 not in s:
        res += 1

print(res)