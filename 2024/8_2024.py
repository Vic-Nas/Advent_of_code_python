# I love classes
import sys
from itertools import product 
rand = "."

class Point:
    def __init__(self, p, n = rand):
        self.x, self.y = p
        self.name = n
    def to(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5
    def __repr__(self):
        return f"({self.x}, {self.y})" + f" -> {self.name}" * (self.name != rand)
    def __ne__(self, p):
        return self.x != p.x or self.y != p.y or self.name != p.name
    def aligned(self, ps):
        x, y = self.x, self.y
        temp = list(filter(lambda p: p.x == x, ps))
        if len(temp) == len(ps): return "x"
        
        temp = list(filter(lambda p: p.y == y, ps))
        if len(temp) == len(ps): return "y"
        
        p = ps[0]
        for i in range(1, len(ps)):
            if (ps[i].x - self.x) * (p.y - self.y) != (p.x - self.x) * (ps[i].y - self.y):
                return False
                
        return "diag"

class Space:
    def __init__(self, data):
        self.len = len(data)
        self.all = list(map(Point, product(range(self.len), repeat = 2)))
        self.named = set()
        for x, y in product(range(self.len), repeat = 2):
            if data[y][x] != rand: self.named.add(Point((x, y), data[y][x]))

space = Space(list(map(lambda row : row.strip(), sys.stdin.readlines())))
SIZE = space.len
r1, r2 = set(), set()

m1, m2 = [list(rand * SIZE) for _ in range(SIZE)], [list(rand * SIZE) for _ in range(SIZE)]

for d in product(space.named, repeat = 2):
    if d[0].name == d[1].name and d[0] != d[1]:
        for p in space.all:
            if p.aligned(d):
                r2.add(p)
                m2[p.y][p.x] = "#"
                if abs(p.to(d[0]) - 2 * p.to(d[1])) <= 10 ** -6: 
                    r1.add(p)
                    m1[p.y][p.x] = "#"

f = lambda m: "\n".join(["".join(r) for r in m])
print(f"Part 1:\n", f(m1) + "\n", "\nPart 2:\n", f(m2) + "\n", sep = "\n")
print(len(r1), len(r2))