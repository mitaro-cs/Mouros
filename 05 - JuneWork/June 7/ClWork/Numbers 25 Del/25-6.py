def f(n):
    k = 0
    d = 2
    while d**2 <= n:
        if n%d == 0:
            if d**2 != n:
                k += 2
            else:
                k += 1
        d += 1
    return k 

for i in range(26600,28101):
    k = f(i)
    if k > 0 and k % 13 == 0:
        print(i,k) 