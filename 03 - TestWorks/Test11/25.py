from fnmatch import *

for i in range(2049,10**9+1,2049):
   if fnmatch(str(i),"32*21?4"):
      print(i,i//2049)
      