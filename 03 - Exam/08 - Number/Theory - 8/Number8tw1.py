from itertools import *

res = set()

for i in product("МОИСЕЙ",repeat = 4):
   a = "".join(i)
   if a[0] != "Й" and (a.count("О") + a.count("И") + a.count("Е")) >= 1:
      res.add(a)
print(len(res))

#Забыл про permutation

