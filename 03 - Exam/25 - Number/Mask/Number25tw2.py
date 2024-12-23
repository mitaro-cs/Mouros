from fnmatch import *

for i in range(259,10**9,259):
   if fnmatch(str(i),"1?31*511"):
      print(i,i//259)