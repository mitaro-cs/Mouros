def f(n):
   s = ""
   while n > 0:
      s += str(n%3)
      n //= 3
   return s

num = (2 * 729**1021) - (2 * 243**1022) + (81**1023) - (2 * 27**1024) - 1025
num3 = f(num)
print(num3.count("0"))
