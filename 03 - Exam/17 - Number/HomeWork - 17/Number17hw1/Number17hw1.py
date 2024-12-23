f = open("./03 - Exam/17 - Number/HomeWork - 17/Number17hw1/17.txt")
a = [int(i) for i in f]

max171 = -10**10
for i in range(len(a)):
	if a[i] % 171 == 0:
		max171 = max(max171, a[i])

res = []
for i in range(len(a)-1):															
	if ((a[i] < max171) + (a[i+1] < max171)) >= 1:
		if (a[i]%2 == 0) + (a[i+1]%2 == 0) >= 1:
			s = a[i] + a[i+1]
			res.append(s)

print(len(res),max(res))
