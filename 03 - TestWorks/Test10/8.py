from itertools import *
res = set()
k = 0
for i in product("0123",repeat = 5):
   a = "".join(i)
   k += 1
   if a.count("3") == 1 and "03" not in a and "30" not in a:
      res.add(a)
print(len(res))