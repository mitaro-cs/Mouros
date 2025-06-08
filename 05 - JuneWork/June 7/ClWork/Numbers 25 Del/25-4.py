def f(n):
    d = 2
    while d**2 <= n:
        if n % d == 0:
            return(n//d + d)
        d += 1
    return 0
k = 0
for i in range(800001,10**10):
    res = f(i)
    if res % 10 == 8:
        print(i,res) 
        k += 1
        if k == 5:
            break
        