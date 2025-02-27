def f(n):
   d = 2
   while d**2 <= n:
      if n % d == 0:
         return False
      d += 1
   return True

k = 0

for i in range(2943444, 2943529 + 1):
   k += 1
   if f(i):
      print(k, i)
