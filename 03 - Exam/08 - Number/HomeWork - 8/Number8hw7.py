from itertools import *
res = set()

for i in permutations("ОЛЬГА",5):
   a = "".join(i)
   if (a[0] != "Ь") and\
      ("ОЬ" not in a and "АЬ" not in a):
      res.add(a)
print(len(res))
