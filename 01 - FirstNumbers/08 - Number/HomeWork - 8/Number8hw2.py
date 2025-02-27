from itertools import *
res = set()

for i in product("АБВ",repeat = 5):
   a = "".join(i)
   if (a[0] == "А" and a.count("А") == 1) or  ((a[-1] == "А") and a.count("А") == 1):
      res.add(a)
print(len(res))
