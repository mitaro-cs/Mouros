for a in range(0,1000):
   if all(((x**2+y**2 > 128) or (y < -x+a)) for x in range(0,1000) for y in range(0,1000)):
      print(a)
      break
   