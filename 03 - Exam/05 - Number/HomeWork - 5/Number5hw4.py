for n in range(1,1000):
   n2 = bin(n)[2:]
   if n%2 == 0:
      n2 += "00"
   else:
      n2 += "11"
   R = int(n2,2)
   if R >83:
      print(n)
      break