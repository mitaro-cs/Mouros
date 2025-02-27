def f(n):
   res = []
   d = 2
   while d*d<n:
      if n % d == 0:
         res.append(d)
         res.append(n//d)
      d += 1
   if d*d == n:
      res.append(d)
   return res

for i in range(338427, 338494 + 1):
   num = f(i)
   if len(num) == 2:
      print(num)
