def f(n):
   d = 2
   while d**2 < n:
      if n%d == 0:
         return n//d + d
      d += 1
   if d**2 == n:
      return d + d
   return 0
k = 0
for i in range(424242 + 1, 10**10):
   R = f(i)
   if R != 0 and R % 2024 == 42:
      print(i,R)
      k += 1
      if k == 8:
         break
