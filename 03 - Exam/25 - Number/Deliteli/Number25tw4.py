k = 0
for i in range(850001,1000000):
   dif = 0
   d = 2
   while d**2 < i:
      if i % d ==0:
         dif = i//d - d
         break
      d += 1
   if d**2 == i:
      dif = 0
   if dif != 0 and dif % 3 == 0:
      print(i,dif)
      k += 1
      if k == 6:
         break