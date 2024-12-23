f = open("./03 - Exam/17 - Number/HomeWork - 17/Number17hw5/17.txt")
a = [int(i) for i in f]

min5 = float("inf")
for i in range(len(a)):
   if (100 <= a[i] < 1000) and (a[i]%10==5):
      min5 = min(min5,a[i])
   
res = []
for i in range(len(a)-1):
   if ((100 <= a[i] < 1000) + (100 <= a[i+1] < 1000)) == 1:
      s = a[i] +a [i+1]
      if s % min5 ==0:
         res.append(s)

print(len(res),max(res))
