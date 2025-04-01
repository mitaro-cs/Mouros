f = open(r"03 - TestWorks/Test6/17var06.txt")
a = [int(i) for i in f]

max100 = -10**10
for i in range(len(a)):
	if a[i] % 1000 == 100:
		max100 = max(max100, a[i])

res = []
for i in range(len(a)-2):
	if ((100 <= a[i] < 1000) + (100 <= a[i+1] < 1000) + (100 <= a[i+2] < 1000)) == 2:
		s = a[i] + a[i+1] + a[i+2]
		if s <= max100:
			res.append(s)

print(len(res),max(res))
