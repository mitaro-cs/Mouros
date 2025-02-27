for n in range(1,1000):
   n2 = bin(n)[2:]
   if n % 2 == 0:
      n2 = n2.replace("1", "11")
   else:
      n2 = n2.replace("0", "00")
   r = int(n2, 2)
   if r > 70:
      print(n)
      break
