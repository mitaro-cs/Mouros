f = open("./03 - Exam/17 - Number/Theory - 17/Number17kw1/17.txt")
a = [int(i) for i in f]

max13 = -10**10
for i in range(len(a)):
	if a[i] % 100 == 13:
		max13 = max(max13, a[i])

res = []
for i in range(len(a)-2):
	if ((10 <= a[i] < 100) + (10 <= a[i+1] < 100) + (10 <= a[i+2] < 100)) == 1:
		s = a[i] + a[i+1] + a[i+2]
		if s <= max13:
			res.append(s)

print(len(res),max(res))
