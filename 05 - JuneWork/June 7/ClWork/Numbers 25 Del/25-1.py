def f(n):
    res = []
    d = 2
    while d**2 < n:
        if n % d == 0:
            res.append(d)
            res.append(n//d)
        d += 1
    if d**2 == n:
        res.append(d)
    return res

for i in range(338472,338494+1):
    res = f(i)
    if len(res) == 2:
        print(res)