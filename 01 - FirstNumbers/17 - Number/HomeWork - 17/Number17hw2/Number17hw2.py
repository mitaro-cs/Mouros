f = open("./03 - Exam/17 - Number/HomeWork - 17/Number17hw2/17.txt")
a = [int(i) for i in f]

min7 = 10**10
for i in range(len(a)):
	if a[i] % 10 == 7:
		min7 = min(min7, a[i])

res = []
for i in range(len(a)-1):
	if ((a[i]%10 == 7) + (a[i+1]%10 == 7)) >= 1:
		if (a[i] - a[i+1])**2 > min7**2:
			s = a[i] + a[i+1]
			res.append(s)

print(len(res),max(res))
