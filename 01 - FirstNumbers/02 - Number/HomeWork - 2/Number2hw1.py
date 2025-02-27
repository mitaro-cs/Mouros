from itertools import *

def f(x,y,z,w):
   return (not((not y) or z) or (x == w) or x)

for x1,x2,x3,x4,x5,x6,x7 in product([0,1],repeat=7):
   table = (
      (x1,0,x2,1,0),
      (1,x3,x4,0,0),
      (0,x5,x6,x7,0)
   )

   if len (table) == len(set(table)):
      for i in permutations("xyzw"):
         if all(f(**dict(zip(i, line[:-1]))) == line[-1] for line in table):
            print(*i)
            