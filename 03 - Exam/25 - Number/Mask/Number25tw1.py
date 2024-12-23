from fnmatch import *

for i in range(2023,10**8,2023):
   if fnmatch(str(i),"2*1?71"):
      print(i,i//2023)