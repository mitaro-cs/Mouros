def fn(n):
   kd = 0
   dl = 1
   while dl**2 <= n:
      if n % dl == 0:
         if dl**2 != n:
            kd += 2
         else:
            kd += 1
      dl += 1
   return kd

for i in range(3954,8980):
   m = fn(i)
   if 41 <= m <= 45:
      print(i,m)
      
