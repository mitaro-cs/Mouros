print("X Y Z W")
for x in range(0,2):
   for y in range(0,2):
      for z in range(0,2):
         for w in range(0,2):
            if ((x == (w or y)) or ((w <= z) and (y <= w))) == False:
               print(x,y,z,w)
