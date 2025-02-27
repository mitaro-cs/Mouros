for n in range(1,10000):
   n2 = bin(n)[2:]
   if n % 4 == 0:
      n2 += n2
   else:
      n2 += n2[::-1]
   res = int(n2,2)
   if res > 544:
      print(n)
      break