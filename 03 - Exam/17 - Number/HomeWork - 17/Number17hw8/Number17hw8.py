f = open("./03 - Exam/17 - Number/HomeWork - 17/Number17hw8/17.txt")
a = [int(i) for i in f]

cr11 = []
for i in range(len(a)):
   if abs(a[i]) % 11 ==0:
      cr11.append(a[i])

avgcr11 = sum(cr11) / len(cr11)

res = []
for i in range(len(a)-2):
   if ((abs(a[i]) % 100 == 11) + (abs(a[i+1]) % 100 == 11) + (abs(a[i+2]) % 100 == 11)) >= 1:
      s = a[i] + a[i+1] + a[i+2]
      avg3 = (a[i] + a[i+1] + a[i+2]) / 3
      if avg3 > avgcr11:
         res.append(s)

print(len(res),max(res))
