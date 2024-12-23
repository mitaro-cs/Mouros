for n in range(100,1000):
   sum1 = int(str(n)[0]) + int(str(n)[1])
   sum2 = int(str(n)[1]) + int(str(n)[2])
   result = int(str(max(sum1,sum2)) + str(min(sum1,sum2)))
   if result == 157:
      print(n)
      break
   