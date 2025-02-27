def sum(n):
   d = 1
   sum_all = 0
   while d**2 < n:
      if n % d == 0:
         sum_all += d
         sum_all += n//d
      d += 1
   if d**2 == n:
      sum_all += d
   return sum_all

k = 0
for i in range(500001, 10**10):
   S = sum(i)
   if S % 10== 4:
      print(i,S)
      k += 1
      if k == 5:
         break
