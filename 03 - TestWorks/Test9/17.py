f = open(r"03 - TestWorks\Test8\17var08.txt")
a = [int(i) for i in f]

min700 = 10**10
for i in range(len(a)):
	if abs(a[i]) % 1000 == 700:
		min700 = min(min700, a[i])

res = []
for i in range(len(a)-2):
	if ((10000 <= abs(a[i]) < 100000) + (10000 <= abs(a[i+1]) < 100000) + (10000 <= abs(a[i+2]) < 100000)) <= 2:
		s = a[i] + a[i+1] + a[i+2]
		if s >= min700:
			res.append(s)

print(len(res),min(res))
