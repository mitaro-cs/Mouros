def f(n):
   s = ""
   while n > 0:
      s += str(n%6)
      n //= 6
   return s

num = 5 * 216**1225 + 4 * 36**1256 - 4 * 6**1257 - 2023
num6 = f(num)
print(num6.count("5"))