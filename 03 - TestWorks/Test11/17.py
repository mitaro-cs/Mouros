f = open(r"03 - TestWorks\Test11\17var11.txt")
a = [int(i) for i in f]

res = []
for i in range(len(a)-2):
	if (a[i] % 10 == 0) + (a[i+1] % 10 == 0) + (a[i+2] % 10 == 0) == 1:
		s = a[i] + a[i+1] + a[i+2]
		if s < max(a):
			res.append(s)

print(len(res),max(res))
