from fnmatch import *

for i in range(123,10**8+1,123):
   if fnmatch(str(i),"32*823"):
      print(i,i//123)
      