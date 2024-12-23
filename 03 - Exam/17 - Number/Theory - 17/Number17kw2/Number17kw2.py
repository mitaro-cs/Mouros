f = open("./03 - Exam/17 - Number/Theory - 17/Number17kw2/17.txt")
a = [int(i) for i in f]

max25 = -10**10
for i in range(len(a)):
	if abs(a[i]) % 100 == 25:
		max25 = max(max25, a[i])

res = []
for i in range(len(a)-2):
	if ((1000 <= abs(a[i]) < 10000) + (1000 <= abs(a[i+1]) < 10000) + (1000 <= abs(a[i+2]) < 10000)) >= 2:
		s = a[i] + a[i+1] + a[i+2]
		if s <= max25:
			res.append(s)

print(len(res),max(res)) 