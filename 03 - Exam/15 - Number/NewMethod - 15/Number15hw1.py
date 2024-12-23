for a in range(0,1000):
   if all(((x+y <= 32) or ((y <= x+4) or (y >= a))) for x in range(0,1000) for y in range(0,1000)):
      print(a)