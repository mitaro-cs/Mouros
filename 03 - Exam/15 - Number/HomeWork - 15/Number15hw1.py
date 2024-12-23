for a in range(1,1000):
   flag = True
   for x in range(1,1000):
      if ((x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))) == False:
         flag = False
         break
   if flag == True:
      print(a)