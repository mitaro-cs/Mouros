from itertools import *

def f(x,y,z,w):
   return (y <= z) and (w == (x <= y)) and not(x)

for x1,x2,x3,x4,x5,x6,x7 in product([0,1],repeat=7):
   table = (
      (0,1,x1,x2,1),
      (1,x3,x4,x5,1),
      (x6,0,1,x7,1)
   )

   if len (table) == len(set(table)):
      for i in permutations("xyzw"):
         if all(f(**dict(zip(i, line[:-1]))) == line[-1] for line in table):
            print(*i)
