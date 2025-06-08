from itertools import *

def f(x,y,z,w):
    return not(w <= (not(x <= y))) and ((not(x)) <= (not(y) == z))


for x1,x2,x3,x4,x5 in product([0,1],repeat=5):
    table = (
        (1,x1,1,1,0),
        (x2,x3,0,0,1),
        (x4,0,0,x5,1)
    )
    if len(table) == len(set(table)):
        for i in permutations("xyzw"):
            if all(f(**dict(zip(i,line[:-1]))) == line[-1] for line in table):
                print(*i)

