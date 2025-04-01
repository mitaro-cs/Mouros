lf = []

for i in range(2**10):
    ad = bin(i)[2:]
    if 4 + ad.count("1") >= 7:
        lf.append(ad)

print(len(lf))