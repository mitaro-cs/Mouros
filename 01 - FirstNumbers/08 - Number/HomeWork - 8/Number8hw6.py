from itertools import *
res = set()

for i in product("МОДУЛЬ",repeat = 5):
   a = "".join(i)
   if a[0] != "Ь":
      res.add(a)
print(len(res))
