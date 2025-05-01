from itertools import *

def f(x,y,z,w):
    return (x and (y <= z) and ((not(y)) <= (not(z) == w)))


for x1,x2,x3,x4,x5 in product([0,1],repeat=5):
    table = (
        (x1,x2,0,0,1),
        (x3,0,0,x4,1),
        (1,x5,1,1,0)
    )
    if len(table) == len(set(table)):
        for i in permutations("xyzw"):
            if all(f(**dict(zip(i,line[:-1]))) == line[-1] for line in table):
                print(*i)

