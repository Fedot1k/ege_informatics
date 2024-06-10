def f(n):
    if n <= 15 :
        return (n * n) + (3 * n) + 9
    elif n > 15 and n%3==0:
        return f(n-1) + n - 2
    elif n > 15 and n%3!=0:
        return f(n-2) + n + 2


res = 0

for i in range(1, 1001):

    alleven = True

    for char in str(f(i)):
        if int(char) % 2 != 0:
            alleven = False
            
    if alleven:
        res += 1

print(res)