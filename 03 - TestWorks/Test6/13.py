a = []

for i in range(2**5):
    s = bin(i)[2:]
    if 5 + s.count("1") <= 8:
        a.append(s)

print(len(a))