for n in range(1,1000):
   n2 = bin(n)[2:]
   if n % 2 == 0:
      n2.replace("1","11")
   else:
      n2.replace("0","00")
   res = int(n2,2)
   if res < 70:
      print(n)