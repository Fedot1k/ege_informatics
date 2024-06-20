# with open('G:/fedot/P2b.txt') as f:
#     n = f.readline()
#     l = list(map(int, f.readlines()))
# res = 0
# c_all = 0
# c_2 = 0
# c_7 = 0
# c_14 = 0
# for i in range(7, len(l)):
#     if l[i-7] % 14 == 0:
#         c_14 += 1
#     elif l[i-7] % 7 == 0:
#         c_7 += 1
#     elif l[i-7] % 2 == 0:
#         c_2 += 1
#     else:
#         c_all += 1
#     res += c_14
#     if l[i] % 2 == 0:
#         res += c_7
#     if l[i] % 7 == 0:
#         res += c_2
#     if l[i] % 14 == 0:
#         res += c_all
# print(res)


# f = open('DZ2b.txt')
# n = int(f.readline())
# k = 14
# counter = 0
# prop = [0] * k
# s = f.readlines()
# a = [int(i) for i in s]
# for i in range(5, n):
#     for x in range(k):
#         prop[x] += int(a[i-5] % k == x)
#     ost = a[i] % k
#     counter += prop[(k-ost)%14]
# f.close()
# print(counter)


with open('G:/fedot/DP3a.txt') as f:
    n = f.readline()
    l = list(map(int, f.readlines()))

ans = 0

l_ch = [x for x in l if x % 2 == 0]
l_nech = [x for x in l if x % 2 != 0]

l_13_ch = [x for x in l_ch if x % 13 == 0]
l_13_nech = [x for x in l_nech if x % 13 == 0]

ans += len(l_13_ch) * len(l_nech)
ans += len(l_13_nech) * len(l_ch)
ans -= len(l_13_ch) * len(l_13_nech)

print(ans)