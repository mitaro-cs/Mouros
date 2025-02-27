from itertools import *

ch = "0246"
words = set()

for i in product("0123456",repeat=7):
   if sum(1 for j in i if j in ch) == 2 and i[0] != "0":
      words.add(i)
print(len(words))
      