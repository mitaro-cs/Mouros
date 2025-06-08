from itertools import *
k = 0
for i in product("АЗЛОПЬ",repeat = 6):
   a = "".join(i)
   k += 1
   if a.count("А") == 1 and a.count("Ь") <= 1 and a.count("З") <= 2:
      print(k,a)
      break