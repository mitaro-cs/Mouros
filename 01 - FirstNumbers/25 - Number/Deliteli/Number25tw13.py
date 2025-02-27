def isprime(n):
    d = 2
    while d**2 <= n:
        if n%d ==0:
            return False
        d += 1
    return True

def maxd(n):
    d = 2
    while d**2 <=n:
        if n%d == 0:
            if isprime(n//d):
                return 0
            else:
                return n//d
        d += 1
    return 0


k = 0
for n in range(550000+1,10**10):
    m = maxd(n)
    if m != 0:
        print(n, m)
        k += 1
        if k == 6:
            break 
            