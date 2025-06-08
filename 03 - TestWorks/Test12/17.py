f = open(r"03 - TestWorks\Test12\17var12.txt")
a = [int(i) for i in f]

res = []
for i in range(len(a)-2):
	if (a[i] % 10 == 3) + (a[i+1] % 10 == 3) + (a[i+2] % 10 == 3) == 0:
		s = a[i]**2 + a[i+1]**2 + a[i+2]**2
		if s > max(a):
			res.append(s)

print(len(res),min(res))
