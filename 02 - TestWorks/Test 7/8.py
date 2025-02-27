from itertools import *
res = set()
nch = "135"

def is_valid(num):
   for i in range(len(num) - 1):
      if num[i] in nch and num[i+1] == "0" or\
      num[i] == "0" and num[i+1] in nch:
         return False
   return True

for i in product("012345",repeat = 6):
   a = "".join(i)
   if a[0] != "0" and a.count("0") == 1 and is_valid(a):
      res.add(a)
print(len(res))