from fnmatch import *

for i in range(3377,10**8+1,3377):
   if fnmatch(str(i),"?79?8*3"):
      print(i,i//3377)
      