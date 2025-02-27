for a in range(1,1000):
   if all((x%a == 0) or ((200 <= x <= 300) <= (x%77 !=0)) for x in range(1,1000)):
      print(a)
      