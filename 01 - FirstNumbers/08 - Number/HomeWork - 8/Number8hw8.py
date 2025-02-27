from itertools import *
res = set()

for i in product("КОНФЕТА",repeat = 5):
   a = "".join(i)
   if (a.count("О") + a.count("Е") + a.count("А")) >= 2  :
      res.add(a)
print(len(res))
