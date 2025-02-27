f = open("./03 - Exam/17 - Number/HomeWork - 17/Number17hw9/17.txt")
a = [int(i) for i in f]

max3 = sorted(a)[-3]

res = []
for i in range(len(a)-2):
   if ((a[i] % 2 == 0) + (a[i+1] % 2 == 0) + (a[i+2] % 2 == 0)) <= 2:
      s = a[i] + a[i+1] + a[i+2]
      if s <= max3:
         res.append(s)

print(len(res),max(res))
