from fnmatch import *

for i in range(12007,10**10+1,12007):
   if fnmatch(str(i),"9*?001?1"):
      print(i,i//12007)
      