from itertools import *
res = set()

for i in product("0123456789AB",repeat=5):
   a = "".join(i)
   if a.count("7") == 1 and\
      (a.count("9") + a.count("A") + a.count("B")) <= 3 and\
      a[0] != "0":
      res.add(a)
print(len(res))