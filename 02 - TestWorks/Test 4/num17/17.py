f = open("./01 - Student/00 - TestWork/Variant4/num17/17.txt")
a = [int(i) for i in f]

len3 = 0
for i in range(len(a)):
	if a[i] % 3 == 0:
		len3 += 1

res = []
for i in range(len(a)-1):															
	if ((a[i] < 0) + (a[i+1] < 0)) >= 1:
		s = a[i] + a[i+1]
		if s < len3:
			res.append(s)

print(len(res),max(res))

