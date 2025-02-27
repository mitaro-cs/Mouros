def f(num):
   s = ""
   while num>0:
      s += str(num%3)
      num //= 3
   return s[::-1]

result = []

for n in range(1,1001):
   num3 = f(n)
   if n % 3 == 0:
      num3 += num3[-2:]
   else:
      sum3 = f(num3.count("1") + (num3.count("2") * 2))
      num3 += sum3
   R = int(num3,3)
   if R % 2 == 0 and R > 220:
      result.append(R)

print(min(result))