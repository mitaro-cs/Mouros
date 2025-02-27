res = []
for n in range(1,1000):
   n2 = bin(n)[2:]
   if n % 3 == 0:
      n2 += n2[-2:]
   else:
      n2 += bin((n%3)*3)[2:]
   R = int(n2,2)
   if R >= 195:
      res.append(R)
print(min(res))