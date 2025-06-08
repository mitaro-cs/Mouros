def f(n):
    mind = 0
    d = 1
    while d**2 <= n:
        if n%d == 0:
            if d % 10 == 9 and d != 9:
                return d
            if n//d % 10 == 9 and n//d != 9:
                mind = n//d
        d += 1
    return mind
k = 0
for i in range(500001,10**10):
    res = f(i)
    if res != 0:
        print(i,res)
        k += 1
        if k == 5:
            break
