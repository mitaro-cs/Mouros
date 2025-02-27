def f(n):
    d = 2
    mind = 0
    while d**2 <= n:
        if n % d == 0:
            if d % 10 == 7 and d != 7:
                return d 
            if (n//d) % 10 == 7 and (n//d) != 7:
                mind = n//d
        d += 1
    return mind

k = 0
for n in range(600000+1, 10**10):
    m = f(n)
    if m != 0:
        k += 1
        print(n,m,sep=" - ")
        if k == 5:
            break