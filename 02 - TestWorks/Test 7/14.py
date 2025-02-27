def f(n):
   s = ""
   while n > 0:
      s += str(n%9)
      n //= 9
   return s

for x in range(1,5769):
   num = 9**2025 + 9**1000 - x
   num9 = f(num)
   if num9.count("0") == 1026:
      print(x)
