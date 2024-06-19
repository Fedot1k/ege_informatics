with open('G:/fedot/DZ4.txt') as f:
    n, k = list(map(int, f.readline().split())) #700 70
    x = [int(i) for i in f.readlines()]

x = sorted(x)
x = x[::-1]

x = x[70:140]

print(sum(x)/len(x))