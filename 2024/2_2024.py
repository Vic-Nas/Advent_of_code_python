import sys

def check(new):
    inc = True
    for i in range(len(new) - 1) :
        diff = new[i + 1] - new[i]
        if not (0 < abs(diff) < 4) : return False
        if i == 0 and diff < 0 : inc = False
        if (diff > 0 and not inc) or (diff < 0 and inc) : return False
    return True
    
res = 0
for row in sys.stdin.readlines() :
    new = list(map(int, row.split()))
    for i in range(len(new)):
        new2 = new.copy()
        new2.pop(i)
        if check(new2) : 
            res += 1
            break    
print(res)   