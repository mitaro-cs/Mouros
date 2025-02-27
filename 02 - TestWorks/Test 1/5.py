for n in range(100,1000):
   l = []
   n2 = str(n)
   for i in n2:
      l.append(int(i))
   l = sorted(l)
   maxn = str(l[-1]) + str(l[-2])
   if l[0] != 0 and l[1] != 0:
      minn = str(l[0]) + str(l[1])
   elif l[1] != 0:
      minn = str(l[1]) + str(l[0])
   else:
      minn = maxn
   R = int(maxn) - int(minn)
   if R == 70:
      print(n)
      break