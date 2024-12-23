print("X Y Z W F")
for x in range(0,2):
   for y in range(0,2):
      for z in range(0,2):
         for w in range(0,2):
            for f in range(0,2):
               f = (int(w <= (y == z)) and (y == (z <= x)))
               print(x,y,z,w,int(f))
