def fn(n):
   d = 2
   while d**2 <= n:
      if n%d ==0:
         return d + n//d
      d += 1
   return 0

k = 0

for i in range(900001, 1000000):
   m = fn(i)
   if m % 10 == 4:
      print(i,m)
      k += 1
      if k == 5:
         break