from itertools import *

def f(x,y,z,w):
    return (not(y <= x) or (y == w) or z) 

for x1,x2,x3,x4,x5,x6 in product([0,1],repeat=6):
    table = (
      (x1, x2, 1, 1, 0),
      (x3, x4, 1, x5, 0),
      (0, 1, x6, 1, 0)
    )

    if len (table) == len(set(table)):
        for i in permutations("xyzw"):
            if all(f(**dict(zip(i, line[:-1]))) == line[-1] for line in table):
                print(*i)
            