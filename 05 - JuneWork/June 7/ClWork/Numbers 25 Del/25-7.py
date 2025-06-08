def f(n):
    res = []
    d = 2
    while d**2 < n:
        if n%d == 0:
            if d % 15 == 0:
                res.append(d)
            if n//d % 15 == 0:
                res.append(n//d)
        d += 1
    if d**2 == n and d%15 == 0:
        res.append(d)
    return res

for i in range(66730,67001):
    res = f(i)
    if len(res) == 3:
        print(i,res)

