from itertools import *
res = set()
num = 0
for i in product("АБЕЛТ",repeat = 5):
   a = "".join(i)
   num += 1
   if ((a[0] == "Л") and (a[-1] == "Т")):
      res.add(a)
      break
print(res, num)
