from fnmatch import *
for i in range(137,10**9+1,137):
   if fnmatch(str(i),"1234*7?8"):
      print(i,i//137)
