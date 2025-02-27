def f(n):
   d = 2
   allnum = []
   while d**2 < n:
      if n%d == 0:
         allnum.append(d)
         allnum.append(n//d)
      d += 1
   if d**2 == n:
      allnum.append(d)
   return allnum
k = 0
for i in range(700001, 10**10):
   R = f(i)
   if len(R) == 4 and max(R) - min(R) <= 15:
      print(i,R)
      k += 1
      if k == 6:
         break
