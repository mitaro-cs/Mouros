from itertools import *
k = 0
for i in product("КНОРСЯ",repeat = 6):
   a = "".join(i)
   k += 1
   if a.count("К") <= 3 and a.count("Я") == 2:
      print(k,a)
      break