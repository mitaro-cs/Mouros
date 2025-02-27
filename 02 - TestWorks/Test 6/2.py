from itertools import *

def f(x,y,z,w):
   return (not(x or y) and not(w) or not(z or w) and y)

for x1,x2,x3,x4,x5,x6,x7,x8 in product([0,1],repeat=8):
   table = (
      (x1,1,x2,x3,1),
      (x4,x5,1,x6,1),
      (x7,1,x8,1,1)
   )

   if len (table) == len(set(table)):
      for i in permutations("xyzw"):
         if all(f(**dict(zip(i, line[:-1]))) == line[-1] for line in table):
            print(*i)
            