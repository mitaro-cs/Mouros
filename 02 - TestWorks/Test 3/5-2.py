for n in range(1,1000):
   n2 = bin(n)[2:]
   n2 += str(n2.count("1")%2)
   n2 += str(n2.count("1")%2)
   r = int(n2,2)
   if r > 77:
      print(n)
      break