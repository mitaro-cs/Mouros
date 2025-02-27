from itertools import *
res = set()

for i in product("1234",repeat = 6):
   a = "".join(i)
   if a.count("1") == 1:
      res.add(a)
print(len(res))
