from itertools import *

letters = "ABCD"
numbers = "13579"

def is_valid(word):
   for i in range(len(word)-1):
      if (word[i] in letters and word[i+1] in numbers) or\
         (word[i] in numbers and word[i+1] in letters):
         return False
   return True

res = set()

for i in product("0123456789ABCD",repeat=5):
   a = "".join(i)
   if a[0] != "0" and is_valid(a):
      res.add(a)
print(len(res))
