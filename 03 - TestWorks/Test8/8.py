from itertools import *
res = set()
k = 0
for i in product("АГЕИЛНРТ",repeat = 5):
   a = "".join(i)
   k += 1
   if a[0] != "Т" and 0 < a.count("Н") <= 2 and k % 2 != 0 :
      res.add(a)
print(len(res))
