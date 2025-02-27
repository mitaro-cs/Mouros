f = open("./03 - Exam/17 - Number/Theory - 17/Number17kw4/17.txt")
a = [int(i) for i in f]

min_all = min(a)

res = []
for i in range(len(a)-1):
	if (a[i]%18 + a[i+1]%18) == min_all:
		res.append(a[i] + a[i+1])

print(len(res),max(res))
