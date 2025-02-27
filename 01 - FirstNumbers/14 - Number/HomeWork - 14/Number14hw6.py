def f(n):
   s = ""
   while n > 0:
      s += str(n%6)
      n //= 6
   return s

num = 5 * 216**155 + 4 * 36**156 - 4 * 6**157 - 2023
num6 = f(num)
print(num6.count("0"))