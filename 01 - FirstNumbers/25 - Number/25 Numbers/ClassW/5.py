def dlm(n):
   d = 1
   res = 0
   while d**2 <= n:
      if n % d == 0:
         if d % 10 == 7 and d != 7:
            return d
         if n//d % 10 == 7 and n//d != 7:
            res = n//d
      d += 1
   return res

k = 0      
for i in range(800000, 10**10):
   num = dlm(i)
   if num != 0:
      print(i,num)
      k += 1
      if k == 5:
         break
