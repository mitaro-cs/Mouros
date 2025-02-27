def is_prime(n):
   d = 2
   while d**2 < n:
      if n%d == 0:
         return False
      d += 1
   return True

def smd(n):
   s = 0
   d = 2
   while d**2 < n:
      if n % d == 0:
         if is_prime(d):
            s += d
         if is_prime(n//d):
            s += n//d
      d += 1
   if d**2 == n:
      if is_prime(d):
         s += d
   return s

k = 0

for i in range(550000+1, 10**10):
   num = smd(i)
   if num != 0 and num % 10 == 1:
      print(i,num)
      k += 1
      if k == 5:
         break

            