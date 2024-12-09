import sys
inp = sys.stdin.readlines()
res = 0
def curr_sum(row) : 
    new = row.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")    
    new = list(filter(str.isdigit, new))
    if new : return 10 * int(new[0]) + int(new[-1])
    return 0

res = sum(map(curr_sum, inp))
print(res)