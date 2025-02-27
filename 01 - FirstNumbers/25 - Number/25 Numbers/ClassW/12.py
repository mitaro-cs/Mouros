def prime(n):
   d = 2
   while d**2 <= n:
      if n%d == 0:
         return False
      d += 1
   return True


def f(n):
   d = 2
   while d**2 <= n:
      if n%d == 0:
         if prime(n//d):
            return 0
         else:
            return n//d
      d += 1
   return 0

k = 0

for i in range(550000+1,10**10):
   res = f(i)
   if res != 0:
      print(i,res)
      k += 1
      if k == 6:
         break



