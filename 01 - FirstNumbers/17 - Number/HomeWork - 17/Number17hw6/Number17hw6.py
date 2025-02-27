f = open("./03 - Exam/17 - Number/HomeWork - 17/Number17hw6/17.txt")
a = [int(i) for i in f]

maxel  = -10**10
for i in range(len(a)):
   if 10 <= a[i] < 100:
      maxel = max(maxel,a[i])

res = []
for i in range(len(a)-1):
   if ((10 <= a[i] < 100) + (10 <= a[i+1] < 100)) == 1:
      s = a[i] + a[i+1]
      if s % maxel == 0:
         res.append(s)

print(len(res),max(res))
