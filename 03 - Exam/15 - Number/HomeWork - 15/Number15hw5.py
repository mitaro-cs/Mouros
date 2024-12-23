for a in range(1,1000):
   flag = True
   for x in range(1,1000):
      if (((x % 35 != 0) and (x % a == 0)) <= ((x % 21 == 0) or (x % a != 0))) == False:
         flag = False
         break
   if flag == True:
      print(a)
      break