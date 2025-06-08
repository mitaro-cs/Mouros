res = []
for n in range(1,1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = "10" + n2
    else:
        n2 = "1" + n2 + "01"
    r = int(n2,2)
    if n <= 12:
        res.append(r)
print(max(res))