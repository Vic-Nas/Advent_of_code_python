import sys
from copy import deepcopy

turtle = list(map(lambda row : list(row.split()[0]), sys.stdin.readlines()))
marked = "X"
obstacle = "#"
directions = {"^" : (-1, 0, ">"), ">" : (0, 1, "v"), "v" : (1, 0, "<"), "<" : (0, -1, "^")}

def fd(turtle):
    states = []
    while True:
        found = False
        for i in range(len(turtle)):
            for j in range(len(turtle[0])):
                if turtle[i][j] in directions.keys():
                    found = True
                    di, dj, turn = directions[turtle[i][j]]
                    i1 = i + di
                    j1 = j + dj
                    state = (i, j, i1, j1)
                    if state in states: return False
                    states.append(state)
                    if 0 <= i1 < len(turtle) and 0 <= j1 < len(turtle[0]):
                        if turtle[i1][j1] != obstacle:
                            turtle[i1][j1] = turtle[i][j]
                            turtle[i][j] = marked
                        else: turtle[i][j] = turn; continue
                    else: turtle[i][j] = marked
                    break
            if found: break
        if not found: return turtle

final_state = fd(deepcopy(turtle))
if final_state: print(sum(row.count(marked) for row in final_state))
else : print("Cycle")

res = 0
for i in range(len(turtle)):
    for j in range(len(turtle[0])):
        if turtle[i][j] == ".":
            turtle[i][j] = obstacle
            if not fd(deepcopy(turtle)): res += 1
            turtle[i][j] = "."
print(res)