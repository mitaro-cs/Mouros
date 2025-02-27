from itertools import *
k = 0
for i in product("АБРТЫ",repeat=5):
   k += 1
   if i.count("А") == 0 and i.count("Р") == 0:
      print(k,i)
      break