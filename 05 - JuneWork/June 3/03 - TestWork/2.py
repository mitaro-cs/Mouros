from itertools import *

def f(x,y,z,w):
    return ((y == (not(w))) <= (not(w and (x == (x or (w <= z))))))

for x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 in product([0,1],repeat=10):
    table = (
        (x1,x2,1,1,0),
        (x3,x4,1,x5,0),
        (x6,1,x7,1,0),
        (1,x8,x9,x10,1)
    )
    if len(table) == len(set(table)):
        for i in permutations("xyzw"):
            if all(f(**dict(zip(i, line[:-1]))) == line[-1] for line in table):
                print(*i)
                
            
