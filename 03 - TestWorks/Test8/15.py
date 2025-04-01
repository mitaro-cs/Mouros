for a in range(0,1000):
   if all(((x >= 20) or (y >= 40) or (y <= x + a) or (y >= 3*x - a)) for x in range(0,1000) for y in range(0,1000)):
      print(a)
      break
   