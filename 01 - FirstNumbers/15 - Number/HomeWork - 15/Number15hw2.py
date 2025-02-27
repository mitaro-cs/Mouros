for a in range(1,1000):
   flag = True
   for x in range(1,1000):
      if ((x % a != 0) <= ((x % 36 == 0) <= (x % 54 != 0))) == False:
         flag = False
         break
   if flag == True:
      print(a)