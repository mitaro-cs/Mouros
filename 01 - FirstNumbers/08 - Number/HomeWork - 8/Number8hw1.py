from itertools import *
res = set()

for i in product("АБВГДЕ",repeat = 5):
   a = "".join(i)
   if a.count("Г") == 2:
      res.add(a)
print(len(res))
