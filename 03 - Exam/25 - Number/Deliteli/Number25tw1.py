for i in range(2582741,2582970):
   res = []
   d = 2
   while d**2 < i:
      if i % d == 0:
         res.append(d)
         res.append(i//d)
      d += 1
   if d**2 == i:
      res.append(d)
   if len(res) == 2:
      print(i,res)
   