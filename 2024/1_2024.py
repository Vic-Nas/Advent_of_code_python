import sys

l1, l2 = [], []
def func(row) : 
    val = row.split()
    global l1, l2
    l1.append(int(val[0]))
    l2.append(int(val[1]))
    # # diff = abs(val[0] - val[1])
    # # print(diff)
    # return diff

list(map(func, sys.stdin.readlines()))
res = 0
for i in range(len(l1)) : res += abs(l1[i] * l2.count(l1[i]))
print(res)
# print(res)

