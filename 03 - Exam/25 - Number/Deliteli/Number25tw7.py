def fn(n):
   dl = 2
   mindl = 0
   while dl**2 <= n:
      if n % dl == 0:
         if dl % 10 == 7 and dl != 7: # проверка первой половины делителей
            return dl
         if n//dl % 10 == 7 and n//dl != 7: # Если в первой половине не нашли делители
            mindl = n//dl # проверка второй половины делителей
      dl += 1
   return mindl

k = 0

for i in range(800001, 1000000):
   m = fn(i)
   if m != 0:
      print(i,m)
      k += 1
      if k == 5:
         break