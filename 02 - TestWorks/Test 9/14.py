def f6(n):
   s = ""
   num = n
   while num > 0:
      s = str(num%6)
      num //= 6
   return s[::-1]


for x in range(1,1000,6):
   if f6(6**2025 + 6 **25 - x).count("0") == 2002:
      print(x)

