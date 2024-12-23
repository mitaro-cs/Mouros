from itertools import *

ch = "0246"
nch = "1357"
def is_valid(word):
   for i in range(len(word)-1):
      if (word[i] in ch and word[i+1] in ch) or\
      (word[i] in nch and word[i+1] in nch):
         return False
   return True

res = set()

for i in permutations("01234567",5):
   a = "".join(i)
   if (a.count("1") == 0) and (is_valid(a)) and (a[0] != "0"):
      res.add(a)
print(len(res))