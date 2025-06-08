from itertools import *

def f(x,y,z,w):
    return ((z == (not(y))) and ((not(x)) or y) and w)

for x1,x2,x3,x4,x5,x6 in product([0,1],repeat=6):
    table = (
        (1,x1,x2,0,1),
        (0,0,x3,1,1),
        (x4,x5,x6,1,1)
    )
    if len(table) == len(set(table)):
        for i in permutations("xyzw"):
            if all(f(**dict(zip(i, line[:-1]))) == line[-1] for line in table):
                print(*i)