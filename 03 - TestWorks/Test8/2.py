from itertools import *

def f(x,y,z,w):
    return (not(w <= x) or ((not(z)) <= (not(y))) or z) #в импликации с двух сторон обязательно


for x1,x2,x3,x4,x5,x6 in product([0,1],repeat=6):
    table = (
        (1,0,1,x1, 0),
        (1,x2,x3,x4,0),
        (x5,x6,1,1, 0)
    )
    if len(table) == len(set(table)):
        for i in permutations("xyzw"):
            if all(f(**dict(zip(i,line[:-1]))) == line[-1] for line in table):
                print(*i)

