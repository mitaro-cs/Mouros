f = open(r"03 - TestWorks\Test7\17var07.txt")
a = [int(i) for i in f]

max90 = -10**10
for i in range(len(a)):
	if abs(a[i]) % 100 == 90:
		max90 = max(max90, a[i])

res = []
for i in range(len(a)-2):
	if ((1000 <= a[i] < 10000) + (1000 <= a[i+1] < 10000) + (1000 <= a[i+2] < 10000)) >= 1:
		s = a[i] + a[i+1] + a[i+2]
		if s > max90:
			res.append(s)

print(len(res),min(res))
