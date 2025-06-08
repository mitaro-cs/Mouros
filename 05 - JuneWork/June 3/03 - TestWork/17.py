f = open(r"03 - TestWork\Files\17.txt")
a = [int(i) for i in f]
max4 = 0
res = []

for mx in range(len(a)):
	if mx % 1000 >= 0:
		max4 = max(max4,mx)

for i in range(len(a)-1):
	rz = abs(a[i] - a[i+1])
	if rz >= max4:	
		res.append(rz)

print(len(res),max(res))