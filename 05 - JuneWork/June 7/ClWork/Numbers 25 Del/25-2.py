def m(n):
    d = 2
    while d**2 <= n:
        if n % d == 0:
            return(n//d - d)
        d += 1
    return 0

k = 0
for i in range(850001,10**10):
    res = m(i)
    if res != 0 and res % 5 == 0:
        print(i,res)
        k += 1 
        if k == 6:
            break
        