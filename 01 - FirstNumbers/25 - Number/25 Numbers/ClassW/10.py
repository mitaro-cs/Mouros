def is_prime(n):
   d = 2
   while d**2 < n:
      if n % d == 0:
         return False
      d += 1
   return True

def f(n):
   d = 2
   while d**2 <= n:
      if n % d == 0:
         if is_prime(n//d):
            return 0
         else:
            return n//d
      d += 1
   return 0

k = 0

for i in range(450000, 10**10):
   dlm = f(i)
   if dlm != 0:
      print(i,dlm)
      k += 1
      if k == 6:
         break

