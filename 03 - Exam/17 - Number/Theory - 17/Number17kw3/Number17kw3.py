f = open("./03 - Exam/17 - Number/Theory - 17/Number17kw3/17.txt")
a = [int(i) for i in f]

min3_7 = 10**10
for i in range(len(a)):
	if 100 <= abs(a[i]) < 1000 and abs(a[i]) % 7 == 0:
		min3_7 = min(min3_7, a[i])
	
min4 = 10**10
for i in range(len(a)):
	if 1000 <= abs(a[i]) < 10000:
		min4 = min(min4, a[i])

res = []
for i in range(len(a)-1):
	if ((a[i] < min3_7) + (a[i+1] < min3_7)) >= 1:
		p = a[i] * a[i+1]
		if (abs(p) % 10) == (abs(min4) % 10):
			s = a[i] + a[i+1]
			res.append(s)

print(len(res),max(res))
	