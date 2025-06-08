from itertools import *

def f(x,y,z,w):
    return (((w == 1) <= z) and ((not(y)) and x))

for x1,x2,x3,x4 in product([0,1],repeat=4):
    table = (
        (0,0,1,x1,0),
        (0,1,1,0,0),
        (x2,x3,1,0,0),
        (0,x4,1,0,1)
    )
    if len(table) == len(set(table)):
        for i in permutations("xyzw"):
            if all(f(**dict(zip(i, line[:-1]))) == line[-1] for line in table):
                print(*i)