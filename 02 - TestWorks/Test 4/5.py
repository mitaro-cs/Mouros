res = []
for n in range(1,8):
   n2 = bin(n)[2:]
   if n % 2 == 0:
      n2 = "10" + n2
   else:
      n2 = "1" + n2 + "01"
   R = int(n2,2)
   res.append(R)

print(max(res))
