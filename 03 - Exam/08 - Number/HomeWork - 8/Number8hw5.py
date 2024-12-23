from itertools import *
res = set()

for i in product("АМОКТС",repeat = 6):
   a = "".join(i)
   if ((a[0] == "Т" and a.count("Т") == 1) or\
   (a[1] == "Т" and a.count("Т") == 1) or\
   (a[0] == "Т" and a[1] == "Т" and a.count("Т") == 2)) and \
   (a[-2] == "О" and a[-1] == "О" and a.count("О") == 2):
      res.add(a)
print(len(res))
