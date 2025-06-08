f = open(r"05 - JuneWork\June 6\Variant - 2\17_17558.txt")
a = [int(i) for i in f]
k = 0
for i in range(len(a)):
    if abs(a[i]) % 32 == 0:
        k += 1


res = []
for i in range(len(a) - 1):
    if ((a[i] < 0) + (a[i + 1] < 0)) >= 1:
        s = a[i] + a[i + 1]
        if s < k:
            res.append(s)
print(len(res), max(res))

