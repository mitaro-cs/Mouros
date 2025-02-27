def dlm(n):
   d = 2
   res = 0
   while d**2 <= n:
      if n % d == 0:
         if d % 10 == 9 and d != 9:
            return d
         if n//d % 10 == 9 and n//d != 9:
            res = n//d
      d += 1
   return res

k = 0      
for i in range(700001, 10**10):
   num = dlm(i)
   if num != 0:
      print(i,num)
      k += 1
      if k == 5:
         break
