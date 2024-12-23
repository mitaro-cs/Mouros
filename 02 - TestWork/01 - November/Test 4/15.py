for a in range(0,1000):
   flag = True
   for x in range(0,1000):
      for y in range(0,1000):
         if ((x+y<=32) or (y<=x+4) or (y >= a)) == False:
            flag = False
            break
      if flag == False:
         break
   if flag == True:
      print(a)