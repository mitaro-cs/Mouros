from itertools import *
res = set()

for i in product("СОН",repeat=6):
   a = "".join(i)
   if (a.count("Н") >= 2) + (a.count("НС") == 0) == 2:
      res.add(a)
print(len(res))
