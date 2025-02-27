from itertools import *

def is_valid(word):
   for i in range(len(word)-1):
      if word[i] == "Я" and word[i+1] == "Я":
         return False
   return True

k = 0

for i in product("АВНРЬЯ",repeat=5):
   k += 1
   if i[0] != "Я" and i.count("Ь") <= 1 and is_valid(i):
      print(k,i)

      