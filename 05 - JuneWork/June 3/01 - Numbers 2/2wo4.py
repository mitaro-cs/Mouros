from itertools import *

def f(x,y,z,w):
    return ((not(w <= x)) or (y <= z) or (not(y)))

for x1,x2,x3,x4,x5,x6,x7 in product([0,1],repeat=7):
    table = (
        (0,1,x1,x2,0),
        (x3,0,x4,1,0),
        (x5,x6,x7,0,0)
    )
    if len(table) == len(set(table)):
        for i in permutations("xyzw"):
            if all(f(**dict(zip(i, line[:-1]))) == line[-1] for line in table):
                print(*i)