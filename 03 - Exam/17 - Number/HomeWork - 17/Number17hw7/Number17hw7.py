f = open("./03 - Exam/17 - Number/HomeWork - 17/Number17hw7/17.txt")
a = [int(i) for i in f]

max42 = -10**10
for i in range(len(a)):
   if abs(a[i]) % 100 == 42:
      max42 = max(max42,a[i])

res = []
for i in range(len(a)-2):
   if ((abs(a[i]) % 100 == 42) + (abs(a[i+1]) % 100 == 42) + (abs(a[i+2]) % 100 == 42)) >= 2:
      s = a[i] * a[i+1] * a[i+2]
      if s > max42**2:
         res.append(s)

print(len(res),max(res))
