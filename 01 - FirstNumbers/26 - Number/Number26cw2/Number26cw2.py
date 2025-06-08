f = open(r"01 - FirstNumbers\26 - Number\Number26cw2\26_16.txt")
n = int(f.readline())   

a = [int(i) for i in f.readlines()]
a.sort(reverse=True)

tek = a[0]
k = 1
for i in range(1,n):
    if tek - a[i] >=7:
        k += 1
        tek = a[i]
print(k,tek)