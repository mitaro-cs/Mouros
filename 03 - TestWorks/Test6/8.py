from itertools import *
res = set()
k = 0
for i in product("АЕИКЛПР",repeat = 6):
   a = "".join(i)
   k += 1
   if a[0] != "К" and a.count("И") >= 2 and k % 2 == 0 :
      res.add(a)
print(len(res))
