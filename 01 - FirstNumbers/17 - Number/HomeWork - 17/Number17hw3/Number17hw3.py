f = open("./03 - Exam/17 - Number/HomeWork - 17/Number17hw3/17.txt")
a = [int(i) for i in f]

max12 = -10**10
for i in range(len(a)):
   if a[i] % 100 == 12:
      max12 = max(max12, a[i])
      
res = []
for i in range(len(a)-1):
   if ((a[i]%100 == 12) + (a[i+1]%100 == 12)) == 1:
      if ((a[i]+a[i+1])**2) < (max12**2):
         s = a[i] + a[i+1]
         res.append(s)

print(len(res),max(res))
