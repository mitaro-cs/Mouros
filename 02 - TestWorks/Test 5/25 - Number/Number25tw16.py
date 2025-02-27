def f(n):
    d = 2
    mind = 0
    while d**2 <= n:
        if n % d == 0:
            if d % 10 == 8 and d != 8:
                return d 
            if (n//d) % 10 == 8 and (n//d) != 8:
                mind = n//d
        d += 1
    return mind

k = 0
for n in range(500000+1, 10**10):
    m = f(n)
    if m != 0:
        k += 1
        print(n,m,sep=" - ")
        if k == 5:
            break