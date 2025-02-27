def f(n):
   d = 2
   while d**2 < n:
      if n%d == 0:
         return n//d - d
      d += 1
   return 0
k = 0
for i in range(850000, 10**10):
   R = f(i)
   if R != 0 and R%5 == 0:
      print(i,R)
      k += 1
      if k == 6:
         break
