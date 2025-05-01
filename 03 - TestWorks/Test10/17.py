f = open(r"03 - TestWorks\Test10\17var10.txt")
a = [int(i) for i in f]

max2 = -10**10
for i in range(len(a)):
	if abs(a[i]) % 2 == 0:
		max2 = max(max2, a[i])

res = []
for i in range(len(a)-1):
	s = a[i] + a[i+1]
	if s == max2:
		res.append(s)

print(len(res),max(res))
