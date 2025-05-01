from itertools import *

def f(x,y,z,w):
    return y and (x <= w) and ((not(x)) <= ((not(w)) == z))


for x1,x2,x3,x4,x5 in product([0,1],repeat=5):
    table = (
        (0,0,x1,x2,1),
        (0,x3,x4,0,1),
        (1,1,1,x5,0)
    )
    if len(table) == len(set(table)):
        for i in permutations("xyzw"):
            if all(f(**dict(zip(i,line[:-1]))) == line[-1] for line in table):
                print(*i)

