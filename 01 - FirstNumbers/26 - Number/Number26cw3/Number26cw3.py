f = open(r"01 - FirstNumbers\26 - Number\Number26cw3\26_23.txt")
n = int(f.readline())
a = [int(i) for i in f.readlines()]

a.sort()
res1 = sum(a[:n - n//4])
res2 = sum(a[n//4:])

print(res1,res2)