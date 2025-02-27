def f(n):
   res = []
   d = 2
   while d**2< n:
      if n%d == 0:
         if d%30 == 0:
            res.append(d)
         if (n//d) % 30 == 0:
            res.append(n//d)
      d += 1
   if d**2 == n and d % 30 == 0:
      res.append(d)
   return res

for n in range(51120, 89080):
   m = f(n)
   if len(m) == 2:
      print(n,m)
