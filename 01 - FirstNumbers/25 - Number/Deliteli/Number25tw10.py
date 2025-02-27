def f(n):
    res = []
    d = 2
    while d**2 <= n:
        if n%d == 0:
            if d % 15 == 0:
                res.append(d)
            if (n//d) % 15 == 0 and n//d != d:
                res.append(n//d)
        d += 1
    return(res)

for n in range(66730, 67001):
    m = f(n)
    if len(m) == 3:
        print(n,m)
