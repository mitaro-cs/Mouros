def f(n):
    kd = 0
    d = 2
    maxd = -1
    while d * d <= n:
        if n % d == 0:
            if maxd == -1:
                maxd = n // d
            if d * d != n:
                kd += 2
            else:
                kd += 1
            if kd >= 4:
                break
        d += 1
    if kd == 3:
        print(n, maxd)

for i in range(123456789, 223456789 + 1):
    if i ** 0.5 == int(i ** 0.5):
        f(i)
