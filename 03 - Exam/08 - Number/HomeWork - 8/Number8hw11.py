from itertools import *
res = set()

for i in product("012345678",repeat=6):
   a = "".join(i)
   if (a.count("4") == 1) and\
      ((a.count("1") + a.count("3") + a.count("5") + a.count("7"))  == 2) and\
      (a[0] != "0"):
      res.add(a)
print(len(res))
