def sum(n):
   d = 2
   while d**2 <= n:
      if n % d == 0:
         return d + n//d
      d += 1
   return 0

k = 0
for i in range(800000, 10**10):
   S = sum(i)
   if S % 10== 8:
      print(i,S)
      k += 1
      if k == 5:
         break
