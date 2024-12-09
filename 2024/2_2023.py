import sys
# inp = sys.stdin.readlines()

def prod(array) :
    res = 1
    for el in array : res *= el
    return res

def val(row: str):
    # temp1 = row.index("Game")
    temp2 = row.index(":")
    # res = int(row[temp1 + 5: temp2])
    row = row[temp2 + 2:].split(";")
    colors = ["blue", "red", "green"]
    # values = {"blue" : 14, "red" : 12, "green" : 13}
    curr_value = {"blue" : 0, "red" : 0, "green" : 0}
    for pick in row :
        pick = pick.split(", ")
        for sub in pick :
            for color in colors :
                if color in sub :
                    value = int(sub[:-len(color) - 1])
                    curr_value[color] = max(value, curr_value[color])                    
    return prod(list(curr_value.values()))
    

res = sum(map(val, sys.stdin.readlines()))
print(res)