import sys

data = map(lambda row : list(row.split()[0]), sys.stdin.readlines())
def valid(x, y, data) : 
    return 0 <= x < len(data) and 0 <= y < len(data[x])

def get_el(x, y, data):
    return data[x][y] if valid(x, y, data) else ""

def cpt(data, directions, condition_fn):
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            for dx, dy in directions:
                if condition_fn(i, j, dx, dy, data):
                    count += 1
    return count

def condition(i, j, dx, dy, grid):
    return all(get_el(i + k * dx, j + k * dy, grid) == "XMAS"[k] for k in range(4))


directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

print(cpt(data, directions, condition))


print(cpt(data, directions[::2],
    lambda i, j, dx, dy, grid :
        get_el(i, j, grid) == "A" and
        all(get_el(i + k * dx, j + k * dy, grid) == get_el(i + k * -dy, j + k * dx, grid) == val 
        for k, val in [(-1, "M"), (1, "S")])))