def f(n):
    d = 2
    while d**2 <= n:
        if n%d == 0:
            return d + n//d
        d += 1
    return 0

k = 0
for n in range(700000+1 , 10**10):
    m = f(n)
    if m%10 == 4:
        k += 1
        print(n,m)
        if k == 5:
            break

            