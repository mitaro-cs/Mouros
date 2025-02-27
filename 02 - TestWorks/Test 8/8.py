from itertools import *

ch = "0246"
words = set()

for i in product("0123456",repeat=6):
   if i[0] != "0" and i.count("0") == 1 and sum(1 for j in i if j in ch) == 2:
      words.add(i)
print(len(words))
      