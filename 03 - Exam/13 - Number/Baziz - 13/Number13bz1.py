res = []
for i in range(2**19):
   a = bin(i)[2:]
   if (8 + a.count("1")) % 2 != 0:
      res.append(a)
print(len(res))
