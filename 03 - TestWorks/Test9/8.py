from itertools import *
res = set()
k = 0
for i in product("01234567",repeat = 5):
   a = "".join(i)
   k += 1
   if a.count("4") == 2 and "14" not in a and "41" not in a and "34" not in a and "43" not in a and "54" not in a and "45" not in a and "74" not in a and "47" not in a:
      res.add(a)
print(len(res))
